import sys
import subprocess
import os
try:
    subprocess.check_call([sys.executable,'-m','pip','install','pytube3'])
except:
    os.system('pip install pytube3')