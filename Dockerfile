# Docker with flask and gunicorn
FROM python:alpine

# ADD links a local file or directory into a container, allowing you to modify the code on the fly, 
# without having to rebuild the image.
# In contrast to COPY, which copies the local content into the container. 
# However, you need to stop and restart the containers to see the effect of any changes
# COPY server /server
# WORKDIR /server

ADD ./server /server
WORKDIR /server

RUN pip install --upgrade pip -r requirements.txt

# Import data into redis database
# RUN python3 db.py

EXPOSE 8000

ENTRYPOINT gunicorn -w 4 -b 0.0.0.0:8000 wsgi:application
