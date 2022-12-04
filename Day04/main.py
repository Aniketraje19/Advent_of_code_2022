import re
f = open("input.txt", "r")
count = 0
count2 = 0
for i in f:
  i = i.strip()
  arr = re.split(",|-",i)
  arr = list(map(int,arr))
  range_a = set(range(arr[0],arr[1]+1))
  range_b = set(range(arr[2],arr[3]+1))
  #part 1
  if range_a.issubset(range_b) or range_b.issubset(range_a):
    count += 1
    
  #part 2
  x = range_a.intersection(range_b)
  if x:
    count2 += 1
  
print(count)
print(count2)
f.close()
