import requests

print(requests.__version__)
print(requests.get("http://www.google.com"))
r = requests.get("https://raw.githubusercontent.com/sxhuang9385/cmput404/master/find_version.py")

print(r.text)