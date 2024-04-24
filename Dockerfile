FROM apache/airflow:2.7.1-python3.9

COPY requirements.txt /opt/airflow/

USER root
RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

EXPOSE 5432
EXPOSE 6379
EXPOSE 8080

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt