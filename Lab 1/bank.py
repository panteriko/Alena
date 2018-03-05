import account
import evro

def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))

    result = account.calculate_income(rate, money, period)
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода: ", result)

    currency = int(input("Укажите код валюты: доллары - 1, евро - 2, йена - 3, юань - 4, фунт стерлингов - 5 "))
    a = evro.procedure_perevod(result, currency)
    print("Итого:", a)


if __name__ == "__main__":
    main()
