import hashlib
import os
import threading
from pathlib import Path

from .base import BaseCacheStorageManager


class DiskStorageManager(BaseCacheStorageManager):
    """
    Managing key:value storage on local file system
    """

    WRITABLE_PERMISSIONS = 775
    JM_CACHE_LOG_NAME = "jm-cache-log"

    def __init__(self, namespace: str, path):
        self.namespace = namespace
        self.storage_location = None
        self.path = path
        self._init_file_storage()

    def _init_file_storage(self):
        # Check the directory if exists, attempt to create if not
        if not os.path.isdir(self.path):
            Path(self.path).mkdir(
                parents=True,
                exist_ok=True
            )
        hasher = hashlib.sha256()
        hasher.update(bytes(self.namespace, "utf8"))
        file_name = hasher.hexdigest()
        self.storage_location = os.path.join(os.path.abspath(self.path), file_name)

    def _read_file(self):
        try:
            with open(self.storage_location, "rb") as f:
                file_data = f.read()
                if not file_data:
                    return {}
                return self.deserialize(file_data)

        except FileNotFoundError:
            return {}

    def _write_file(self, data: dict):

        with threading.Lock():
            with open(self.storage_location, "wb") as f:
                data = self.serialize(data)
                f.write(data)
        return True

    def get(self, key):
        """
        return associated value from the local disk file.
        :param key: str:int
        :return: str|int
        """
        data = self._read_file()
        return data.get(key)

    def pop(self, key):
        data = self.get(key)
        self.delete(key)
        return data

    def set(self, key, value):
        data = self._read_file()
        data[key] = value
        return self._write_file(data)

    def delete(self, key):
        """
        Delete the key and value from the storage.
        Do not delete the storage itself.
        """
        data = self._read_file()
        data.pop(key)
        self._write_file(data)

    def truncate(self):
        """
        Remove everything in the file
        Set file content to and empty dict: {}
        """
        return self._write_file({})
