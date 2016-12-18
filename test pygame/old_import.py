import subprocess
file = subprocess.check_output("find /media/ -maxdepth 2 -name questions.csv 2>/dev/null",shell=True).strip()
