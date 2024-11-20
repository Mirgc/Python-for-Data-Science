FROM python:3.10 

ADD tester.py .
ADD load_image.py .
ADD landscape.jpg .
RUN pip install flake8 pillow numpy

ENTRYPOINT ["python", "./tester.py"] 