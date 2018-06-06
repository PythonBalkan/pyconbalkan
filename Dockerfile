FROM python:3.6

WORKDIR /app
COPY . /app


RUN apt-get -y update
RUN apt-get -y install --no-install-recommends binutils
RUN pip install -r /app/requirements.txt

RUN ./generate-django.sh


CMD ./run_migrate.sh