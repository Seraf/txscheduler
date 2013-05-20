'''
'''
from datetime import datetime

from twisted.python import log

class ScheduledTaskManager(object):
    '''Manages a group of tasks.
    '''
    def __init__(self):
        self.tasks = []
        
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
        


