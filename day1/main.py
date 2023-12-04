import pandas as pd
import regex as re

sums1 = []
sums2 = []

def getNumbers1(str):
    array = re.findall(r'\d', str)
    return array

def getNumbers2(str):
   array = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine|zero', str, overlapped=True)
   return array


data = pd.read_csv('input.txt', sep=" ", header=None, names=["old_value"])

for i in data['old_value']:
    values = getNumbers1(i)
    if len(values) == 1:
      sums1.append(int(values[0]+values[0]))
    else:
       sums1.append(int(values[0]+values[len(values)-1]))

data["part1_value"] = sums1

for i in data['old_value']:
   numbers_dictionary = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
   values = getNumbers2(i)
   #  sums2.append(values)
   if len(values) == 1:
      if values[0].isnumeric():
         sums2.append(int(values[0]+values[0]))
      else:
         sums2.append(int(numbers_dictionary.get(values[0])+numbers_dictionary.get(values[0])))
   else:
      first_char = values[0]
      last_char = values[len(values)-1]
      if first_char.isnumeric():
         if last_char.isnumeric():
            sums2.append(int(first_char+last_char))
         else:
            sums2.append(int(first_char+numbers_dictionary.get(last_char)))
      else:
         if last_char.isnumeric():
            sums2.append(int(numbers_dictionary.get(first_char)+last_char))
         else:
            sums2.append(int(numbers_dictionary.get(first_char)+numbers_dictionary.get(last_char)))


data["part2_value"] = sums2

#  print(data.head(50))

print(data.part1_value.sum())
print(data.part2_value.sum())