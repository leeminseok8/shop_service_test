FROM python:3.8

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

COPY . .

RUN pip install pipenv
RUN pipenv install
RUN pipenv install gunicorn

# CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
