import pylognunit


APACHE_LL_STR = (
    '127.0.0.1 - - [12/Jul/2013:19:31:24 +0000] "GET /test '
    'HTTP/1.1" 404 461 "-" "curl/7.29.0"'
)


class ApacheLogsTest(pylognunit.TestCase):

    def test_combined(self):
        expected = {
            'user_agent': 'curl/7.29.0',
            'url': '-',
            'bytes': '461',
            'status_code': '404',
            'http_version': 'HTTP/1.1',
            'uri': '/test',
            'method': 'GET',
            'timestamp': '12/Jul/2013:19:31:24 +0000',
            'b': '-',
            'a': '-',
            'remote_host': '127.0.0.1'
        }

        self.assertEqual(expected, self.normalize(APACHE_LL_STR))
