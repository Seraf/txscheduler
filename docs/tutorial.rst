txScheduler Tutorial
====================

Step 0: Importing stuff!
------------------------
First we'll import some modules::

    from txscheduler.tasks import ScheduledTask
    from txscheduler.manager import ScheduledTaskManager
    from txscheduler.service import ScheduledTaskService

    from dateutil.rrule import rrule, SECONDLY

Step 1: Deciding what you want to run
-------------------------------------

OK, this is the easy bit (actually, it's all pretty easy, but this is the 
*easiest*).  Pick a Python callable you want to run at some scheduled time.  
Any old callable will do.  We'll use something completely trivial::

    def example_callable():
        print 'example_callable called!'


Step 2: Sepecifying when you want to run it
-------------------------------------------
Now we need to decide when we want to run our callable.  We specify this 
using the rrule module from the dateutil package.  What we want is an 
*rrule* instance.  These can be really simple or horribly complex.  For 
now we'll pick something easy::

    rule = rrule(SECONDLY, interval=5)
    
Obviously this is pretty simple, but it's enough to give you an idea.  You 
can make these rules pretty complex, and if the basic **rrule** 
functionality isn't enough for you, you can also use a **rruleset** 
(see the 
`dateutil <http://labix.org/python-dateutil>`_
documentation).


Step 3: Set up a  :class:`ScheduledTask <txscheduler.tasks.ScheduledTask>` instance
-----------------------------------------------------------------------------------
Now we just need to glue our callable and our rrule together using a 
:class:`txscheduler.tasks.ScheduledTask` instance.  
This is easy::

    task = ScheduledTask('Example task', rule, example_callable)
    
If you like you can create a subclass of 
:class:`ScheduledTask <txscheduler.tasks.ScheduledTask>` and override the 
before_execute and after_execute methods.  These do exactly what they say, 
they run either before the task or after it.


Step 4: Set up a :class:`ScheduledTaskManger <txscheduler.manager.ScheduledTaskManger>`
---------------------------------------------------------------------------------------
Now we need to create a :class:`txscheduler.manager.ScheduledTaskManager` object, and add our 
task to it.  This class basically holds a list of tasks, and is 
responsible for running them at the right times.
::

    taskman = ScheduledTaskManager()
    taskman.add_task(task)
    
You can add more than one task of course, but we'll leave that as an 
exercise to the reader.

Step 5: Tell Twisted to run your tasks
--------------------------------------
There are two ways to do this...

Using the Twisted Application framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
use :class:`ScheduledTaskService <txscheduler.service.ScheduledTaskService>`::

    # create a scheduler service, and give it the task manager
    scheduler = ScheduledTaskService(taskman)

    # create the application and add the scheduler service
    application = service.Application("scheduler")
    scheduler.setServiceParent(application)

Using loopingCall
~~~~~~~~~~~~~~~~~
Or use 
`twisted.internet.task.loopingCall <http://twistedmatrix.com/documents/8.1.0/api/twisted.internet.task.LoopingCall.html>`_
::

    looper = loopingCall(taskman.run)
    looper.start(1)
    
This will repeatedly call ScheduledTaskManager's run() method once every 
second, unless your task takes longer than that to run.  