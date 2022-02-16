FROM python:3.8
ENV PYTHONUNBUFFERED=1
# Create a working directory for the django project
WORKDIR /code

# install requirements
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the project files into the working directory
COPY . /code/
