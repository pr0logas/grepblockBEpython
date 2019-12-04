import jenkins
from auth import username, password

server = jenkins.Jenkins('https://development.adeptio.cc', username='administrator',
password='dnVOQfYwG7GmTaTnpY27yxFzf4N/ziED')

user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

def printJobs():
    jobs = server.get_jobs()
    return jobs

def createJob(jobName, xml):
    server.create_job(jobName, xml)

def printJobXML(jobName):
    return server.get_job_config(jobName)

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

#print(printJobXML('Adeptio-daemon-parseWallets'))


createJob('testas', newXml)


