n=int(input())
def counts(n):
    total_s=0
    off_s=0
    on_s=0
    for i in range(n):
        print('Фамилия:','Имя:','Возраст:','Формат:')
        data=str(input())
        data=data.split(' ')
        surname=data[0]
        name=data[1]
        age=int(data[2])
        part_format=data[3]=='True'
        part_format=str(part_format)
        total_s +=1
        if part_format=='True':
            off_s +=1
        if part_format=='False':
            on_s +=1
    
    print(surname, name, age, part_format)
    print('Очное:',off_s,'Заочное:',on_s)
counts(n)
