# задача 1

# import random
# spisok = [random.randint(0, 9) for i in range(20)]
# print(spisok)
# for nomer in spisok:
#     if spisok.count(nomer) == 1:
#         print(nomer, end=' ')


# задача 5
s = {'торт': [{'Состав:': ['мука', 'яйца', 'сахар', 'вишня', 'шоколад', 'глазурь']}, 5, 'руб. за 100 г', 1000, 'г'],
     'пирожное': [{'Состав:': ['заварное тесто', 'яйца', 'сахар', 'сгущенка']}, 2, 'руб.за 100 г', 1500, 'г'],
     'маффин': [{'Состав:': ['мука', 'яйца', 'сахар', 'шоколад', 'сахарная пудра']}, 3, 'руб.за 100 г', 1500, 'г'],
     'эклер': [{'Состав:': ['мука', 'яйца', 'сахар', 'белковый крем']}, 2, 'руб.за 100 г', 2000, 'г'],
     'мороженое': [{'Состав:': ['сливки', 'начинка']}, 3, 'руб.за 100 г', 5000, 'г']}
print('Здравствуйте! Если вы захотите покинуть нашу кондитерскую, введите n.')
while True:
    a = input('Что Вам подсказать? описание, цену, количество, всю информацию?')
    if a == 'описание':
        for i in s:
            print(i,'--', s[i][0])
    elif a == 'цену':
        for i in s:
            print(i,'--', s[i][1], s[i][2])
    elif a == 'количество':
        for i in s:
            print(i,'--', s[i][3], s[i][4])
    elif a == 'всю информацию':
        print('Ассортимент:')
        for i in s:
            print(i, '--', s[i][0], ' --', s[i][1], '--', s[i][2], '--', s[i][3], s[i][4] )
    b = input('Вы готовы сделать заказ?(да/нет)',)
    if b == 'да':
        break
    elif b == 'n':
        print('Досвидания, заходите к нам еще!')
        break
    else:
        continue

sh_l = {}  # пустой чек
summa = 0  # сумма чека

while True:
    a = input('Что вы закажите?')
    if a == 'n':
        break
    b = float(input('Сколько:'))

    if a not in sh_l:
        sh_l[a] = b,'единица товара', s[a][1], s[a][2], s[a][3], s[a][4]  # добавляем в чек товар и цену за неск-ко кг.
    summa += b * s[a][1]  # прибавляем сумму в чек
    s[a][3] -= b*100  # переучет в магазине оставшихся продуктов
for i in s:
    print(i, '--', s[i][1], ' --', s[i][2], '--', s[i][3], s[i][4])
print('Ваш чек:''\n', sh_l)
print('К оплате:', summa)
print('Осталось в Кондитерской:', s)
print('Досвидания, заходите к нам еще!')

