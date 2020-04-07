FROM nginx:1.17.1

# 替换为国内源
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
#COPY ./compose/production/nginx/sources.list /etc/apt/
#RUN apt-get update && apt-get install -y --allow-unauthenticated certbot python-certbot-nginx


RUN rm /etc/nginx/conf.d/default.conf \
&& mkdir -p /usr/share/nginx/html/static \
&& mkdir -p /usr/share/nginx/html/media \
&& mkdir -p /usr/share/nginx/ssl

COPY ./compose/production/nginx/django_blog.conf /etc/nginx/conf.d/django_blog.conf



