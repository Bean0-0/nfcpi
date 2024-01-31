import subprocess

output = subprocess.check_output(["python3", "/home/pi/nfcpi/raspberrypi/python/get_uid.py"])  # Assuming Python 3
print(output)
