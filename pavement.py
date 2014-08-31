import os
from paver.easy import *
from paver.setuputils import setup
import time

def _kill(arg1, arg2): #TODO(MridulS) add functionality to kill server by port.
    """Stops a proces that contains arg1 and is filtered by arg2
    """
    from subprocess import Popen, PIPE

    # Wait until ready
    t0 = time.time()
    # Wait no more than these many seconds
    time_out = 30
    running = True

    while running and time.time() - t0 < time_out:
        if os.name == 'nt':
            p = Popen('tasklist | find "%s"' % arg1, shell=True,
                      stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=False)
        else:
            p = Popen('ps aux | grep %s' % arg1, shell=True,
                      stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)

        lines = p.stdout.readlines()

        running = False
        for line in lines:
            #this kills python including self in windows
            if ('%s' % arg2 in line) or (os.name == 'nt' and '%s' % arg1 in line):
                running = True

                # Get pid
                fields = line.strip().split()

                info('Stopping %s (process number %s)' % (arg1, fields[1]))
                if os.name == 'nt':
                    kill = 'taskkill /F /PID "%s"' % fields[1]
                else:
                    kill = 'kill -9 %s 2> /dev/null' % fields[1]
                os.system(kill)

        # Give it a little more time. Go have some beer!!!
        time.sleep(1)
    else:
        pass

    if running:
        raise Exception('Could not stop %s: '
                        'Running processes are\n%s'
                        % (arg1, '\n'.join([l.strip() for l in lines])))

@task
def setup():
	"""
	Install dependencies
	"""
	sh('pip install -r requirements.txt')
    sh('python manage.py syncdb')

@task	
def start():
    """
    Start HealthDB at localhost
    """
    sh('python manage.py runserver')

@task
def stop():
    """
    Stop HealthDB
    """
    _kill('python', 'runserver')
