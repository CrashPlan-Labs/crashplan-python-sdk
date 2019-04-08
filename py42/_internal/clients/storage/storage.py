from py42._internal.base_classes import BaseStorageClient
from py42._internal.clients.storage.security import StorageSecurityClient
from py42._internal.clients.storage.restore import StorageRestoreClient
from py42._internal.clients.storage.archive import StorageArchiveClient


class StorageClient(BaseStorageClient):
    def __init__(self, session):
        super(StorageClient, self).__init__(session)
        self._session = session
        self._archive_client = StorageArchiveClient(session)
        self._restore_client = StorageRestoreClient(session)
        self._security_client = StorageSecurityClient(session)

    @property
    def archive(self):
        return self._archive_client

    @property
    def restore(self):
        return self._restore_client

    @property
    def security(self):
        return self._security_client
