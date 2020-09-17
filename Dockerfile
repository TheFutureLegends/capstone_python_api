# Download python 3.8 and install it in Linux environment
FROM python:3.8-slim

# Show all log messages while running the app
ENV PYTHONUNBUFFERED TRUE

# Create an "app" folder and use as the Docker container 
WORKDIR /app

# Copy all the files in the current directory to the Docker container
COPY . ./

# Update package manager for Linux
RUN apt-get update

# Set up Linux environment for installing Pillow
RUN apt-get install gcc libtiff5-dev libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev \
    liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev tcl8.6-dev tk8.6-dev python-tk -y

# Set up Linux environment for installing mysqlclient
RUN apt-get install python3-dev default-libmysqlclient-dev -y

# Install all required dependencies for the app
RUN pip install -r requirements.txt

# Run data migration
RUN python3 ./blog/manage.py makemigrations \
    && python3 ./blog/manage.py migrate

# Expose port 8000 so that other applications can connect to this container
EXPOSE 8000

# Run this command when "docker run" is used to start the container
ENTRYPOINT ["python3",  "./blog/manage.py runserver 0.0.0.0:8000"]