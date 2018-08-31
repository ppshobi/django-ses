#!/usr/bin/env python

from __future__ import absolute_import, print_function, unicode_literals

import os
import sys

import coverage
import nose


def start(argv=None):
    sys.exitfunc = lambda: sys.stderr.write("Shutting down...\n")

    if argv is None:
        # cov = coverage.Coverage()
        # cov.start()

        argv = [
            "nosetests", "--verbose", "--cover-package=django_ses",
        ]


    nose.run_exit(argv=argv, defaultTest=os.path.abspath(os.path.dirname(__file__)))


if __name__ == "__main__":
    start(sys.argv)