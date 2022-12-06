f = open("input.txt","r")
arr = []
stack = []
stack_height = 0

for i in f:
  if  not(i.strip()):
    break
  arr2 = []
  for j in range(0,len(i)+1,4):
    arr2.append(i[j:j+4].strip())
  arr.append(arr2)
  stack_height += 1
stack_height -= 1
total_stacks = int(arr[-1][-2])

for i in range(0,total_stacks):
  temp = []
  for j in range(0,stack_height):
    temp.append(arr[j][i])
  stack.append(temp)

# Removing the empty strings and reversing the list
for i in range(0,total_stacks):
  stack[i] = ' '.join(stack[i]).split()
  stack[i].reverse()

stack2 = stack[:]
step = []

for i in f:
  step = i.split()
  move = int(step[1])
  from_ = int(step[3])-1
  to = int(step[5])-1

  for j in range(0,move):
    crate = stack[from_].pop()
    stack[to].append(crate)

  # part 2
  stack2[to].extend(stack2[from_][-move:])
  stack2[from_] = stack2[from_][:-move]

# printing part1 Answer
part1Ans = ''
for i in range(0,total_stacks):
  part1Ans += " ".join((stack[i][-1]))
  
part2Ans = ''
for i in range(0,total_stacks):
  part2Ans += " ".join((stack2[i][-1]))

print(part1Ans)
print(part2Ans)

f.close() 
