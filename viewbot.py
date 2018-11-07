import requests
import time


def viewdeeznuts():
    print
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------")
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " viewbot")
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " v.1.0.0")
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " @edzart + @washedgram")
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " --------------------------------------------\n")
    listingURL = raw_input("[" + (time.strftime("%H:%M:%S")) + "]" + " Link : ")
    print
    viewCount = int(raw_input("[" + (time.strftime("%H:%M:%S")) + "]" + " How many views? : "))
    print
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Watching ... ")
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Do not close this window. ")

    print
    start_time = time.time()
    for i in range(viewCount):
        r = requests.get(listingURL)
    
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " Task completed! ")
    viewTime = float(time.time() - start_time)
    print("[" + (time.strftime("%H:%M:%S")) + "]" + " Total time : " + " %s sec" % viewTime)
    viewRate = float(viewCount / viewTime)
    print ("[" + (time.strftime("%H:%M:%S")) + "]" + " View rate  : " +  " %s views/sec" % viewRate)
    print
    print


if __name__ == '__main__':
  viewdeeznuts()

