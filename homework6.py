#phone_booke={'Denis': [89263775565, 123,], 'Max': 438590384095} #Денис Макс это ключи
#print (phone_booke['Denis'])
#phone_booke['Denis']=48789373847382, 111 
#phone_booke['Vitaly']=392483949032
#del phone_booke['Max']
#phone_booke.update({'Sasha': 84574949385749, #Добавляет несколько мтрок 
                  # 'Alex': 89457457439})
#print(phone_booke)
#print(phone_booke.get('Denis'))  #если ключа не будет найдето, будет какой то значение 
#print(phone_booke.get('Nik', 'Такого ключа нет')) # Не добовляет а пишет None
#print(phone_booke)
#a = phone_booke.pop('Vitaly') #Метод pop удаляет ключ Vitaly и возвращает значение цифру
#print(phone_booke)
#print(a)
#print(phone_booke.keys()) # Вытаскивает только ключи-имена телефоны не берет 
#print(phone_booke.values())# Показывает только значения 
#print(phone_booke.items()) # Возвращает целые пары 
#print(phone_booke)
#set_={1,2, 3, 4, 5, 1,2,3, 'Strong',True, (1,2,3)} # Сет хранит только уникальные значения 
#print(set_)
#list=[1,2,3,2,1,3]
#ist=set(list)
#print(list)
#print(list.remove(1)) #удаление цифры discard(не будет показывать ошибку если нет цифры), rimov
#print(list.add(10)) #Добавить значение add 
#print(list)
my_dict= {'Anton': [1980,],'Yuriy': [1994,],'Irina':[1992,]}
print(my_dict['Anton'])
print(my_dict.get('Denis' 'такого нет '))
b=my_dict.pop('Anton')
print(my_dict.items())
my_set={1,2,3,4,5,4,3,2,1,1,2,3, 'Яблок',True,}
print(my_set)
my_set={1,2,3,4,5,4,3,2,1,1,2,3,10,11, 'Яблок',True,}
print(my_set.discard(10))