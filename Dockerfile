FROM python:3.12.4
WORKDIR /django_BrainBlasters
RUN apt-get update
RUN apt install sqlite3
COPY requirements.txt .
RUN pip install -r requirements.txt
#RUN pip install pillow
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python", "django_BrainBlasters/manage.py", "runserver", "0.0.0.0:8000"]