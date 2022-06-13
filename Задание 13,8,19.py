vol = 0    # количество билетов
summ = 0.00 #Сумма к оплате
age = 0  # возраст посетителя
ques = ""

while True:
    try:
        vol = int(input("Укажите количество покупаемых билетов:\t"))
    except ValueError:
        print("Вы ввели некорректное число")
    else:
        if vol <1:
            print("Количество билетов указано неправильно")
        else:
            break

print("")
i = 0
while i < vol:
    try:
        ques = 'Укажите возраст посетителя № ' + str(i+1) + ', лет:\t'
        age = int(input(ques))

    except ValueError:
        print("Вы ввели некорректное число")

    else:
        if 0 <= age <18:
            print("Стоимость билета 0 руб")
            print("Сумма к оплате ", summ, "руб")
            i += 1

        elif 18 <= age < 25:
            summ += 990
            print("Стоимость билета 990 руб")
            print("Сумма к оплате ", summ, "руб")
            i += 1

        elif 25 <= age <=110:
            summ += 1390
            print("Стоимость билета 1390 руб")
            print("Сумма к оплате ", summ, "руб")
            i += 1
        else:    #100 < age < 0:
            print("Вы ввели некорректный возраст")

    print("")

if vol > 3:
    summ *= 0.9
    print ("За покупку более 3-х билетов даём скидку 10%!")

print("ИТОГОВАЯ СУММА К ОПЛАТЕ -", summ, "руб")
