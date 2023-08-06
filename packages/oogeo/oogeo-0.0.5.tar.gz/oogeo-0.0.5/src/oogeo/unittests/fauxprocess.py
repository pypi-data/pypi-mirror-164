# coding=utf-8
""" This is a fake program used for testing the `Processor()` class's ability to launch external processes.

"""

import time

# if running from a command line, gather command line args and call process_frequency
if __name__ == '__main__':
    print('This is a test process that performs no functions. Ending in 5 seconds...')
    time.sleep(5)
