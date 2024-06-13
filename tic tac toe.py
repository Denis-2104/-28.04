number = 9
n = ''
for i in range (1, number //2+1 ):
    for j in range (i+1, number):
        if number % (i + j) == 0:
            n = n+  str (i) + str (j) 
print (n)
