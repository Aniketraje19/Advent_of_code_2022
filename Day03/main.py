def error_item(str1,str2):
  for letter in str1:
    if letter in str2:
      return letter
  return None

def priority_of_item(item):
  ascii = ord(item)
  if item.isupper():
    return ascii - 38  
  return ascii - 96

def find_badge(str1,str2,str3):
  for letter in str1:
    if letter in str2 and letter in str3:
      return letter
  return None
    
f = open("input.txt","r")
sum_priorities = 0
sum_priorities2 = 0
three_rucksacks = []
count = 0

for i in f:
  #  part 1
  i = i.strip()
  first_compartment = i[: (half := len(i)//2)]
  second_compartment = i[half:]
  item = error_item(first_compartment,second_compartment)
  priority_value = priority_of_item(item)
  sum_priorities += priority_value
  # part 2
  if count == 3:
    count = 0
    badge = find_badge(three_rucksacks[0],three_rucksacks[1],three_rucksacks[2])
    sum_priorities2 += priority_of_item(badge)
    three_rucksacks.clear()
  count += 1
  three_rucksacks.append(i)
badge = find_badge(three_rucksacks[0],three_rucksacks[1],three_rucksacks[2])
sum_priorities2 += priority_of_item(badge)

print(sum_priorities)
print(sum_priorities2)

f.close()
