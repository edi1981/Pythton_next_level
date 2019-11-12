import urllib.request
import webbrowser

content = urllib.request.urlopen("http://www.wp.pl")
print(type(content))
print(content.code)
if content.code == 200:
    webbrowser.open("http://www.wp.pl")
# elif content.code == 404:
#     print("Not Found")