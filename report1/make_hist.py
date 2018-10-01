# coding: utf-8

import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser(description='Please input path')
parser.add_argument('-t', nargs=1, help='Please input text path for list number', required=True)
parser.add_argument('-g', nargs=1, help='Please input graph path for histgram', required=True)
args = parser.parse_args()

text_path = args.t[0]
graph_path = args.g[0]
int_list = []

# for i in range(100):
#   int_list.append(random.randint(0, 100))
# print(int_list)

int_list = np.random.randint(0, 100, 100)
print(int_list)
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

n, bins, patches = plt.hist(int_list, edgecolor='yellow', bins=10, range=(0, 100))
#plt.savefig('hist_' + graph_path)
print(n)
print(bins)
print(patches)
n2, bins2, patches2 = plt.hist(int_list, edgecolor='black', normed=True, cumulative=True, alpha=0.5, range=(0, 100))
print(n2)
print(n2*100)
print(bins2)
print(patches2)
point = n2 * 10

plt.plot(x, point, marker='o', color='red')
plt.title("Histgram")
plt.xlabel("x")
plt.ylabel("y")
# plt.show()
plt.savefig(graph_path)

str_list = np.array(int_list, dtype=str)
str_frequency = np.array(n, dtype=str)
str_relative = np.array(n2, dtype=str)


with open(text_path, mode='w') as f:
  for i in range(100):
    f.write(str_list[i] + ' ')
  f.write('\n階級（度数） + \n')
  for xx in range(10):
    f.write(str_frequency[xx] + ',')  
  f.write('\n累積相対度数\n')
  for xx in range(10):
    f.write(str_relative[xx] + ',')
  

print('finish!')
