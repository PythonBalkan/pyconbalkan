#!/bin/bash

function django_secret() { python -c "import random,string;print('SECRET_KEY='+''.join([random.SystemRandom().choice(\"{}{}{}\".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(63)]).replace('\\'','\\'\"\\'\"\\''))"; }
echo "DEBUG=True" > .env
django_secret >> .env

