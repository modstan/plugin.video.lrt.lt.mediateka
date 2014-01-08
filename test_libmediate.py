#!/usr/bin/python2
# encoding: utf-8
import libmediateka as lm
from random import randint

def dump_data(x):
	for i in x:
		for j in i:
			print "%s|" % j,
		print("")

"""
print("Get main menu")
dump_data(lm.get_data('', '<li ><a href="mediateka/(.*)">(.*)</a></li>'))
print("Get 'temos' list")
dump_data(lm.get_data('temos', regexp["temos"]))
print("Get 'laidos' list")
dump_data(lm.get_data('laidos', regexp["laidos"]))
laidulist = lm.get_data('laidos', lm.regexp["laidos"])
#dump_data(laidulist)
nr = randint(0, len(laidulist))
print(nr)
#print("Laidos listas")
videolist = lm.get_data(laidulist[nr][0], lm.regexp["laidu-list"])
nr = randint(0, len(videolist))
print(nr)
print(lm.get_data(videolist[nr][0], lm.regexp["videolink"]))
"""
print(lm.get_data('irasas/16105/nostalgija._vokalinis_duetas_n._paltiniene_ir_e._ivanauskas._i_dalis_.', lm.regexp["videolink"]))

