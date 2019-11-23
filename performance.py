#!/usr/bin/env python

import time

setTimeCommand = int(round(time.time() * 1000))

def perfResult(start, end):
	perfResult = str(end - start)
	return (perfResult) + ' ms'