# задание 1
print('книга')
print('игра в прятки')
a = 'игра в прятки'
print(a)
arm_23 = 23
print(arm_23)

ask_234 = 12
print(ask_234 * 10)

ask3333 = 234
print(ask3333)
df = 45
print(df / 2)
print(df // 2)
print(df * 10)
print(df ** 4)

#название = input()
#print('название', название)

#магазин = input()
#print('магазин', магазин)


# задание 2
t = 3567
print(t // 3600, t // 60, t % 60)
print('чч:0', 'мм:59', 'cc:27')
print(t // 3600, ':', t // 60, ':', t % 60)


#задание 3
#n = input()



#print(n)
#print(int(n))
n = 3
print(n * 1 + n * 11 + n * 111)

#задание 4
num = 8934756
result = 0
while num > 0:
    cur_digital = num % 10
    if cur_digital > result:
        result = cur_digital
    num //= 10
print(result)












