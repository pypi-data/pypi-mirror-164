from typing import Any, Callable, Optional

from layer.logged_data.file_uploader import FileUploader


class DataLoggingRequest:
    def __init__(
        self,
        files_storage: FileUploader,
        queued_operation_func: Callable[[], Optional[Any]],
        data: Optional[Any] = None,
        break_url: bool = False,
    ) -> None:
        self._queued_operation_func = queued_operation_func
        self._data = data
        self._files_storage = files_storage
        self._break_url = break_url

    def execute(self) -> None:
        maybe_presigned_url = self._queued_operation_func()
        if self._data is not None and maybe_presigned_url is not None:
            self._files_storage.upload(
                url=maybe_presigned_url, break_url=self._break_url, data=self._data
            )
