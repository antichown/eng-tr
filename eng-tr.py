#!/usr/bin/python
# -*- coding: utf-8 -*-
#twitter @0x94
from threading import Event, Thread
import os,random

def randomsatir(dosya):
	fd = file(dosya,'rb')
	l = fd.readlines()
	pos = random.randint(0,len(l))
	fd.close()
	return l[pos]


class RepeatTimer(Thread):
    def __init__(self, interval, function, iterations=0, args=[], kwargs={}):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.iterations = iterations
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()
 
    def run(self):
        count = 0
        while not self.finished.is_set() and (self.iterations <= 0 or count < self.iterations):
            self.finished.wait(self.interval)
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
                count += 1
 
    def cancel(self):
        self.finished.set()


def donbabadonelim():
	satir = randomsatir("eng-tr.txt")
	satir = satir.replace("\n","")

	parcala = satir.split(" = ")

	ingilizce = parcala[0]
	turkce = parcala[1]

	komut = "notify-send '"+ingilizce+"' '"+turkce+"'"
	os.system(komut)


t = RepeatTimer(40.0, donbabadonelim)
t.start()



