import os
import time

# 1
source = ['./mymodule.py', './mymoduletest.py', './testprint.py', './__pycache__']

# 2
target_dir = './'

# 3
target = target_dir + time.strftime('%Y-%m-%d-%H-%M-%S') + '.tar.gz'

# 4
zip_command = 'tar -cvzf %s %s' % (target, ' '.join(source))

# 5
if os.system(zip_command) == 0:
    print('Successful backup to:', target)
else:
    print('Backup FAILED')
