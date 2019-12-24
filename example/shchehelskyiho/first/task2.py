result = []
mas = input('Введіть массив: ')
mas = mas.split(' ')

for i in mas:
    for j in i:
        if(j.isupper()):
            result.append(i)
            break
print(result)
