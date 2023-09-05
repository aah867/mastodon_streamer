
import mastodon
from mastodon import Mastodon
from bs4 import BeautifulSoup
import argparse
import datetime
from threading import Timer
import os

'''Maxium waiting time for a new post before unfollowing the user'''
class Watchdog:
    def __init__(self, timeout, userHandler=None): # timeout in seconds
        self.timeout = timeout
        if userHandler != None:
            self.timer = Timer(self.timeout, userHandler)
        else:
            self.timer = Timer(self.timeout, self.handler)

    def reset(self):
        self.timer.cancel()
        self.timer = Timer(self.timeout, watchExpired)
        self.timer.start()

    def stop(self):
        self.timer.cancel()

    def handler(self):
        raise self;

def watchExpired():
    print('Watchdog expired')
    # ugly, but expected method for a child process to terminate a fork
    os._exit(1)
