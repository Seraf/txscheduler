  -*- restructuredtext -*-

txScheduler readme file
=======================

txScheduler is a python package that adds the ability to run 
"scheduled tasks" to `Twisted <http://www.twistedmatrix.com>`_ 
applications.

While Twisted offers facilities to call a Python callable after a 
specified time interval (i.e. call this function in 5 seconds), it does not
offer any way to make a call at a specified time (call this function at 
5:00pm every weekday).  This functionality is often desired (or required) 
in long-running processes like most Twisted daemons.

txScheduler offers just this functionality, allowing scheduling of Python 
tasks from within a Twisted app according to arbitrarily complex rules 
specified by the developer.