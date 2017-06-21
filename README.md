# Eventex

Sistema de Eventos proposto pelo Welcome Django

[![Build Status](https://travis-ci.org/VicenteOluz/wttd.svg?branch=master)](https://travis-ci.org/VicenteOluz/wttd)
[![Code Health](https://landscape.io/github/VicenteOluz/wttd/master/landscape.svg?style=flat)](https://landscape.io/github/VicenteOluz/wttd/master)

## como desevolver?

1. Clone o repositorio.
2. Crie um virtualenv com python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:vicenteoluz/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## como fazeer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force

```