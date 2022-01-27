import datetime
from dateutil.relativedelta import relativedelta

date = "31.01.2021" # начальная дата для вклада, формат ДЕНЬ.МЕСЯЦ.ГОД через точку
periods = 7 # количество месяцев по вкладу
amount = 10000 # сумма вклада
rate = 6 # процент по вкладу
deposit = {}

for i in range(periods):
    amount = amount * (1 + rate/12/100) # к сумме вклада добавляется сумма по процентам за этот месяц
    deposit[date] = round(amount, 2) # округляем число до двух знаков после запятой
    date_time_obj = datetime.datetime.strptime(date, '%d.%m.%Y') # переводим дату-строку в объект календарной даты
    date_time_obj = date_time_obj + relativedelta(months=+1, day=31) # увеличиваем на один месяц и добавляем максимальное количество дней в месяце, чтобы получить последний день месяца
    date = datetime.datetime.strftime(date_time_obj, '%d.%m.%Y') # форматируем дату обратно в строку
print(deposit)
