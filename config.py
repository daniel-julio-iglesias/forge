#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os


class Config:
    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY') or 'YOUR_API_KEY'


if __name__ == '__main__':
    config = Config()
    print("SECRET_KEY: {}".format(config.SECRET_KEY))
