# Personal Gallery

##  Description
This is a web app that allows the user to views, copy links of different photos of different categories based on ones interest. A user is not allowed to upload, comment or like a photo but can copy the photos link description.

######  By Gabriel Gatumu


### User Stories

####  As A User I Would Like:

    View different photos that interest me.
    Click on a single photo to expand it and also view the details of the photo.
    Search for different categories of photos. (ie. Nature, Animals)
    Copy a link to the photo to share with my friends.
    View photos based on the location they were taken.

####  How To Use The App

    Visit https://github.com/GabrielSpear/PersonalGallery/tree/master
    clone the repository to your local machine
    Download and install virtual environment then activate it
    Install all requirements needed from the requirements.txt file


### Setup/Installation Requirements

    internet access

    git clone   https://github.com/GabrielSpear/PersonalGallery/tree/master

    $ cd PersonalGallery

    $ pip3 install virtualenv

    $ source virtual/bin/activate

    $ python3.6 -m pip install -r requirements.txt (install all dependencies)

    $ python3.6 manage.py runserver


##  Requirements

      Python3.6.4
      dj-database-url==0.4.2
      Django==1.11
      gunicorn==19.7.1
      Pillow==5.0.0
      psycopg2==2.7.4
      psycopg2-binary==2.7.4
      python-decouple==3.1
      pytz==2018.3
      whitenoise==3.3.1

"'Incase you have any questionor issues while using this code do not hesitate to get in touch with me via gabrieldvjspear@gmail.com'"


#### Know bugs

No known bugs

####  Technologies Used

    Python3.6
    Django.1.11
    Bootstrap
    postgress
    virtualenv

### License

MIT (c) 2018 Gabriel Gatumu









# [PGALLA](https://instagramal.herokuapp.com/)
#### Web app whereby a user views photoapp and copy links attached to each.
#### By **[Gabriel Gatumu](https://github.com/GabrielSpear/)**

## Description
This is a django web application that allows users to view images of different categories, coppy links attached to them, Search for images that interest them and view their locations.

### User Stories

####  As A User I Would Like:

      View different photos that interest me.
      Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
      Search for different categories of photos. (ie. Travel, Food)
      Copy a link to the photo to share with my friends.
      View photos based on the location they were taken.


## Set Up and Installations

### Prerequisites
1. Internet access
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo

    git clone   https://github.com/GabrielSpear/InstaGrama.git

    $ cd PGALLA

    $ pip3 install virtualenv

    $ source virtual/bin/activate

    $ python3.6 -m pip install -r requirements.txt (install all dependencies)

    $ python3.6 manage.py runserver

### Create the Database

    ```bash
    psql
    CREATE DATABASE galleria;
    ```

### .env file
Create .env file and paste paste the following filling where appropriate:
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'galleria'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```

### Run initial Migration

```bash
python3.6 manage.py makemigrations person
python3.6 manage.py migrate
```

### Run the app
```bash
python3.6 manage.py runserver
```
Open terminal on `localhost:8000`

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - JavaScript
    - Heroku
    - Postgresql

##  Requirements

      Python3.6.4
      dj-database-url==0.4.2
      Django==1.11
      gunicorn==19.7.1
      Pillow==5.0.0
      psycopg2==2.7.4
      psycopg2-binary==2.7.4
      python-decouple==3.1
      pytz==2018.3
      whitenoise==3.3.1

## Support and contact details
```
Incase you have any questions issues while using this code do not hesitate to get in touch with me via gabrieldvjspear@gmail.com
```
### License
MIT (c) **Gabriel Gatumu**
