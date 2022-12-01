import requests
import shutil
import os
s = 'link to file to download'
dirname, filename = os.path.split(s)
r = requests.get(s, stream = True)
if r.status_code == 200:
    with open(filename, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
