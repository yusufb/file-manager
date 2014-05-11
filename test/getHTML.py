from urllib import urlopen
from HTMLParser import HTMLParser

fileFormat = "tff"

url = "http://www.fileinfo.com/extension/" + fileFormat
page = urlopen(url).read()

print page


