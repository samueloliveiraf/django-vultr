# django-vultr

Eu realmente estou muito feliz por conseguir fazer essa façanha em programação, algo que achava super difícil, mas consegui! Que felicidade meus amigos. Tenho um compromisso comigo mesmo de programar todos os dias, o resultado vem pode confiar!

Essa aplicação esta em um servidor linux na nuvem no site https://www.vultr.com/ , que inclusive recomendo de mais, super fácil criar um instancia lá! Coloquei uma aplicação DJANGO com POSTGRES e NGINIX + GUNICORN e claro meu grade amigo LINUX UBUNTU que foi o facilitador... Pra fechar o ano com chave de ouro.

Use o sistema o quando quiser...

https://djangoapp-estoque.online/

# Configuração do NGNIX e GUNICORN na servidor linux na nuvem...

sudo apt -y install build-essential python3-venv python3-dev libpq-dev install virtualenv
virtualenv venv

pip install django gunicorn psycopg2

sudo ufw allow 8000

./manage.py 0:8000

gunicorn --bind 0:8000 nameapp.wsgi

—-----------------------------------

sudo vim /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=root
Group=www-data

WorkingDirectory=/root/django-vultr
ExecStart=/root/django-vultr/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/root/django-vultr/django-vultr.sock app_web.wsgi:application

[Install]
WantedBy=multi-user.target

-----------------------------------

sudo systemctl enable gunicorn

sudo systemctl start gunicorn

sudo systemctl status gunicorn

vai aparecer na pasta do projeto um arquivo .sock

sudo journalctl -u gunicorn

sudo systemctl daemon-reaload
sudo systemctl status restart gunicorn

sudo apt -y install nginx

sudo vim /etc/ngnix/sites-avaible/nomedoprojeto

-----------------------------------

server {
    listen 80;
    server_name 155.138.230.147 djangoapp-estoque.online;

    location /static/ {
        root /root/django-vultr;
    }

    location /media/ {
        root /root/django-vultr;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/root/django-vultr/django-vultr.sock;
    }
}

-----------------------------------

sudo ln -s /etc/ngnix/sites-avalible/nomedoprojeto /etc/ngnix/sites-enable


sudo ngnix -t

sudo ufw delete allow 8000

sudo ufw allow ‘Ngnix Full’

sudo tail -F /var/log/ngix/error.log

namei -nom /root/meuprojeto/aquivo.sock

sudo chmod 777 /root

# Configuração do dominio + https

curl -o- https://raw.githubusercontent.com/vinyll/certbot-install/master/install.sh | bash

sudo certbot --nginx

