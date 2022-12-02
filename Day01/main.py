f = open("input.txt","r")

calories = 0
arr = []

for x in f:
  x = x.strip()
  if x:
    calories += int(x)
  else:
    arr.append(calories)
    calories = 0
arr.sort()
# part 1 output
print(f"Total Calories elf carrying is {max(arr)}")

# part 2 Output
print(f"Total Calories Elves carrying is {sum(arr[-3:])}")
f.close()
