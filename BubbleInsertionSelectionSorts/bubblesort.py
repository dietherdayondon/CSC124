import time

def bubblesort(list):
	for i in range((len(list)-1), 0, -1):
		for j in range(i):
			if(list[j] > list[j+1]):
			    temp = list[j]
			    list[j] = list[j+1]
			    list[j+1] = temp

with open('random15000.txt', 'r') as rd:
	lineread = rd.read().split()
	inputValues = [int(item) for item in lineread]

start_time = time.time()
bubblesort(inputValues)

print("Sorting Done!!\n")
exec_time = time.time() - start_time
print("Execution Time: "+ str(format(exec_time, 'f'))+ " sec")
