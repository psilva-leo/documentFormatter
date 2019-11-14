from centos/python-36-centos7

USER root

RUN yum -y update && \
    yum -y clean all

WORKDIR /home/document_formatter
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -ms /bin/bash document_formatter
RUN chown document_formatter:document_formatter -R /home/document_formatter
RUN chmod -x /home/document_formatter/app.py

USER document_formatter

EXPOSE 8080
CMD ["uwsgi", "--ini", "uwsgi.ini"]
