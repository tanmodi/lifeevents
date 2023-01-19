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
# home page
![Screenshot from 2023-01-20 01-21-20](https://user-images.githubusercontent.com/54736837/213556814-b3fd7eb4-e130-41a2-b63b-aae2db7fb958.png)

# speaker page
![Screenshot from 2023-01-20 01-21-46](https://user-images.githubusercontent.com/54736837/213556087-6cef6c47-e198-43da-a2ef-37923ab7d432.png)

# search events in the city
![Screenshot from 2023-01-20 01-22-30](https://user-images.githubusercontent.com/54736837/213556852-7634889d-9c9f-4738-8759-4da04b6a3858.png)

# Blog page
![Screenshot from 2023-01-20 01-22-52](https://user-images.githubusercontent.com/54736837/213556877-83909dbb-eb2c-4aa6-84f3-68c74d2dcaa7.png)

# user login

![Screenshot from 2023-01-20 01-23-05](https://user-images.githubusercontent.com/54736837/213556909-97372e09-ded4-418c-a526-39957d3c2dff.png)
# multiple ways to login to the page
![Screenshot from 2023-01-20 01-23-13](https://user-images.githubusercontent.com/54736837/213556924-c458e85b-1f33-4fe0-a840-5a409f1f39aa.png)

# otp verification page if login through otp on email or phone
![Screenshot from 2023-01-20 01-23-27](https://user-images.githubusercontent.com/54736837/213556963-a2c8c8fb-2ff8-49ad-b276-f33bf07b3402.png)

# user home page
![Screenshot from 2023-01-20 01-24-26](https://user-images.githubusercontent.com/54736837/213556992-7fa3c479-b825-4218-b103-4e212d7cb5c3.png)

