import re
import pandas as pd
import matplotlib.pyplot as plt
import random

dump_file = r'C:\Users\a.shesterikov.NKO\Documents\GitHub\Regular-expressions\emails.txt'  ##################### path to dumpfile emails.txt -------------------- change to your path

input_fule = open(dump_file, mode='r')
my_text = input_fule.read()
# print(my_text)  # output all content from emails.txt

pattern = r"@\w+\.\w+"  # at, all alphabet symbol, dot, all alphabet symbol
matches = re.findall(pattern, my_text)

dy_dict = {'Domain name': matches}  # make dataframe
df = pd.DataFrame(dy_dict)
# df.groupby('Domain name')  # group by column 'Domain name'
# distinct = df.groupby(matches)  # groupped entity

# print(distinct.count().sort_values('Domain name'))

df2 = df.groupby('Domain name').size().reset_index(name='counts')
n = df['Domain name'].unique().__len__() + 1

all_colors = list(plt.cm.colors.cnames.keys())
random.seed(100)
c = random.choices(all_colors, k=n)

# Plot Bars
plt.figure(figsize=(16, 10), dpi=80)
plt.bar(df['Domain name'], df['Domain name'], color=c, width=.5)
for i, val in enumerate(df['Domain name'].values):
    plt.text(i, val, str(val), horizontalalignment='center', verticalalignment='bottom',
             fontdict={'fontweight': 500, 'size': 12})

# Decoration
plt.gca().set_xticklabels(df['Domain name'], rotation=60, horizontalalignment='right')
plt.title("Number of domain name", fontsize=22)
plt.ylabel('# Vehicles')
plt.ylim(0, 16)
plt.grid()
plt.show()