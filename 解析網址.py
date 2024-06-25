# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 21:26:26 2024

@author: User
"""
#解析網址模組 urllib.parse 套件 urlparse
from urllib.parse import urlparse
uc = urlparse('https://www.google.com/finance/markets/losers?hl=zh-TW')
uc
uc.scheme
uc.netloc
uc.params

uc1 = urlparse('https://www.google.com/finance/quote/NI225:INDEXNIKKEI?hl=zh-TW&comparison=INDEXASX%3AXJO%2CINDEXHANGSENG%3AHSI')
uc1
uc1.query.split('&') # 把這段內容以'&'切割

