FROM node:18-alpine as frontend-build

RUN apk --no-cache add zip

RUN adduser --disabled-password --gecos '' builder

WORKDIR /usr/dataset_sh_server
#RUN apt-get update && apt-get install -y zip

COPY --chown=builder:builder app-ui app-ui

WORKDIR /usr/dataset_sh_server/app-ui


USER builder

RUN yarn
RUN yarn build
RUN zip frontend.zip -r build



FROM python:3

RUN adduser --disabled-password --gecos '' runner

WORKDIR /usr/dataset_sh_server

RUN mkdir -p /dataset-sh-storage/data && chown -R runner:runner /dataset-sh-storage

RUN mkdir -p /tmp
RUN touch /tmp/upload.dataset && chown runner:runner /tmp/upload.dataset

COPY --chown=runner:runner . .
COPY --chown=runner:runner --from=frontend-build /usr/dataset_sh_server/app-ui/frontend.zip /usr/dataset_sh_server/src/dataset_sh_server/assets/app-ui.frontend

USER runner

RUN pip install -e .

WORKDIR /dataset-sh-storage

ENV DATASET_APP_STORAGE_LOCATION=/dataset-sh-storage/data
ENV DATASET_SH_SERVER_CONFIG_FILE=/dataset-sh-storage/dataset-sh-server-config.json

CMD ["gunicorn"  , "-b", "0.0.0.0:8989", "dataset_sh_server.app:create_app()"]
