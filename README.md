# pyconbalkan [![Build Status](https://travis-ci.org/PythonBalkan/pyconbalkan.svg?branch=master)](https://travis-ci.org/PythonBalkan/pyconbalkan)

Website for PyCon Balkan

## Contributing

PyCon Balkan website is an open source project and welcomes contributions.

To get started follow the steps above.

## Get up and running

1. Clone this repo
2. Create a virtual environment:

```
cd pyconbalkan
python -m venv .venv
```

3. Activate the virtual environment:

```
source .venv/bin/activate
```

4. Install the requirements:

```
pip install -r requirements.txt
```

5. Create a file named `.env`

Inside add:
```
SECRET_KEY={create_and_add_your_own_SECRET_KEY_here_with_no_spaces}
DEBUG=True
```

NOTE:

For more information on how you can generate a secret key visit [here](https://foxrow.com/generating-django-secret-keys) or you can generate a key online at [here](https://www.miniwebtool.com/django-secret-key-generator/).

6. Run migrations:

```
python manage.py migrate
```

7. Run collect static:

```
python manage.py collectstatic
```

8. Get the server up and running:

```
python manage.py runserver
```

You did it! If you have any problems doing this let us know by submitting an [issue](https://github.com/PythonBalkan/pyconbalkan/issues).


## Public Trello Board
To contribute to the project, please visit our newest trello board [here](https://trello.com/b/mQGuXopj/pycon-balkan-2019)


## Deprecated 
Old deprecated public board can be found [here](https://trello.com/b/J6NhX1GZ/pycon-balkan-2018).
