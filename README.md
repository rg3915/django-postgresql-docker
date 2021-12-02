# django-postgresql-docker

Running PostgreSQL with Docker + Portainer + pgAdmin + Django local for development.

![img/docker-compose.png](img/docker-compose.png)

## This project was done with:

* [Python 3.9.8](https://www.python.org/)
* [Django 3.2.9](https://www.djangoproject.com/)
* [Bootstrap 4.0](https://getbootstrap.com/)

## How to run project?

* Clone this repository.
* Create virtualenv with Python 3.
* Active the virtualenv.
* Install dependences.
* Run the migrations.

```
git clone https://github.com/rg3915/django-postgresql-docker.git
cd django-postgresql-docker
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

# django-postgresql-docker

Rodando PostgreSQL com Docker + Portainer + pgAdmin + Django local para desenvolvimento.

## Este projeto foi feito com:

* [Python 3.9.8](https://www.python.org/)
* [Django 3.2.9](https://www.djangoproject.com/)
* [Bootstrap 4.0](https://getbootstrap.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-postgresql-docker.git
cd django-postgresql-docker
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

