#set the base image 
FROM python:3.6.9
COPY requirements.txt .
COPY . /home/coumbasy/projetfinetudes
WORKDIR /home/coumbasy/projetfinetudes

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip



# Expose ports
EXPOSE 8000
COPY . .

# default command to execute    
#CMD exec gunicorn projetfinetudes.wsgi:application --bind 0.0.0.0:8000 --workers 3 
#CMD python -m http.server 8000
#CMD [ "python3", "projetfinetudes/manage.py runserver 0.0.0.0:8000" ]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]




