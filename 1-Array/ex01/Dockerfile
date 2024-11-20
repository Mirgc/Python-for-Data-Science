FROM python:3.10 

ADD tester.py .
ADD array2D.py .
RUN pip install flake8

ENTRYPOINT ["python", "./tester.py"] 