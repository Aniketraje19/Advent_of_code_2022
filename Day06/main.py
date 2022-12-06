def solve(filename="input.txt",char=4):
  f = open(filename,"r")
  signal = f.readline()
  flag = True 
  next = char
  prev = 0
  while flag:
    word = signal[prev:next]
    next += 1
    prev += 1
    for j in word:
      if word.count(j) > 1:
        break 
      if word[-1] == j:
        flag = False 
  f.close()
  return next-1
 
print(solve('input.txt',4))
print(solve('input.txt',14))
