#!/usr/bin/env python

# Mack Foggia - CS 461P - HW 1 - 6/28/2021


fullInput = ""

while(1):
  try:
    fullInput += input()
    fullInput += ' '
  except:
    break

inputList = fullInput.split(' ')

print(inputList)

total = 0
for word in inputList:
  count = {}
  word = word.lower()
  for char in word:
    if char in count:
      count[char] += 1
    else:
      count[char] = 1

  max = 0
  for i, j in count.items():
    if j > max:
      max = j
  print(max)