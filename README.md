# API на DRF для подсчета месячного процента по депозиту  

## Запуск проекта  
1. Скопировать файлы  
2. Создать файл .env для переменных окружения DEBUG и SECRET_KEY  
3. Запустить сервер:  
```pip install -r requirements.txt```  
```python manage.py makemigrations```  
```python manage.py migrate```  
```python manage.py runserver```   
4. Открыть `http://127.0.0.1:8000/calculate/` и создать POST-запрос в форме Django  
3. Или отправить POST-запрос на этот URL через Postman, файл коллекции `python-deposit-API.postman_collection.json`  

## Описание API  
Метод POST  
URL - `http://127.0.0.1:8000/calculate/`   

Входные данные:  
- *date* - начальная дата для вклада, формат ДЕНЬ.МЕСЯЦ.ГОД через точку (строка)  
- *periods* - количество месяцев по вкладу (int)  
- *amount* - сумма вклада (int)  
- *rate* - процент по вкладу (float)  
  
Результат:  
Создание новой записи о депозите.  
Возвращается поле deposit созданной записи: словарь { 'последняя дата месяца': сумма вклада с накопленным процентом }  
  
## TODO:  
- unit-тесты  


![Postman](https://s1.hostingkartinok.com/uploads/images/2022/02/14fbd20e7a7ee9f6cc5c69d9c856bf64.png)  
  