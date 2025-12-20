k=0

for s in open('9_25348.csv'):
    flag=0
    a = (list(map(int, s.split(';'))))
    
    for i in (a):
        if a.count(i)==3:
            flag=1 #проверка кол-ва элементов, которые встречаются 3 раза
            
    a = sorted(a) #сортируем список, чтобы легко достать старший элемент
    if a.count(a[-1])==1 and flag==1 and len(set(a))==5: # проверяем, что остальные элементы не повторяются
        k+=1
        
print(k)
