#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os


class Config:
    def __init__(self):
        self.FORGE_API_KEY = os.environ.get('FORGE_API_KEY') or 'YOUR_API_KEY'


if __name__ == '__main__':
    config = Config()
    print("FORGE_API_KEY: {}".format(config.FORGE_API_KEY))
