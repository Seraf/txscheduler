from datetime import datetime
from twisted.python import log
from pymongo import MongoClient
from tasks import ScheduledTask
from dateutil.rrule import *
from twisted.python.reflect import namedAny


class TraceTask(ScheduledTask):

    def before_execute(self):
        print 'current time is: %s' % datetime.now()
        print 'tasks last runtime was: %s' % self.last_runtime
        print 'tasks next runtime is: %s' % self.next_scheduled_runtime

    def after_execute(self):
        print 'current time is: %s' % datetime.now()
        print 'tasks last runtime was: %s' % self.last_runtime
        print 'tasks next runtime is: %s' % self.next_scheduled_runtime

class ScheduledTaskManager(object):
    '''Manages a group of tasks.
    '''
    def __init__(self, configuration):
        mongo = MongoClient(configuration['database']['server'], configuration['database']['port'])
        self.database = mongo.jarvis
        self.build_default_cron()
        self.tasks = []
        for cron in self.database.crons.find( { "enabled": 1 } ):
            rule = rrule(**cron['rule'])
            object = namedAny(cron['module'] + '.' + cron['class'])()
            func = namedAny(cron['module'] + '.' + cron['class'] + '.' + cron['method'])
            if cron['args']:
                if cron['debug'] == True:
                    self.tasks.append(TraceTask(cron['name'], rule, func, object, cron['args']))
                else:
                    self.tasks.append(ScheduledTask(cron['name'], rule, func, object, cron['args']))
            else:
                if cron['debug'] == True:
                    self.tasks.append(TraceTask(cron['name'], rule, func, object))
                else:
                    self.tasks.append(ScheduledTask(cron['name'], rule, func, object))

    def build_default_cron(self):
        key_defaultcron =     {   "name": "DefaultCron" }
        data_defaultcron =    {
            "name": "DefaultCron",                  \
            "debug": 1,                             \
            "rule": {
                      "interval": 5,                \
                      "freq": SECONDLY              \
            },
            "module": 'programmetv',
            "class": 'ProgrammeTV',
            "method": 'downloadProgrammeTV',
            "args": '',
            "enabled": 1,
        }
        self.database.crons.update(key_defaultcron, data_defaultcron, upsert=True)

    def add_task(self, task):
        '''Adds a task to be run.
        
        Expects a :class:`txscheduler.tasks.ScheduledTask` instance.
        '''
        self.tasks.append(task)
        
    def remove_task(self, task):
        '''Removes a task to be run.
        
        Expects a :class:`txscheduler.tasks.ScheduledTask` instance.
        '''
        self.tasks.remove(task)
        
    def run(self):
        '''Checks for tasks which need to be run and runs them.
        '''
        log.msg('ScheduledTaskManager: checking for tasks to run...')
        tasks_to_run = [task for task in self.tasks if
                            task.next_scheduled_runtime < datetime.now()]
        log.msg('Scheduledtaskmanager: %d tasks found.' % len(tasks_to_run) )
        for task in tasks_to_run:
            task.run()
