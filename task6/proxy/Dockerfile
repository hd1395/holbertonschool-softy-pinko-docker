FROM nginx:latest

# انسخ ملف إعدادات البروكسي إلى موقع Nginx الافتراضي
COPY ./proxy.conf /etc/nginx/conf.d/default.conf

# المنفذ الذي سيستمع عليه البروكسي
EXPOSE 80
