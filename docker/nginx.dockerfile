FROM nginx:1.18.0
MAINTAINER Samuel Fernandes

COPY . .

RUN rm /etc/nginx/conf.d/default.conf
COPY /docker/config/default.conf /etc/nginx/conf.d/
COPY /docker/config/fullchain.pem /
COPY /docker/config/privkey.pem /

EXPOSE 80 443

ENTRYPOINT ["nginx"]

CMD ["-g", "daemon off;"]
