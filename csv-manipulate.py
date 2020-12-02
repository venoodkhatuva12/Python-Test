# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:48:10 2020

@author: Vinod NK
"""
import csv


import matplotlib.pyplot as plt

numerial_col_1 = []
numerial_col_2 = []
numerial_col_3 = []

def Average(lst):
    return sum(lst) / len(lst)
first = True
with open('broadway.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        if first == False:    
            numerial_col_1.append(row[7])
            numerial_col_2.append(row[8])
            numerial_col_3.append(row[9])
        else:
            first= False
            pass

min_value_1 = min(numerial_col_1)
min_value_2 = min(numerial_col_2)
min_value_3 = min(numerial_col_3)
print("MIN")
print(min_value_1," | ",min_value_2," | ",min_value_3)

max_value_1 = max(numerial_col_1)
max_value_2 = max(numerial_col_2)
max_value_3 = max(numerial_col_3)
print("MAX")
print(max_value_1," | ",max_value_2," | ",max_value_3)




fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['Column 1', 'Column 2', 'Column 3']
students = [min_value_1,min_value_2,min_value_3]
ax.bar(langs,students)
ax.set_ylabel('MIN')
ax.set_title('MINIMUM COMPARISON')
plt.show()


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['Column 1', 'Column 2', 'Column 3']
students = [max_value_1,max_value_2,max_value_3]
ax.bar(langs,students)
ax.set_ylabel('MAX')
ax.set_title('MIXIMUM COMPARISON')
plt.show()
