f = open("input.txt","r")

total_score = 0
total_score2 = 0

for i in f:
  score = 0
  score2 = 0
  if i[2] == "X":
    score += 1
    if i[0] == "A":
      score2 += 3
    elif i[0] == "B":
      score2 += 1
    elif i[0] == "C":
      score2 += 2


  elif i[2] == "Y":
    score += 2
    score2 += 3
    if i[0] == "A":
      score2 += 1
    elif i[0] == "B":
      score2 += 2
    elif i[0] == "C":
      score2 += 3
      
  elif i[2] == "Z":
    score += 3
    score2 += 6
    if i[0] == "A":
      score2 += 2
    elif i[0] == "B":
      score2 += 3
    elif i[0] == "C":
      score2 += 1
      

  if (i[0]=="A" and i[2]=="X") or (i[0]=="B" and i[2]=="Y") or (i[0]=="C" and i[2]=="Z"):
    score += 3
  elif (i[0]=="A" and i[2]=="Y") or (i[0]=="B" and i[2]=="Z") or (i[0]=="C" and i[2]=="X"):
    score += 6
  elif (i[0]=="A" and i[2]=="Z") or (i[0]=="B" and i[2]=="X") or (i[0]=="C" and i[2]=="Y"):
    score += 0
  total_score += score
  total_score2 += score2 
print(total_score)
print(total_score2)

f.close()
