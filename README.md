# LittleLemon
>## **Note**
* In setting.py add **SECRET_KEY** as **'anything_between_quotes'** and save the file.
* Configure your MySQL database settings in **settings.py** and save the file.
* To run **Unit test** run **_python manage.py test_**. All test case will pass.
* **DRF API Login** can be used from the below endpoints for testing.
* **Some names may vary but everything has been implemented. Thanks**

>### **API Endpoints**

|Name|Endpoint|
|-----|-------|
|Admin|http://127.0.0.1:8000/admin/|
|Static Homepage|http://127.0.0.1:8000/restaurant/|
|Djoser User|http://127.0.0.1:8000/auth/users/|
|Djoser Token|http://127.0.0.1:8000/auth/token/login/|
|Menu Item|http://127.0.0.1:8000/restaurant/menu-items/|
|Single Menu Item|http://127.0.0.1:8000/restaurant/menu-items/1|
|Booking|http://127.0.0.1:8000/restaurant/booking/|
|DRF API Login|http://127.0.0.1:8000/api-auth/login/|
|Generate Token Without Djoser API|http://127.0.0.1:8000/restaurant/api-token-auth/|


>#### **Requirements**
1. django
2.  djangorestframework
3. mysqlclient
4. djoser
5. python-decouple
6. python version: 3.11 




