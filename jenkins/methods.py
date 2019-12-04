class jenkinsJobs():
    def __init__(self, assetName):
        self.assetName = assetName


    def coingeckoParseHistoricalPrice(self):
        newXml = '''<?xml version='1.1' encoding='UTF-8'?>
        <project>
          <actions/>
          <description></description>
          <keepDependencies>false</keepDependencies>
          <properties/>
          <scm class="hudson.scm.NullSCM"/>
          <canRoam>true</canRoam>
          <disabled>false</disabled>
          <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
          <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
          <triggers>
            <hudson.triggers.TimerTrigger>
              <spec>*/5 * * * *</spec>
            </hudson.triggers.TimerTrigger>
          </triggers>
          <concurrentBuild>false</concurrentBuild>
          <builders>
            <hudson.tasks.Shell>
              <command>asset=''' + self.assetName + '''
        
cd ~/grepblockbepython/assets/coins/${asset}

python ./${asset}ImportHistoricalPrices.py</command>
            </hudson.tasks.Shell>
          </builders>
          <publishers/>
          <buildWrappers>
          </buildWrappers>
        </project>
        '''
        return newXml

    def daemonParseWallets(self):
        newXml = '''<?xml version='1.1' encoding='UTF-8'?>
                <project>
                  <actions/>
                  <description></description>
                  <keepDependencies>false</keepDependencies>
                  <properties/>
                  <scm class="hudson.scm.NullSCM"/>
                  <canRoam>true</canRoam>
                  <disabled>false</disabled>
                  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
                  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
                  <triggers>
                    <hudson.triggers.TimerTrigger>
                      <spec>*/30 * * * *</spec>
                    </hudson.triggers.TimerTrigger>
                  </triggers>
                  <concurrentBuild>false</concurrentBuild>
                  <builders>
                    <hudson.tasks.Shell>
                      <command>asset=''' + self.assetName + '''

        cd ~/grepblockbepython/assets/coins/${asset}

        python ./${asset}ImportWallets.py</command>
                    </hudson.tasks.Shell>
                  </builders>
                  <publishers/>
                  <buildWrappers>
                  </buildWrappers>
                </project>
                '''
        return newXml