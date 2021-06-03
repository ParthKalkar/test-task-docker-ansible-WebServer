# test-task-docker-ansible-web-server
DevOps test task to implement a simple web server for print the current Moscow time. Creating a docker image and automating the bootstrapping using Ansible

## Web Server
1. Created a webserver using : https://flask.palletsprojects.com/en/2.0.x/
2. Representational state transfer is a software architectural style which uses a subset of HTTP. It is commonly used to create interactive applications that use Web services. A Web service that follows these guidelines is called RESTful.
3. In my web server we only have one app.py file which makes this web service a REST API based application
4. Created Docker image using : https://docs.docker.com/language/python/build-images/

## Bootstrapping
1. Hosted on local machine
2. Automated this process using : https://www.ansible.com/
3. Created a ".yml" file which has the name and the actions.
4. The actions part basically includes running the command : `python -m flask run`
5. The automated version basically allows multiple hosts and can open this webservice by just writing a simple Ansible command : `ansible-"name" -i hosts -K "name_of_the_raw_file.yml"`
