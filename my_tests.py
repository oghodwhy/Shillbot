import unittest
import codecs
import os

from mothership.base import MothershipServer
from workers.basic_worker import BasicUserParseWorker
from tests.test_mothership_basic import TestMothershipBasic
from tests.test_worker_basic import TestWorkerBasic


if __name__ == "__main__":
    dostuff = True
    

    #start mothership and worker
    server = MothershipServer()
    server.run()
    worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")
    worker.run()

    #check basic tests still work
    test_worker_basic.test_worker_parsing()



