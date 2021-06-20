# fileSync-client-python

uploads an entire directory to a simple object API.

## Upload a directory

with your object API running at http://localhost:3000/block, run the python
script

```
./fileSync.py target_directory
```

**Works with [fileSync](https://github.com/micarlise/fileSync)**

## How this works

fileSync will scan the target_directory and upload each file to the backend
object API.  The ID (filename) of each upload will be the sha256 digest of the
file contents.  This will automatically deduplicate the uploads; if you have two
filenames.
