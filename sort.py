import sys as cmd
from timeit import default_timer as elapsed_t
from datetime import timedelta # to define elapsed time in seconds

def bubble_sort(num):
   n = len(num)
   for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num[j+1] : # check if the post element is smaller than the previous one 
                num[j], num[j+1] = num[j+1], num[j] # when if condition is correct switch elements positions in each other

def insertion_sort(num):
    for i in range(1,len(num)):
        for j in range(0,len(num)):
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]

def merge_sort(num):
    if len(num)>1:
        mid = len(num)//2
        left = num[:mid]
        right = num[mid:]

        merge_sort(left)
        merge_sort(right)
        i=j=k=0       
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num[k]=left[i]
                i=i+1
            else:
                num[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            num[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            num[k]=right[j]
            j=j+1
            k=k+1

stopping_point = int(cmd.argv[1]) # created argv[1] to take command from console

num = []
source_file = open("data.txt","r") # open and read data.txt for specified number of elements 
for i in range(0,stopping_point):
    num.append(int(source_file.readline()))

start_count = elapsed_t()

#---arg2---#
# to take specific command to run specific type of sorting algorithm 
if cmd.argv[2] == "MergeSort":
    merge_sort(num)
elif cmd.argv[2] == "InsertionSort":
    insertion_sort(num)
elif cmd.argv[2] == "BubbleSort":
    bubble_sort(num)

end_count = elapsed_t()
print("Elapsed Time:",timedelta(end_count - start_count)) # starts measuring beginning of operations and ends end of proceses
                                                          # take difference to procure elapsed time 
source_file.close()

sorted_file = open("sorted.txt", "w")
for i in range(len(num)):                                 # write sorted text into a new txt file
    sorted_file.write(str(num[i])+'\n')

sorted_file.close()