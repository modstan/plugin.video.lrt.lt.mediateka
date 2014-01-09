#!/usr/bin/python2
# encoding: utf-8
import libmediateka as lm
from random import randint

def dump_data(x):
	for i in x:
		for j in i:
			print "%s|" % j,
		print("")

print("===============Get main menu=======================")
dump_data(lm.get_data('', lm.regexp["pagrindinis"]))
print("===============Get 'temos' list====================")
dump_data(lm.get_data('temos', lm.regexp["temos"]))

print("===============Get 'laidos' list===================")
laidulist = lm.get_data('laidos', lm.regexp["laidos"])
dump_data(laidulist)
nr = randint(0, len(laidulist))
print("===============Laidos '%s' irasu listas=============" % laidulist[nr][1])
videolist = lm.get_data(laidulist[nr][0], lm.regexp["laidu-list"])
dump_data(videolist)
print("===============Iraso linkas=========================")
nr = randint(0, len(videolist) - 1)
print(lm.get_data(videolist[nr][0], lm.regexp["videolink"]))
print("===============Abecele==============================")
abc = lm.get_data('laidos', lm.regexp["abecele"]) 
dump_data(abc)
nr = randint(0, len(abc) - 1)
print("===============Laidos is %s raides==================" % abc[nr][1])
dump_data(lm.get_data(abc[nr][0], lm.regexp["laidos"]))
print("===============Tiesiogiai===========================")
tiesiogiai = lm.get_data("tiesiogiai", lm.regexp["tiesiogiai"])
dump_data(tiesiogiai)
nr=randint(0, len(tiesiogiai) - 1)
print("===============Tiesiogiai %s linkas=================" % tiesiogiai[nr][1])
print(lm.get_data(tiesiogiai[nr][0], lm.regexp["videolink"]))
