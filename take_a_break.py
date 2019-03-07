from webbrowser import open
import time

total_breaks = 3
num = 0
print ("This program starts in "+time.ctime())
while (num < total_breaks):
    time.sleep(10)
    open("https://www.youtube.com/watch?v=RRJGsyeuyNg&frags=pl%2Cwn")
    num += 1
