# joblibgcs

A google cloud storage memory backend for joblib

- inspired by and closely following [joblib-s3](https://github.com/aabadie/joblib-s3)

- relies heavily on [gcsfs](https://github.com/fsspec/gcsfs)

```py
import numpy as np
from joblib import Memory, register_store_backend
from joblibgcs.gcs_backend import GCSFSStoreBackend

register_store_backend("gcs", GCSFSStoreBackend)

mem = Memory(
    "cache-location",
    backend="gcs",
    verbose=100,
    backend_options={"project": "project-name"},
)

multiply = mem.cache(np.multiply)
array1 = np.arange(10000)
array2 = np.arange(10000)

result = multiply(array1, array2)
print(result)

result2 = multiply(array1, array2)
print(result2)
```