FROM python:3

#Install Chef Inspec
RUN curl https://omnitruck.chef.io/install.sh | bash -s -- -P inspec

