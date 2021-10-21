Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import datetime
>>> t = datetime.now()
>>> t
datetime.datetime(2021, 10, 19, 10, 7, 32, 16496)
>>> t.year
2021
>>> t.month
10
>>> t.day
19
>>> t.hour
10
>>> t.minute
7
>>> t.seconds
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t.seconds
AttributeError: 'datetime.datetime' object has no attribute 'seconds'
>>> t.second
32
>>> t1 = datetime.now()
>>> t1 - t
datetime.timedelta(seconds=89, microseconds=765494)
>>> 
>>> str(t.year, '/', t.month, '/', t.day)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    str(t.year, '/', t.month, '/', t.day)
TypeError: str() takes at most 3 arguments (5 given)
>>> print(t.year, '/', t.month, '/', t.day)
2021 / 10 / 19
>>> 
>>> 
>>> "19 October 2021"
'19 October 2021'
>>> t
datetime.datetime(2021, 10, 19, 10, 7, 32, 16496)
>>> f = "%d %B %Y"
>>> t.strftime(f)
'19 October 2021'
>>> 
