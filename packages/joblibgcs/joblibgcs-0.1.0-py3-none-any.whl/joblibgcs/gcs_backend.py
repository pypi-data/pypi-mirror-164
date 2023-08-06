from joblib._store_backends import StoreBackendBase, StoreBackendMixin
from gcsfs import GCSFileSystem

class GCSFSStoreBackend(StoreBackendBase, StoreBackendMixin):
    """A StoreBackend for google cloud storage"""

    def configure(self, location, verbose=0, backend_options={"project": None}):
        """Configure the store backend."""
        # compress = backend_options["compress"]
        self.storage = GCSFileSystem(
            project=backend_options["project"],
        )

        self.location = location
        if not self.storage.exists(self.location):
            self.storage.mkdir(self.location, create_parents=True)

        # compression not yet supported
        self.compress = False

        # Memory map mode is not supported
        self.mmap_mode = None

    def _open_item(self, fd, mode):
        return self.storage.open(fd, mode)

    def _item_exists(self, path):
        return self.storage.exists(path)

    def _move_item(self, src, dst):
        self.storage.mv(src, dst)

    def clear_location(self, location):
        """Check if object exists in store."""
        self.storage.rm(location, recursive=True)

    def create_location(self, location):
        """Create object location on store."""
        self.storage.mkdir(location, create_parents=True)

    def get_items(self):
        """Return the whole list of items available in cache."""
        return []