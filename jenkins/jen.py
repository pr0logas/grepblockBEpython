import jenkins
from methods import jenkinsJobs
from asset import assetName

server = jenkins.Jenkins('https://development.adeptio.cc', username='administrator',
password='dnVOQfYwG7GmTaTnpY27yxFzf4N/ziED')

user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

# Init Classes;
Methods = jenkinsJobs(assetName)

def printJobs():
    jobs = server.get_jobs()
    return jobs

def createJob(jobName, method, xml):
    name = jobName.capitalize()
    server.create_job(name+'-'+method, xml)

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

try:
    deleteJob(assetName+'-'+'coingecko-parseHistoricalPrice')
except:
    pass

try:
    deleteJob(assetName+'-'+'coingecko-parsePrice')
except:
    pass

try:
    deleteJob(assetName+'-'+'daemon-parseBlocks')
except:
    pass

try:
    deleteJob(assetName+'-'+'daemon-parseWallets')
except:
    pass

try:
    deleteJob(assetName+'-'+'graph-assetActiveWallets')
except:
    pass


deleteJob(assetName+'-'+'graph-assetBlockchainSize')
deleteJob(assetName+'-'+'graph-assetBlocks')
deleteJob(assetName+'-'+'graph-assetDifficulty')
deleteJob(assetName+'-'+'graph-assetTransactions')
deleteJob(assetName+'-'+'graph-marketcap')
deleteJob(assetName+'-'+'graph-price')
deleteJob(assetName+'-'+'graph-volume')

createJob(assetName, 'coingecko-parseHistoricalPrice', Methods.coingeckoParseHistoricalPrice())
createJob(assetName, 'coingecko-parsePrice', Methods.coingeckoParsePrice())
createJob(assetName, 'daemon-parseBlocks', Methods.daemonParseBlocks())
createJob(assetName, 'daemon-parseWallets', Methods.daemonParseWallets())
createJob(assetName, 'graph-assetActiveWallets', Methods.assetActiveWallets())
createJob(assetName, 'graph-assetBlockchainSize', Methods.assetBlockchainSize())
createJob(assetName, 'graph-assetBlocks', Methods.assetBlocks())
createJob(assetName, 'graph-assetDifficulty', Methods.assetDifficulty())
createJob(assetName, 'graph-assetTransactions', Methods.assetTransactions())
createJob(assetName, 'graph-marketcap', Methods.marketcap())
createJob(assetName, 'graph-price', Methods.price())
createJob(assetName, 'graph-volume', Methods.volume())