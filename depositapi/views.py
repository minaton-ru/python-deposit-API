from depositapi.models import Deposit  
from depositapi.serializers import DepositSerializer  
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
import datetime
from dateutil.relativedelta import relativedelta

class DepositCalculate(generics.CreateAPIView):
    serializer_class = DepositSerializer
    def post(self, request):
        newdeposit = DepositSerializer(data=request.data)
        if newdeposit.is_valid():
            date = request.data.get('date')
            periods = int(request.data.get('periods'))
            amount = int(request.data.get('amount'))
            rate = float(request.data.get('rate'))
            deposit = {}
            for i in range(periods):
                amount = amount * (1 + rate/12/100) # к сумме вклада добавляется сумма по процентам за этот месяц
                deposit[date] = round(amount, 2) # округляем число до двух знаков после запятой
                date_time_obj = datetime.datetime.strptime(date, '%d.%m.%Y') # переводим дату-строку в объект календарной даты
                date_time_obj = date_time_obj + relativedelta(months=+1, day=31) # увеличиваем на один месяц и добавляем максимальное количество дней в месяце, чтобы получить последний день месяца
                date = datetime.datetime.strftime(date_time_obj, '%d.%m.%Y') # форматируем дату обратно в строку
            # newdeposit = Deposit(date=date, periods=periods, amount=amount, rate=rate, deposit=deposit)
            newdeposit.deposit = deposit
            newdeposit.save
            return Response(newdeposit.deposit, status=status.HTTP_201_CREATED)
        return Response(newdeposit.errors, status=status.HTTP_400_BAD_REQUEST)