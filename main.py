import re

a = '121245abc456 ABC4545ABC4545151065abn_abc Irina, Olga, Petr, yankov@mail.ru, job@hh.ru, small2@ii.net'

pattern = r"@\w+\.\w+"    # at, all alphabet symbol, dot, all alphabet symbol
matches = re.findall(pattern, a)

for i in matches:
    print(i)