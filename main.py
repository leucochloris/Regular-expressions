import re

a = '121245abc456 ABC4545ABC4545151065abn_abc'

pattern = re.compile(r"ABC")
matches = re.finditer(r"abc", a)



for i in matches:
    print(i.span())     # place in massive where we find it