#!/usr/bin/python

# quick script to run tests from source directory
# i.e. without having to install

import sys
from os.path import dirname, join as joinpath

from base_test_code import *

def main():
    dn = dirname(sys.argv[0])
    sys.path.insert(0, joinpath(dn,'..'))
    sys.path.insert(0, dn)
    import test_grabber, test_byterange, test_mirror, test_keepalive
    suite = TestSuite( (test_grabber.suite(),
                        test_byterange.suite(), 
                        test_mirror.suite(),
                        test_keepalive.suite()) )
    suite.description = 'urlgrabber tests'
    runner = TextTestRunner(stream=sys.stdout,descriptions=1,verbosity=2)
    runner.run(suite)
    
if __name__ == '__main__':
    main()
