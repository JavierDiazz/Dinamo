FROM python:alpine3.19

ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE=1

#RUN apk update \
  # psycopg2 dependencies
  #&& apk add --virtual build-deps gcc python3-dev musl-dev \
  #&& apk add postgresql-dev \
  # Pillow dependencies
  #&& apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  #&& apk add libffi-dev py-cffi \
  # Translations dependencies
  #&& apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  #&& apk add postgresql-client

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

ENTRYPOINT ["/code/entrypoint.sh"]