import time

def selectionsort(list):
   for items in range(len(list)-1,0,-1):
       position_max=0
       for location in range(1,items+1):
           if list[location]>list[position_max]:
               position_max = location

       temp = list[items]
       list[items] = list[position_max]
       list[position_max] = temp

with open('random15000.txt', 'r') as rd:
	lineread = rd.read().split()
	inputValues = [int(item) for item in lineread]

start_time = time.time()
selectionsort(inputValues)
# print(inputValues)
print("Sorting Done!!\n")
exec_time = time.time() - start_time
print("Execution Time: "+format(exec_time, '.8f')+" sec")