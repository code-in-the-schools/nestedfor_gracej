### part one
for i in range(10):
  print ("outer loop | i : ", (i))
  for j in range(10):
    print("outer loop | i : ", i, "inner loop | j : " , j)
    if i != 0 and j != 0 and (i%2) == 1 and (j%2) == 1 :
      print ("odd")
    

