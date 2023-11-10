from teamcity.messages import TeamcityServiceMessages as _TSM


class TeamcityServiceMessages(_TSM):
    def testMetadata(self, testName, name, value='', type='', flowId=None):
        # https://www.jetbrains.com/help/teamcity/reporting-test-metadata.html#Reporting+Additional+Test+Data
        self.message('testMetadata', name=name, testName=testName, value=value, type=type, flowId=flowId)
