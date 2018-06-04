FROM python:3.6

WORKDIR /app
COPY . /app


RUN apt-get -y update
RUN apt-get -y install --no-install-recommends libgeos-3.5.1 libgeos++-dev libgeos-dev graphviz binutils libproj-dev gdal-bin
RUN pip install -r /app/requirements.txt

RUN printf """SECRET_KEY=$(./generate-django.sh)')\n\
DEBUG=True""" > /app/.env


CMD python manage.py runserver