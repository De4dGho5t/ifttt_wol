FROM tiangolo/uwsgi-nginx-flask:python3.8

ARG ARG_ULTRAHOOK_API_KEY
ARG ARG_ULTRAHOOK_SUB_DOMAIN

ENV ULTRAHOOK_API_KEY=$ARG_ULTRAHOOK_API_KEY
ENV ULTRAHOOK_SUB_DOMAIN=$ARG_ULTRAHOOK_SUB_DOMAIN
ENV APP_DIR=/app

RUN apt-get update \
    && apt-get -y install rubygems \
    && gem install ultrahook

COPY ./templates/ultrahook.conf /etc/supervisor/conf.d
COPY ./templates/ultrahook_api_key /root/.ultrahook
COPY ./app ${APP_DIR}

RUN sed -i s/ULTRAHOOK_API_KEY/${ULTRAHOOK_API_KEY}/g /root/.ultrahook \
    && sed -i s/ULTRAHOOK_SUB_DOMAIN/${ULTRAHOOK_SUB_DOMAIN}/g /etc/supervisor/conf.d/ultrahook.conf

RUN pip install -r ${APP_DIR}/requirements.txt
