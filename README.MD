# Crypto Exchange Project

## Installation Instructions

First, run make the migrations and run the migrate command.

```
python3 manage.py makemigrations crypto
python3 manage.py migrate
```

Make sure to install all the dependencies from `requirements.txt`.

```pip3 install -r requirements.txt```

The project used `raabitmq-server` for storing results of asynchronous tasks at backend.

Hence, a separate setup is required fo it.

```sudo apt install rabbitmq-server```


Also, the celery `worker` needs to be run after installing `rabbitmq` as separate process.

Open up a new terminal tab and run the following command for running the background worker.

```
celery -A core worker -l INFO
``` 


Also, a separate process for triggering periodic tasks is required which is through `celery beat` command.

```
celery -A core beat -l INFO
```

Note that, for running these celery commands, `raabitmq-server` setup is required.


Hence, all steps gets boiled down to this list:

```
pip3 install -r requirements.txt
sudo apt install rabbitmq-server -y
python3 manage.py makemigrations crypto
python3 manage.py migrate
celery -A core worker -l INFO &
celery -A core worker -l INFO &
python3 manage.py runserver
```
