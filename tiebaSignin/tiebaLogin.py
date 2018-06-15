#!/usr/bin/env python
#coding:utf8

import urllib
import urllib2
import cookielib
import json
import random
import request
import os


def login(url, header):
    cookiejar = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    urllib2.install_opener(opener)

    request = urllib2.Request(url, headers=header)
    token = urllib2.urlopen(request).read()
    print token

    #urllib2.urlopen(url, data=)


loginurl = 'https://passport.baidu.com/v2/api/?login'
tokenurl = 'https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=log'
def loginHeaders():
    login_header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/60.0}',
         #           'Referer':'https://tieba.baidu.com/f?fr=w…kw=%E8%BF%85%E9%9B%B7%E5%AE%9D'
                    'Upgrade-Insecure-Requests': 1
                    }
token_header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/60.0}',
                'Cookie': '	BAIDUID:D805692BA1AFD0EEA012DB39F9F28B02:FG=1;HOSUPPORT=1'
                }


login(tokenurl, token_header)