#coding:utf-8
from PIL import Image
import io
import urllib.request
url="http://yx-kbs-ks3.haofenshu.com/images/e5df3028d97f90d16475708b49c5cc54.jpg@w=800&h=1239"
file = urllib.request.urlopen(url)
tmpIm = io.BytesIO(file.read())
im = Image.open(tmpIm)

print(im.format, im.size, im.mode)