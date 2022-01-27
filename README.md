# Логика для подсчета месячного процента по депозиту  

Входные данные:  
- *date* - начальная дата для вклада, формат ДЕНЬ.МЕСЯЦ.ГОД через точку (строка)  
- *periods* - количество месяцев по вкладу (int)  
- *amount* - сумма вклада (int)  
- *rate* - процент по вкладу (float)  
  
Результат:  
Словарь { 'последняя дата месяца': сумма вклада с накопленным процентом }  
  
TODO:  
- API  
- проверка валидности входных данных  
  