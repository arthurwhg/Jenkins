#! /usr/local/bin/python3
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.utils.crumb_requester import CrumbRequester

crumb=CrumbRequester(username="arthur", password="arthur", baseurl="http://localhost:8080")
J=Jenkins("http://localhost:8080","arthur","arthur",requester=crumb)

J.build_job('Build_Server_on_AWS/master')


