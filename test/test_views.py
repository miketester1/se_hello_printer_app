import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie":"Michal_MM", "mgs":Hello World!"}', rv.data) # noqa

    def test_msg_with_outputxml(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b'<greetings><name>Michal_MM</name><msg>Hello World!</msg></greetings>', rv.data) # noqa
        # \ to lamanie linii
