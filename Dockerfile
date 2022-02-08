FROM python:3.8.9-slim
# basis for our python env and its a debian OS
RUN apt update && apt install libpq-dev  gcc -y
WORKDIR /app
#sets where application will run
COPY . ./ 
#copy contents of application
RUN pip install -r requirements.txt
#dependencies of application

ENV APP_VERSION=""

EXPOSE 5000

# Make the gunicorn command script executable by the user/owner.
RUN chmod +x gunicorn_starter.sh

#runs the application
ENTRYPOINT ["./gunicorn_starter.sh"]

#dockerfile is a recipe for docker build.