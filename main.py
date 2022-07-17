import re
import pandas as pd
import matplotlib.pyplot as plt

dump_file = r'C:\Users\prove\Documents\GitHub\Regular-expressions\emails.txt'  # path to dumpfile emails.txt -------------------- change to your path

input_fule = open(dump_file, mode='r')
my_text = input_fule.read()
# print(my_text)  # output all content from emails.txt

pattern = r"@\w+\.\w+"  # at, all alphabet symbol, dot, all alphabet symbol
matches = re.findall(pattern, my_text)

dy_dict = {'Domain name': matches}  # make dataframe
df = pd.DataFrame(dy_dict)
df.groupby('Domain name')  # group by column 'Domain name'

distinct = df.groupby(matches)  # groupped entity

# print(distinct.count().sort_values('Domain name'))

plt.plot(distinct.count().sort_values('Domain name'))
plt.ylabel('Count of domain name')
plt.grid()
plt.show()
