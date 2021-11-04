n = int(input("Сколько уроков? : " ))
o = 0
g = 0
k = 0
l = 0
T = 0
        
for i in range(n):
        
  sub = str(input("Урок: "))
  mark = int(input("Оценка :"))
  
  if mark == 5 :
      o += 1
      k += 5
      l += 1
  elif mark == 3:
      g += 1
      k += 3
      l += 1
  if mark == 4:
      k += 4
      l += 1
  elif mark == 2:
      k += 2
      l += 1

T = k/l
              
print("~~~-=- Пяторок - " + str(o) + " !-=-~~~")
print("~~~-=- Тройки, это плохо... - " + str(g) + " !-=-~~~")
print("~~~-=- Общий балл ~~~-=-\n          " + str(T) + "")
