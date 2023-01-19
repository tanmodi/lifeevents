# lifeevents
TED like conference company website using Django framework using python 
# To run the project

1. Enter your own django secret key

    ```at /events/settings.py```
    
2. Install requirements.txt

```python
    pip install -r requirements.py
```
    
3. Make migration of database
```python
    python manage.py makemigrations
    
    python manage.py migrate
  ```

4. Run the project
```
    python manage.py runserver
```
5. Open Browser and go to 
```
    127.0.0.1:8000
```
# To see the database 

1.Create a admin account
```
    python manage.py createsuperuser
```
2. Open browser and go
```
    127.0.0.1:8000/admin
```
# To use the email service

1. Set up your email accounts details at
```
    /events/setting.py
```
2. Also enter your email at 
```
    /app/views.py
    /login/views.py
    /speakerlogin/views.py
```
# To use SMS service

    you can any SMS service provider according to your country
