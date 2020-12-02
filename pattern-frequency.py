# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 23:54:51 2020

@author: Vinod N K
"""


import re
frequency = {}
document_text = open('HHCR.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
number_of_lines = 0
number_of_words = 0
number_of_sentences = len(text_string.split("."))


with open('HHCR.txt', 'r') as f:
    for line in f:
        words = line.split()
        number_of_lines += 1
        number_of_words += len(words)



def sortSecond(val): 
    return val[1]

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

sorted = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

#Top 5 words are
#<word 1(15 characters total including padding)> : <count>
print('Top 5 words are')
for i in range(0,5):
    print(sorted[i][0],(i+1),'(',len(sorted[i][0]), 'characters total including padding) : ',sorted[i][1])

print('Least common word is :',sorted[len(sorted)-1][0])
print('Total Sentences:',number_of_sentences)
print('Total Lines:',number_of_lines)
print('Total Words:',number_of_words)
