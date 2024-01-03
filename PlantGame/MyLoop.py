import time

script_to_run = "Run.py"
loopCount = 0

while True:
    loopCount += 1
    exec(open(script_to_run).read())
    time.sleep(3)