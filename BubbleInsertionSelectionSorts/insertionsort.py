import time

def insertionsort(list):
	i = 1
	while (i < len(list)):
	    currentElement = list[i]
	    j = i
	    i = i + 1
	    while ((j>0) and (list[j-1]>currentElement)):
	        list[j] = list[j-1]
	        j = j-1
	    
	    list[j] = currentElement

	# for items in range(0,len(list)):
	#     print(list[items])

with open('random15000.txt', 'r') as rd:
	lineread = rd.read().split()
	inputValues = [int(item) for item in lineread]

start_time = time.time()
insertionsort(inputValues)
print(inputValues)
# print("Sorting Done!!\n")
exec_time = time.time() - start_time
print("Execution Time: "+format(exec_time,'.8f')+" sec")