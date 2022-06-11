# Keywordio---Library-Managment-System

Student View : all Books are shown

Admin View :
1. All books are shown with option to delete or update book.
2. Books Can be added - Add Book Function.

Admin Signup :
Admin can be register by using admin signup View.

admin Login :
admin can login by using admin login method.

## Authors

- [@vivekbhoye](https://github.com/vivekbhoye)

## Prerequisites
1. Python 3
2. python3-venv (if-needed)
 ```sudo apt-get install python3-venv```
## Installation

1. Clone git repository

```bash
  git clone https://github.com/vivekbhoye/Keywordio---Library-Managment-System
  cd Keywordio---Library-Managment-System
```

2. Create new virtual environment and activate it.
  replace path/to/directory with your path 
```bash
  python3 -m venv .venv
  source "path/to/directory/Keywordio---Library-Managment-System/.venv/bin/activate"
```
3. install all dependency using below command.

```bash
  pip install -r requirements.txt
```
4. now in project folder config/settings.py replace your MySQl database settings.
```bash
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql', 
        'NAME'    : 'mytestdb',                 # database name 
        'USER'    : 'test',                     # user name
        'PASSWORD': 'Secret_1234',              # password
        'HOST'    : 'localhost',                # host name
        'PORT'    : '3306',                     # Port no 
    }
}
```
5. now create table using following command.
```bash
  python manage.py makemigrations
  python manage.py migrate
```
6. after migrations. Run server using below command.

```bash
  python manage.py runserver
```

7. now navigate to http://127.0.0.1:8000/ 

## Third Party Packages
Django Crispy forms : for forms visual appearance and Validation.
## Screenshots

Admin Signup ( created user will have admin permissions,no duplicates email and username allowed ) 
![App Screenshot](https://github.com/vivekbhoye/Keywordio---Library-Managment-System/blob/master/Screenshots/unique_email.png?raw=True)

Admin Login Page
![App Screenshot](https://github.com/vivekbhoye/Keywordio---Library-Managment-System/blob/master/Screenshots/Admin_Login.png?raw=True)

Add Book (create entry for new Books)
![App Screenshot](https://github.com/vivekbhoye/Keywordio---Library-Managment-System/blob/master/Screenshots/Add_Book.png?raw=True)

Admin View ( retieve all books with delete and update button )
![App Screenshot](https://github.com/vivekbhoye/Keywordio---Library-Managment-System/blob/master/Screenshots/Logged_In_Admin_View.png?raw=True)

Book Update
![App Screenshot](https://github.com/vivekbhoye/Keywordio---Library-Managment-System/blob/master/Screenshots/Book_Update.png?raw=True)

Book Delete
![App Screenshot](https://github.com/vivekbhoye/Keywordio---Library-Managment-System/blob/master/Screenshots/Delete_Book.png?raw=True)

Student View ( Anonomouse user View)
![App Screenshot](https://github.com/vivekbhoye/Keywordio---Library-Managment-System/blob/master/Screenshots/Student_View.png?raw=True)
