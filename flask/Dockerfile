FROM python:3.8-alpine
WORKDIR /app
COPY ./package.txt /app/
RUN pip install -r package.txt
# RUN pip install flask && pip install flask_sqlalchemy  pymysql
COPY . .
CMD [ "python3", "app.py" ]
#CMD [ "flask", "run", "--debugger", "--reload" ]
