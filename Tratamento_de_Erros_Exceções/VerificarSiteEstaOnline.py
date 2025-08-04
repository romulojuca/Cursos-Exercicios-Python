import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://google.com')
except urllib.error.URLError:
    print('O site Pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim.')
    print(site.read())
