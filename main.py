### primary objective 
for i in range(2):
  print ("outer loop | i : ", (i))
  for j in range(2):
    print("outer loop | i : ", i, "inner loop | j : " , j)
    if i != 0 and j != 0 and (i%2) == 1 and (j%2) == 1 :
      print ("odd")
    
### second

char = input('>> enter a char: ')
num = int(input('>>enter a positive number(>5): '))

for i in range(1, num + 1):
  text = ' '
  for j in range(i):
    text += char
  print(text)

for i in range(1, num + 1):
  text = ' '
  for j in range(num - i):
    text += char
  print(text)

for i in range(1, num + 1):
  text = ' '
  for j in range(num + 1) :
    text += char
  print(text)