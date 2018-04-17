FROM centos:7.3.1611
RUN yum -y install epel-release && yum clean all
RUN yum -y install python-pip && yum clean all
RUN pip install pip --upgrade

COPY requirements.txt /
COPY flask-app/ /flask-app/
RUN pip install -r requirements.txt
EXPOSE 5000
WORKDIR /flask-app/
CMD ["python", "app.py"]