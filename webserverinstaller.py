import time
import os
import requests

print('PyBuild - V1.0.0')
print('> build github.webserver.zip 0.0.0.0 -r false')
time.sleep(1)
print('Building File - py.webserver.app by NotRealGuest (GitHub)')
url = 'https://aaronverdep.github.io/webserver.zip'

get =  requests.get(url)

with open(fr'C:\Users\{os.getlogin()}\Desktop\webserver.zip', 'wb') as f:
    f.write(get.content)
