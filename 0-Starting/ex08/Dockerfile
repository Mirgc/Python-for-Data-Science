FROM python:3.10 

ADD tester.py .
ADD Loading.py .
RUN pip install flake8
RUN pip install tqdm

ENTRYPOINT ["python", "./tester.py"] 