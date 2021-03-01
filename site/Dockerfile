FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends libxml2 libxslt1.1

RUN pip install requests markdown lxml

COPY update.py /
COPY template.html /

WORKDIR /workdir

ENTRYPOINT ["python", "/update.py"]

