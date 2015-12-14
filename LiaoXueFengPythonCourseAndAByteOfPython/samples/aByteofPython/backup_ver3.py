import os
import time

# 1
source = ['./'+'testprint.py', '.'+os.sep+'mymodule.py', '.'+os.sep+'mymoduletest.py', '.'+os.sep+'__pycache__']

# 2
target_dir = '.'+os.sep

# 3
today = target_dir + time.strftime('%Y-%m-%d')
now = time.strftime('%H-%M-%S')

comment = input('Enter a comment --> ')
if len(comment)==0:
    target = today + os.sep + now + '.tar.gz'
else:
    target = today+os.sep+now+'_'+comment.replace(' ','_')+'.tar.gz'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 4
zip_command = 'tar -cvzf %s %s' % (target, ' '.join(source))

# 5
if os.system(zip_command) == 0:
    print('Successful backup to:', target)
else:
    print('Backup FAILED')
