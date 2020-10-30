FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV APP_DIR=/app

COPY ./app ${APP_DIR}

RUN pip install -r ${APP_DIR}/requirements.txt