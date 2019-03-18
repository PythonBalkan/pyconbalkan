# pyconbalkan [![Build Status](https://travis-ci.org/PythonBalkan/pyconbalkan.svg?branch=master)](https://travis-ci.org/PythonBalkan/pyconbalkan)

Website for PyCon Balkan

## Contributing

PyCon Balkan website is an open source project and welcomes contributions.

To get started follow the steps above.

## Custom design for PyCon Years

As this [custom loader](https://github.com/PythonBalkan/pyconbalkan/pull/145) MR introduced if you want to make a custom template changes for a conference year, please use template inheritence by adding {year}_template_name.html it will be loaded in favor of that year, and your changes will be visible.

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


## FAQ

**Q1** Git Workflow

**A1** Create new feature branch from master, work on feature, when done create pull request

**Q2** How do we call appropriate conference in our templates and views? 

**A2** We have pyconbalkan.conference.middleware.ConferenceSelectionMiddleware class and
_get_year_from_domain method to distinguish which conference is current. 

**Q3** How to enable model filtering for each conference year?

**A3** Model needs to inherit pyconbalkan.conference.models.AbstractConference

**Q4** Just pulled repository from Git, when I run server and try to open it in the browser I get 
``'NoneType' object has no attribute 'as_meta'`` error.

**A4** Just create admin user and then make one or more conference entities. Make sure you put year of the conference
as part of the URL like this: ```2018.localhost:8000```

**Q5** How to load templates depending on the conference year?

**A5** Simply name them like this ```{year}_{template_name}.html```  