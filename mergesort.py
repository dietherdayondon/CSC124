import time

def mergeSort(list):
    print("Splitting ",list)
    if len(list)>1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",list)

inputlist = [54,26,93,17,77,31,44,55,20]
start_time = time.time()
mergeSort(inputlist)
print(inputlist)
exec_time = time.time() - start_time

print("Execution time: ", format(exec_time, ".8f")+" sec")
