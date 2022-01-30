from django.urls import path
from depositapi.views import DepositCalculate

app_name = 'depositapi'  
urlpatterns = [  
    path('calculate/', DepositCalculate.as_view(), name='deposit-calculate'),   
]