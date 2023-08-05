import time
from datetime import datetime

"""
Note: The file will be written in the root directory (/) because the program
will write in the path from the perspective of systemd.
"""

while True:
    with open("~/timestamp.txt", "a") as f:
        f.write("The current timestamp is: " + str(datetime.now()))
        f.close()
    time.sleep(10)
