import os
import sys
import time
import subprocess
from subprocess import PIPE

def run(command):
    process = subprocess.Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def main():
    print("Running")
    output, error = run("python -u \"c:/Users/Leonardo Oliveira/Documents/Python/main.py\"")
    print(output)
    print(error)
    print("Done")
    time.sleep(1)
    print("Running")
    output, error = run("python -u \"c:/Users/Leonardo Oliveira/Documents/Python/main.py\"")
    print(output)
    print(error)
    print("Done")

if __name__ == "__main__":
    main()

    
