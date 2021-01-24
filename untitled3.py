# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:04:39 2019

@author: Programming
"""

f=open("fasta1.txt", "r")
if f.mode == 'r':
    contents =f.read()
   # print(contents)
    print("count of fasta")
    print(len(contents))
    
    
#def findG(contents):
    j=0
    countG=0
    while j<len(contents):
        if contents[j]=='G':
            countG=countG+1
        j=j+1

print("no. of G")
print(countG)

j=0
countC=0
while j<len(contents):
    if contents[j]=='C':
        countC=countC+1
    j=j+1
print("no. of C")
print(countC)

count= countC+countG

print("total count of c and g")
print(count)
           