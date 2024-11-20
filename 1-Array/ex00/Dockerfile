FROM python:3.10 

ADD tester.py .
ADD give_bmi.py .
RUN pip install flake8

ENTRYPOINT ["python", "./tester.py"] 