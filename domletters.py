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