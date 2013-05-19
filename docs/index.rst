.. txScheduler documentation master file, created by sphinx-quickstart on Fri Oct 24 15:27:02 2008.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

txScheduler Documentation
=======================================

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

.. toctree::
    :maxdepth: 1
   
    tutorial
    moduleref
   

Requirements
============
- `Python <http://www.python.org>`_ - The best dynamic language there is.
- `Twisted <http://www.twistedmatrix.com>`_ - An asynchronous application 
  framework for Python
- `dateutil <http://labix.org/python-dateutil>`_ - A Python module 
  offering powerful extensions to the standard **datetime** module.
   

Installing
==========
This should be as easy as:

    easy_install txScheduler
    
You have 
`setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_ 
installed, right?


Limitations
===========
- Rrules must currently be created 'manually' from within python code.  
  Future releases may have the ability to read from some kind of config 
  file (perhaps similar to the ubiquitous 'crontab').
- There is no guarantee that jobs will be run *exactly* when specified 
  in an rrule.  Jobs will be run on the next iteration of the 
  TaskManager after their next scheduled time.  By default, this will 
  usually be within a second or so of the actual scheduled time.  However, 
  be aware that if you set the interval parameter of the 
  ScheduledTaskService to a higher number, your tasks could be off by a
  significantly greater margin.
- Currently there is no way to 'make up' tasks that were not run (while 
  the server was down, for example).
   

Future Plans
============
- unit tests
- add conveniences to make creating rrules easier (e.g. something similar 
  to cron format)





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

