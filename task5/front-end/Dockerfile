FROM nginx:latest

# انسخ ملفات الواجهة إلى هذا المسار داخل الصورة
COPY ./softy-pinko-front-end /var/www/html/softy-pinko-front-end

# انسخ إعدادات Nginx ليستخدم منفذ 9000 وملفاتنا كـ root
COPY ./softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# توثيق المنفذ (الـ ENTRYPOINT/CMD الافتراضي لـ nginx سيعمل تلقائياً)
EXPOSE 9000
