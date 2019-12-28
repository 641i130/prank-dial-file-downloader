import requests
from xml.dom import minidom
import os

def download(url):
    xurl = url.split("/")
    file_name = xurl[-1]
    newpath = ""
    for part in xurl:
        if xurl.index(part) is 0 or xurl.index(part) is 1 or part is file_name:
            continue
        else:
            newpath+=("/"+part)
    newpath = "." + newpath
    print(newpath)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    print("Downloading: {}".format(file_name))
    if file_name:
        with open(newpath+"/"+file_name, "wb") as file:
            response = requests.get(url)
            file.write(response.content)

mydoc = minidom.parse("prankdial.xml")
keys = mydoc.getElementsByTagName('Contents')
for link in keys:
    raw = link.getElementsByTagName('Key')[0].firstChild.nodeValue
    link = "https://cdn-pranks.prankdial.com/"
    download(link+raw)
