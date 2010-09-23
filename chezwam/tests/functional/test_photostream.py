from chezwam.tests import *

class TestPhotostreamController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='photostream', action='index'))
        # Test response...
