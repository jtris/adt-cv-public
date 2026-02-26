data = 3,7,6,11,5,5,8,9
prev = 0

for value in data:
  print(value/(value - prev))
  prev = value


