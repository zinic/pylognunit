import unittest
import json
import os

from pylognorm import LogNormalizer, lib_version


RULES_LOCATION = 'rules'


class TestCase(unittest.TestCase):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        self.maxDiff = 4096
        self.normalizer = LogNormalizer()
        self._load_stock_rules()

    def _load_stock_rules(self):
        """
        Loads all rules db files within the default rules location. When
        run with nosetests, this should be the rules directory under the
        pylognunit project root. All rules db files must be text files that
        end with the suffix '.db'
        """
        if os.path.isdir(RULES_LOCATION):
            for possible_rule_db in os.listdir(RULES_LOCATION):
                if possible_rule_db.endswith('.db'):
                    self.normalizer.load_rules(
                        os.path.join(RULES_LOCATION, possible_rule_db))

    def load_rule(self, rule):
        """
        Loads a single rule into the normalizer context for this test
        class. This method is only available if the liblognorm library
        version is greater than or equal to 0.3.7
        """
        self.normalizer.load_rule(rule)

    def load_rules_file(self, rule_filename):
        """
        Loads a file of rules into the normalizer context for this test
        class. This method is available to all versions of liblognorm.
        """
        if not os.path.exists(rule_filename):
            raise IOError('Unable to locate rules file: {}'.format(
                os.path.join(os.getcwd(), rule_filename)))
        self.normalizer.load_rules(rule_filename)

    def normalize(self, source):
        """
        Attempts to normalize the given source string. This source may be
        a PyString, a byte array or a unicode object.
        """
        event = self.normalizer.normalize(source)
        return json.loads(event.as_json())
