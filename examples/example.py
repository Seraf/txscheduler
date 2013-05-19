'''A simple example for the txscheduler module.

This script is a .tac file.  To run it, use twistd.
e.g. twistd -noy example.tac

This script creates a ScheduledTask using a trivial callable and a
dateutil recurrence rule.  It then creates ScheduledTaskManager, adds the
task to it, and passes the taskmanager instance to a ScheduledTaskService.
'''

from twisted.application import service

from txscheduler.tasks import ScheduledTask
from txscheduler.manager import ScheduledTaskManager
from txscheduler.service import ScheduledTaskService

from datetime import datetime
from dateutil.rrule import rrule, SECONDLY

# create a subclass of ScheduledTask to add some tracing

class ExampleTask(ScheduledTask):

    def before_execute(self):
        print 'current time is: %s' % datetime.now()
        print 'tasks last runtime was: %s' % task.last_runtime
        print 'tasks next runtime is: %s' % task.next_scheduled_runtime

    def after_execute(self):
        print 'current time is: %s' % datetime.now()
        print 'tasks last runtime was: %s' % task.last_runtime
        print 'tasks next runtime is: %s' % task.next_scheduled_runtime


# create a callable
# this is the actual work we need to be performed on a schedule
def example_callable():
    print 'example_callable called!'

# create a recurrence rule
# this one means 'every five seconds'
rule = rrule(SECONDLY, interval=5)

# create a task from our callable and recurrence rule
task = ExampleTask('Example task', rule, example_callable)

# create a task manager and add a task
taskman = ScheduledTaskManager()
taskman.add_task(task)

# create a scheduler service, and give it the task manager
scheduler = ScheduledTaskService(taskman)

# create the application and add the scheduler service
application = service.Application("scheduler")
scheduler.setServiceParent(application)

if __name__ == '__main__':
    usage = '''This script is a .tac file.  To run it, use twistd.
                e.g. twistd -noy example.tac'''

    print usage
