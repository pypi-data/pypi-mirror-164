import queue
import threading
from logging import Logger
from queue import Queue
from types import TracebackType
from typing import Any, Callable, Optional
from uuid import UUID

from layer.clients.logged_data_service import LoggedDataClient
from layer.contracts.logged_data import LoggedData
from layer.logged_data.data_logging_request import DataLoggingRequest
from layer.logged_data.file_uploader import FileUploader
from layer.logged_data.logged_data_destination import LoggedDataDestination


WAIT_INTERVAL_SECONDS = 1


class QueueingLoggedDataDestination(LoggedDataDestination):
    def __init__(self, client: LoggedDataClient, logger: Logger) -> None:
        self._logged_data_client = client
        self._logger = logger
        self._files_storage = FileUploader()

        self._sending_errors: str = ""
        self._stop_reading = False
        self._local_queue: Queue[DataLoggingRequest] = Queue()
        self._reading_thread = threading.Thread(target=self._execute_elem_from_queue)

    def __enter__(self) -> "QueueingLoggedDataDestination":
        self._reading_thread.start()
        return self

    def __exit__(
        self,
        exc_type: Optional[BaseException],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        self._exit()

    def get_logged_data(
        self,
        tag: str,
        train_id: Optional[UUID] = None,
        dataset_build_id: Optional[UUID] = None,
    ) -> LoggedData:
        return self._logged_data_client.get_logged_data(
            tag=tag, train_id=train_id, dataset_build_id=dataset_build_id
        )

    def receive(
        self,
        func: Callable[[LoggedDataClient], Optional[Any]],
        data: Optional[Any] = None,
        break_url: bool = False,
    ) -> None:
        self._local_queue.put_nowait(
            DataLoggingRequest(
                files_storage=self._files_storage,
                queued_operation_func=lambda: func(self._logged_data_client),
                data=data,
                break_url=break_url,
            )
        )

    def get_logging_errors(self) -> Optional[str]:
        self._exit()
        return (
            None
            if len(self._sending_errors) == 0
            else f"WARNING: Layer was unable to log requested data because of the following errors:\n{self._sending_errors}"
        )

    def _exit(self) -> None:
        if not self._stop_reading:
            self._stop_reading = True
            # give reading thread at most 10 seconds to complete uploading data, if still uploading.
            self._reading_thread.join(timeout=10)
            self._flush_queue()
            self._files_storage.close()

    def _execute_elem_from_queue(self) -> None:
        while not self._stop_reading:
            try:
                execution_item = self._local_queue.get(
                    block=True, timeout=WAIT_INTERVAL_SECONDS
                )
                execution_item.execute()
            except queue.Empty:
                # no item in the queue, wait for another
                pass
            except Exception as ex:
                self._log_exception(ex)

    def _flush_queue(self) -> None:
        while not self._local_queue.empty():
            execution_item = self._local_queue.get(block=False)
            try:
                execution_item.execute()
            except Exception as ex:
                self._log_exception(ex)
        return

    def _log_exception(self, ex: Exception):
        self._logger.warning("Could not log requested data: %s", str(ex))
        self._append_to_error_message(ex)

    def _append_to_error_message(self, ex: Exception) -> None:
        self._sending_errors = self._sending_errors + f"Exception: {ex}\n"
