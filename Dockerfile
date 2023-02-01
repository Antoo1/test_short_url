FROM python:3.10-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
RUN touch /var/log/filebeat.log && chmod 664 /var/log/filebeat.log

COPY Pipfile.lock Pipfile ./

RUN pip install --no-cache-dir -U setuptools pip pipenv \
    && CI=1 pipenv install --dev --deploy --system \
    && pipenv --clear


COPY . .

RUN chmod +x ./entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]
