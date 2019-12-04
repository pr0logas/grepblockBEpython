class jenkinsJobs():
    def __init__(self, assetName):
        self.assetName = assetName


    def coingeckoParseHistoricalPrice(self):
        newXml = '''<?xml version='1.1' encoding='UTF-8'?>
        <project>
          <actions/>
          <description></description>
          <keepDependencies>false</keepDependencies>
          <properties>
            <jenkins.model.BuildDiscarderProperty>
              <strategy class="hudson.tasks.LogRotator">
                <daysToKeep>90</daysToKeep>
                <numToKeep>-1</numToKeep>
                <artifactDaysToKeep>-1</artifactDaysToKeep>
                <artifactNumToKeep>-1</artifactNumToKeep>
              </strategy>
            </jenkins.model.BuildDiscarderProperty>
          </properties>
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

    def assetActiveWallets(self):
        newXml = '''<?xml version='1.1' encoding='UTF-8'?>
            <project>
              <actions/>
              <description></description>
              <keepDependencies>false</keepDependencies>
              <properties>
                <jenkins.model.BuildDiscarderProperty>
                  <strategy class="hudson.tasks.LogRotator">
                    <daysToKeep>90</daysToKeep>
                    <numToKeep>-1</numToKeep>
                    <artifactDaysToKeep>-1</artifactDaysToKeep>
                    <artifactNumToKeep>-1</artifactNumToKeep>
                  </strategy>
                </jenkins.model.BuildDiscarderProperty>
              </properties>
              <scm class="hudson.scm.NullSCM"/>
              <canRoam>true</canRoam>
              <disabled>false</disabled>
              <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
              <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
              <triggers>
                <hudson.triggers.TimerTrigger>
                  <spec>5 5 * * *</spec>
                </hudson.triggers.TimerTrigger>
              </triggers>
              <concurrentBuild>false</concurrentBuild>
              <builders>
                <hudson.tasks.Shell>
                  <command>asset=''' + self.assetName + '''

cd ~/grepblockbepython/assets/coins/${asset}

python ./${asset}CreateGraphActiveWallets.py </command>
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
          <properties>
            <jenkins.model.BuildDiscarderProperty>
              <strategy class="hudson.tasks.LogRotator">
                <daysToKeep>90</daysToKeep>
                <numToKeep>-1</numToKeep>
                <artifactDaysToKeep>-1</artifactDaysToKeep>
                <artifactNumToKeep>-1</artifactNumToKeep>
              </strategy>
            </jenkins.model.BuildDiscarderProperty>
          </properties>
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


    def coingeckoParsePrice(self):
        newXml = '''<?xml version='1.1' encoding='UTF-8'?>
        <project>
          <actions/>
          <description></description>
          <keepDependencies>false</keepDependencies>
          <properties>
            <jenkins.model.BuildDiscarderProperty>
              <strategy class="hudson.tasks.LogRotator">
                <daysToKeep>90</daysToKeep>
                <numToKeep>-1</numToKeep>
                <artifactDaysToKeep>-1</artifactDaysToKeep>
                <artifactNumToKeep>-1</artifactNumToKeep>
              </strategy>
            </jenkins.model.BuildDiscarderProperty>
          </properties>
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

python ./${asset}ImportPrices.py</command>
                    </hudson.tasks.Shell>
                  </builders>
                  <publishers/>
                  <buildWrappers>
                  </buildWrappers>
                </project>
                '''
        return newXml

    def daemonParseBlocks(self):
        newXml = '''<?xml version='1.1' encoding='UTF-8'?>
        <project>
          <actions/>
          <description></description>
          <keepDependencies>false</keepDependencies>
          <properties>
            <jenkins.model.BuildDiscarderProperty>
              <strategy class="hudson.tasks.LogRotator">
                <daysToKeep>90</daysToKeep>
                <numToKeep>-1</numToKeep>
                <artifactDaysToKeep>-1</artifactDaysToKeep>
                <artifactNumToKeep>-1</artifactNumToKeep>
              </strategy>
            </jenkins.model.BuildDiscarderProperty>
          </properties>
          <scm class="hudson.scm.NullSCM"/>
          <canRoam>true</canRoam>
          <disabled>false</disabled>
          <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
          <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
          <triggers>
            <hudson.triggers.TimerTrigger>
                      <spec>* * * * *</spec>
                    </hudson.triggers.TimerTrigger>
                  </triggers>
                  <concurrentBuild>false</concurrentBuild>
                  <builders>
                    <hudson.tasks.Shell>
                      <command>asset=''' + self.assetName + '''

cd ~/grepblockbepython/assets/coins/${asset}

python ./${asset}ImportBlocks.py</command>
                    </hudson.tasks.Shell>
                  </builders>
                  <publishers/>
                  <buildWrappers>
                  </buildWrappers>
                </project>
                '''
        return newXml