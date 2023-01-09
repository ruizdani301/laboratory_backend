# indica al contenedor desde que imagen empezar
FROM python:3.10.9-alpine3.16
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apk update \
    && python3 -m pip install --upgrade pip \ 
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
   
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

copy ./ ./

EXPOSE 8000
# comando que se ejecutara al iniciar el contenedor

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# docker build -t appointment .
# -t : el nombre que se le sa al contenedor
# . : que busque Dockerfile en el directorio actual