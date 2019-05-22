#!/usr/bin/env python
# -*- coding: utf-8 -*-


from googlesearch import search

query = input('请输入要查询的内容:')

for j in search(query,tld="co.in",num=10,stop=1,pause=2):
	print(j)