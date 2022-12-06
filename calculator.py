val1 = 60
val2 = 61
val3 = 62
val4 = 63
total1 = 1235
total2 = 1235
total3 = 1235
total4 = 1235
for s in range(26):
  total1 -= val1
  total2 -= val2
  total3 -= val3
  total4 -= val4
  val1 -= 1
  val2 -= 1
  val3 -= 1
  val4 -= 1
  
print("Val1: " + str(total1))
print("Val2: " + str(total2))
print("Val3: " + str(total3))
print("Val4: " + str(total4))
  