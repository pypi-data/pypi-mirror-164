import seldom
from seldom.logging import log
from seldom import file_data


class YouTest(seldom.TestCase):

    @file_data("data.json", key="login")
    def test_login(self, _, username, password):
        """a simple test case """
        log.info(_)
        log.info(username)
        log.info(password)

