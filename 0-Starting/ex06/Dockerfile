FROM python:3.10 

ADD filterstring.py .
ADD ft_filter.py .
RUN pip install flake8

ENTRYPOINT ["python", "./filterstring.py"] 