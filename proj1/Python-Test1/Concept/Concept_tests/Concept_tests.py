'''
Concept
    Used to write unit tests for functions and classes.
    There are many ways to run tests in python
        1. Unitest
        2. Nose
        3. Nose2

Module
    Unitest
        import unittest
        from unittest.mock import patch
    Nose
        from nose import with_setup
        from nose.tools import assert_raises
        import mock

Methods
    Unittest
        setUpClass, tearDownClass, setUp, tearDown, patch
    Nose
        setup_module, teardown_module, setup_class, teardown_class, setup, teardown

Notes:
        UniTest
            setUpClass: Is a class method which is run once before all test cases are run
            tearDownClass: Is a class method run once all test cases are executed
            setUp: Is run at the beginning of every test case
            tearDown: Is run at the end of every test case
            Patch: Is used to mock api response in your test cases

            python -m unittest

        Nose
            setup_module, teardown_module -- Used to run before/after all tests are run in a module
            @with_setup(setup_func(), teardown_func()) - run/teardown set up for each test
            setup_class, teardown_class -- Run before/after all tests are run in a class
            setup, teardown -- run/teardown set up for each test

            nosetests           -- Run al tests
            nosetests -s        -- Run all tests with stdout
            nostests -w         -- specify workind dir
            nosetests -v        -- Info and debugging output
            nosetests -w simple tests/test_stuff.py:test_b  -- Run test test_b inside test_stuff.py

References
    https://realpython.com/testing-third-party-apis-with-mocks/#your-first-mock
    https://pythontesting.net/framework/nose/nose-introduction/

'''