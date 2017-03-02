# Rest TODO List
Um projeto relativamente simples, integrando Django Rest Framework e AngularJS 1.6.

## Configuração
As seguintes váriaveis de ambiente são requeridas. Ex:

    export EMAIL_URL=console://:@localhost:1025
    export SECRET_KEY='ztibsdwjar1v1pnp-6abc@r(1@!mfklak0$abg9^l^wo!7!sf1'
    export DATABASE_URL=postgres://igor:123@localhost:5432/todo
    export ADMINS=admin,admin@domain.com

## Instalação

    pip3.6 install -r requirements.txt
    python3.6 manage.py migrate

## Tests

    invoke test
    
## Executar a aplicação

    invoke