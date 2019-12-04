import jenkins
from auth import *

server = jenkins.Jenkins('https://development.adeptio.cc', username='administrator', password='dnVOQfYwG7GmTaTnpY27yxFzf4N/ziED')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

def printJobs():
    jobs = server.get_jobs()
    return jobs

def createJob(jobName):
    server.create_job(jobName, jenkins.EMPTY_CONFIG_XML)

def printJobXML(jobName):
    my_job = server.get_job_config(jobName)
    return my_job

server.build_job('empty')
server.disable_job('empty')
server.copy_job('empty', 'empty_copy')
server.enable_job('empty_copy')
server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)

#server.delete_job('empty')
#server.delete_job('empty_copy')

# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
build_info = server.get_build_info('api-test', last_build_number)
print build_info

# get all jobs from the specific view
jobs = server.get_jobs(view_name='View Name')
print jobs
