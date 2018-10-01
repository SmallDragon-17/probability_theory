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

plt.hist(int_list,  bins=10)
plt.title("Histgram")
plt.xlabel("x")
plt.ylabel("y")
# plt.show()
plt.savefig(graph_path)

str_list = np.array(int_list, dtype=str)

with open(text_path, mode='w') as f:
  for i in range(100):
    f.write(str_list[i] + ' ')

print('finish!')
