FROM ubuntu:latest

# تحديث وترقية
RUN apt-get update && apt-get upgrade -y

# تثبيت بايثون وبيبت
RUN apt-get install -y python3 python3-pip

# إصلاح مشكلة EXTERNALLY-MANAGED لو ظهرت
RUN rm -f /usr/lib/python*/EXTERNALLY-MANAGED

# تثبيت Flask و CORS عبر pip3
RUN pip3 install --no-cache-dir flask flask-cors

# العمل داخل /app
WORKDIR /app

# نسخ ملف الـ API
COPY ./api.py /app/api.py

# توثيق المنفذ
EXPOSE 5252

# تشغيل التطبيق
CMD ["python3", "api.py"]
