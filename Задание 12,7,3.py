per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = (input("Введите сумму вложения:"))
money= float(money)

print("накопленные средства за год вклада:")
deposit.append(round(money/100*per_cent["ТКБ"],2))
print ("ТКБ ",deposit[0], "руб")
deposit.append(round(money/100*per_cent["СКБ"],2))
print ("СКБ ",deposit[1], "руб")
deposit.append(round(money/100*per_cent["ВТБ"],2))
print ("ВТБ ",deposit[2], "руб")
deposit.append(round(money/100*per_cent["СБЕР"],2))
print ("СБЕР ",deposit[3], "руб")

deposit.sort()
print("Максимальная сумма, которую вы можете заработать - ",deposit[-1])

