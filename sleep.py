#!/usr/bin/env python3
# Fast hack to fix standard sleep program not working in Ubuntu 20.04 in WSL 1
import sys
import time

#print(len(sys.argv))
def sleep(secs):
    #print("Waiting: " + str(secs) + " secs...")
    time.sleep(secs)
    return

def help():
    print("Usage: sleep NUMBER[SUFFIX]")
    print("Pause for NUMBER seconds.  SUFFIX may be 's' for seconds (the)")
    print("default), 'm' for minutes, 'h' for hours or 'd' for days.")
    exit()

if len(sys.argv) > 1:
    s = sys.argv[1]
    if s == "--help":
       help()

    try:
        s = float(s)
        sleep(s)
        
    except:
        s = s.lower()
        r = s[-1]
        #print("Rightmost: " + r)
        s = s[0:-1]
        
        try:
            s = float(s)
            if r == "m":
                #print("Minutes")
                s = s * 60
            if r == "h":
                #print("Hours")
                s = s * 60 * 60
            if r == "d":
                #print("Days")
                s = s * 60 * 60 * 24
            
            sleep(s)
            
        except:
            print("Invalid input: " + str(sys.argv[1]))
            help()
else:
    print("No args!")
    help()
