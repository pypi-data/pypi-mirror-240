import os
import sys
import requests
import json

class FileUploader:
    def __init__(self, file, expires=None):
        self.file = file
        self.expires = expires
    def upload(self):
        url = 'https://file.io'
        if self.expires:
            url = '%s?expires=%s' % (url, self.expires)
        if os.path.exists(self.file):
            with open(self.file, 'rb') as f:
                res = requests.post(url, files={'file': f})
        else:
            res = requests.post(
                url,
                files={'file': ('file', self.file)}
            )

        try:
            res.raise_for_status()
        except:
            link = sys.stderr.write(res.text)
            link1 = json.loads(link)
            print (link1["link"])
            raise
        else:
            da = res.text
            daa = json.loads(da)
            print (daa["link"])