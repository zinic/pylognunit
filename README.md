# pylognunit
### The pylognorm rule testing framework

This project is a very simple wrapper to make testing liblognorm rules
easier.

This project expects the user to have a basic knowledge of unittest and
nosetests.

## Setting up pylognunit

```bash
pip install -r tools/pip-requires
pip install -r tools/test-requires
```

## Writing a Rule

Writing a test first requires the user to first add the rule they wish to
test under the [rules directory](https://github.com/zinic/pylognunit/tree/master/rules).
Rules must follow the
[liblognorm log samples syntax](http://www.liblognorm.com/files/manual/sampledatabase.htm).

A rule may be added to an existing rules file or it may be added in a rules
file all its own. The testing framework will attempt to load both.

## Writing a Test

After the rule is written, a [unit test](https://github.com/zinic/pylognunit/blob/master/tests/unit_test.py)
for it may be created. This unit test may be added to an existing suite of
unit tests or it may be added to a unit test module all its own. It is
important to note that the TestCase class is loaded from the pylognunit
module instead of the unittest module.

## Running Tests

```bash
nosetests
```

##That Legal Thing...

This software library is released to you under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).
See [LICENSE](https://github.com/zinic/pylognunit/blob/master/LICENSE) for
more information.