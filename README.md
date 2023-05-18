# closest-points


## A Simple Django application with an API that receives a set of points on a grid as semicolon separated values. And then it finds the points that are closest to each other



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites
You will find hereafter what I use to develop and to run the project
* Python 3
* Django 4.2.1
* pipenv (not mandatory but highly recommended).  Instructions on how to get pipenv [here](https://pypi.org/project/pipenv/)



### Installation

Get a local copy of the project directory by cloning "closest-points" from github.

```bash
git clone https://github.com/BabGee/closest-points.git
```

cd into the folder

```bash
cd closest-points
```

I use pipenv for developing this project so I recommend you to create a virtual environment and activate it.

```bash
python3 -m pipenv shell
```

Install the requirements

```bash
python3 -m pip install -r requirements.txt
```

Then follow these steps:
1. Move to root folder 

```bash
cd django_angular
```
2. Create a `.env` file in the root folder, provide the required database information  to the `.env` file (.env.example file is provided to help set this information)

3. Create the tables with the django command 

```bash
python manage.py makemigrations
```
then migrate the changes
 
```bash
python manage.py migrate
```

Create an admin using command below and enter your preferred username, email and password.(You will use this to login django admin and create products etc)
 
```bash
python3 manage.py createsuperuser
```

4. Finally, run the django server

```bash
python manage.py runserver
```


