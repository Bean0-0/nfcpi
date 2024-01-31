import threading
import subprocess
import RPi.GPIO 

def run_script(script_name):
    subprocess.run(["python3", script_name])

if __name__ == "__main__":
    script1_thread = threading.Thread(target=run_script, args=("/home/pi/nfcpi/raspberrypi/python/get_uid.py",))
    script2_thread = threading.Thread(target=run_script, args=("/home/pi/nfcpi/raspberrypi/python/allowed.py",))

    script1_thread.start()
    script2_thread.start()

    script1_thread.join()
    script2_thread.join()

    print("Both scripts have finished executing.")