import math 
import sys
from datetime import datetime
import time

class City:
    def __init__(self,name,latitude,longitude,distance=0):         # x_val = latitude, y_val = longitude, dist = distance value
        self.name = name
        self.x_val = latitude
        self.y_val = longitude
        self.distance = distance
    
    def __str__(self):
        return self.name + "\t" + str(self.x_val) + "\t" + str(self.y_val) + "\n"

def calculate_distance(x_val1,y_val1,x_val2,y_val2):
    dist = math.sqrt((x_val2-x_val1)**2+(y_val2-y_val1)**2)
    return dist

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1   
    r = 2 * i + 2  

    if l < n and arr[largest].distance < arr[l].distance:
        largest = l
 
    if r < n and arr[largest].distance < arr[r].distance:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)
 

def heapSort(arr):
    n = len(arr)
 
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)



class_list = []

f = open("location.txt", "r", encoding="utf8")          # reading location.txt
lines = f.readlines()                                   # reading each line and putting them into a string list 

counter = 0

for line in lines:                                      # split each line from tab point 
    if (counter == int(sys.argv[1])):
        break
    l = line.split("\t")
    distance = calculate_distance(float(sys.argv[3]),float(sys.argv[4]),float(l[1]), float(l[2]))
    city = City(l[0], float(l[1]), float(l[2]), distance)
    class_list.append(city)
    counter +=1

timer_start = datetime.now()
heapSort(class_list)
timer_end = datetime.now()

w = open("150150210.txt","w")
for i in range(int(sys.argv[2])):
    w.write(str(i+1)+"."+class_list[i].__str__()+'\n')
w.write("Elapsed time for:\t"+str(len(class_list))+"\telements\t"+str(timer_end-timer_start))
w.close()
