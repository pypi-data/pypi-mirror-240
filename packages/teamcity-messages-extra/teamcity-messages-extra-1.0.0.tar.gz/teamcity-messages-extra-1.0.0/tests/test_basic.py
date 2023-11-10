from unittest import TestCase
import io
import time
from datetime import datetime

from teamcity_extra import messages


def fixed_time():
    return fixed_time._time


fixed_time._time = time.mktime(datetime(2000, 11, 2, 10, 23, 1).timetuple()) + 0.5569


class Test(TestCase):
    def test_constructor(self):
        messages.TeamcityServiceMessages()

    def test_metadata(self):
        out = io.BytesIO()
        tsm = messages.TeamcityServiceMessages(output=out, now=fixed_time)
        tsm.testMetadata('testName', 'link', value='https://github.com', type='link')
        self.assertEqual(
            out.getvalue(),
            b"##teamcity[testMetadata timestamp='2000-11-02T10:23:01.556' name='link' testName='testName' type='link' value='https://github.com']\n",
        )
