import re
import pandas as pd

dump_file = r'C:\Users\a.shesterikov.NKO\Documents\GitHub\Regular-expressions\emails.txt'  # path to dumpfile emails.txt
input_fule = open(dump_file, mode='r')
my_text = input_fule.read()
# print(my_text)    # output all content from emails.txt


pattern = r"@\w+\.\w+"  # at, all alphabet symbol, dot, all alphabet symbol
matches = re.findall(pattern, my_text)

# for i in matches:
#     print(i)

print(pd.unique(matches))  # output unique vallues
