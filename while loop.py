#while True: #1 > 0 : # True # while работает бесконечно как и if
#    namber = int(input('Введите число:')) # что бы не копировать код при необходимости ввести (Циклы While)
#    if namber  % 2 == 0 :
#        print ( 'Число четное' )
#    else:
#        print ('Не четное') 
#        continue
#        print ('Меня забыли ')
#        #break # Остановка повторений
#print ('Больше нуля')

my_list =[42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while True: 
    if my_list [i] > 0 :
        print(my_list[i])
    elif my_list[i] < 0:
        break
    i = i+1
