# Blog Site Demo

This is my Django Blog Site Demo.

## Set Up

### Clone source code

```
$ git clone https://github.com/jiajunchang/Blog-Site
```

### Create a virtual environment

This is for windows machine since I'm working on my windows laptop.

```
$ py -m pip install virtualenvwrapper-win
$ mkvirtualenv yourNameOfEnv
$ workon yourNameOfEnv
```

### Install Django

For those who don't have Django installed.

```
$ py -m pip install Django
```

### Configure database

In the setting.py change the database configuration as your environment. 
For example, I'm using MySQL for my project.
(Require previously installed database. If not, choose one to install before setting)

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogsite',
        'USER': 'root',
        'PASSWORD': 'jiajunc',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### Database Migration

```
$ python manage.py migrate
```

### Running the application

```
$ python manage.py runserver
```
