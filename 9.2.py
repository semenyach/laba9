import csv
a='Нужно купить:\n'
sum=0
with open('file.csv', newline='', encoding='utf-8 ') as fp:
    reader= csv.reader(fp)
    heading = next(fp)
    for row in reader:
        a=a+row[0]+' - '+row[1]+ ' шт. за '+ row[2] + ' руб.\n'
        sum+=int(row[2])
print(a+'Итоговая сумма = ', sum, ' руб' )