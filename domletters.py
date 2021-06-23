#!/usr/bin/env python

# Mack Foggia - CS 461P - HW 1 - 6/28/2021


fullInput = ""

# Read in all input into a single string
while(1):
  try:
    fullInput += input()
    fullInput += ' '
  except:
    break

# Get rid of upper case letters
fullInput = fullInput.lower()

# Split into a list of strings around spaces
inputList = fullInput.split(' ')



total = 0
# Loop through each word
for word in inputList:
  # Check if it is a valid word 
  if word.isalpha():
    # Reset count dict for each new word
    count = {}
    for char in word:
      # Count instances of each char
      if char in count:
        count[char] += 1
      else:
        count[char] = 1

    # Find the max count and add it to total 
    # There's probably a slicker way to do this but it works
    max = 0
    for i, j in count.items():
      if j > max:
        max = j
    total += max

# Output result
print(total)