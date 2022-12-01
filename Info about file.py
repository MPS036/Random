import os.path
from datetime import datetime
path = r'import the path to the file'
size = os.path.getsize(path)
ksize = size // 1024
atime = os.path.getatime(path)
mtime = os.path.getmtime(path)
print('Size: ', ksize, ' KB')
print('Date of last use: ', datetime.fromtimestamp(atime))
print('Last time edited: ', datetime.fromtimestamp(mtime))
