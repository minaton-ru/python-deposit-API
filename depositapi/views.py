from depositapi.serializers import DepositSerializer  
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
import datetime
from dateutil.relativedelta import relativedelta

class DepositCalculate(generics.CreateAPIView):
    serializer_class = DepositSerializer
    def post(self, request):
        error_message = { 'error': 'Описание ошибки'}
        date = request.data.get('date')
        date = request.data.get('date')
        periods = int(request.data.get('periods'))
        amount = int(request.data.get('amount'))
        rate = float(request.data.get('rate'))
        deposit = {}
        try: # проверяем что дата введена в нужном формате
            date_time_obj = datetime.datetime.strptime(date, '%d.%m.%Y') # переводим дату-строку в объект календарной даты
        except ValueError:
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        else:
            if 1<=periods<=60 and 10000<=amount<=3000000 and 1<=rate<=8: # валидация входных данных
                newdeposit = DepositSerializer(data=request.data)
                for i in range(periods):
                    amount = amount * (1 + rate/12/100) # к сумме вклада добавляется сумма по процентам за этот месяц
                    deposit[date] = round(amount, 2) # округляем число до двух знаков после запятой  
                    date_time_obj = date_time_obj + relativedelta(months=+1, day=31) # увеличиваем на один месяц и добавляем максимальное количество дней в месяце, чтобы получить последний день месяца
                    date = datetime.datetime.strftime(date_time_obj, '%d.%m.%Y') # форматируем дату обратно в строку
                # newdeposit = Deposit(date=date, periods=periods, amount=amount, rate=rate, deposit=deposit)
                newdeposit.deposit = deposit
                newdeposit.save
                return Response(newdeposit.deposit, status=status.HTTP_200_OK)
            else:
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)