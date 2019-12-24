mas = [[], [], 1, 2, 33.3, 'b', 'c', 'd', 'word', 'crowd']
numericType = []
textType = []
text = ''

for i in mas:
    kind = type(i)

    if (kind == int or kind == float or kind == complex):
        numericType.append(i)
    elif (kind == str):
        textType.append(i)

for word in textType:
    text += word + ' '

print('Сума числових ел-тів:', sum(numericType))
print('Об\'єднання рядкових ел-тів:', text)