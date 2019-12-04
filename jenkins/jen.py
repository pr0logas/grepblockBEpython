import jenkins
from auth import username, passwordk

server = jenkins.Jenkins('https://development.adeptio.cc', username='administrator',
password='dnVOQfYwG7GmTaTnpY27yxFzf4N/ziED')

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

def buildJob(jobName):
    server.build_job(jobName)

def disableJob(jobName):
    server.disable_job(jobName)

def copyJob(jobName1, jobName2):
    server.copy_job(jobName1, jobName2)

def enableJob(jobName):
    server.enable_job(jobName)

def reconfigJob(jobName):
    server.reconfig_job(jobName, jenkins.RECONFIG_XML)

def deleteJob(jobName):
    server.delete_job(jobName)

def showViewJobs(viewName):
    return server.get_jobs(view_name=viewName)

createJob(api-test)
# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
build_info = server.get_build_info('api-test', last_build_number)
print build_info

