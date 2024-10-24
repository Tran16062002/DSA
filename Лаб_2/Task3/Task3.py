# Bubble sort in Python
#function
from time import perf_counter
def bubbleSort(array):
    if len(array)<=1:
        return 0
    
    num = 0
    
    for i in range(len(array)):
        
        for j in range(0, len(array) - i - 1):
            
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                num = num+1
    return str(num)

#result
t1_start = perf_counter()
with open('D:\\Lab CTDL  - GT\\Чан Тхи Лиен_Лаб0 - Copy\\Лаб_2\\Task3\\input.txt','r') as infile:
    n = int(infile.readline())
    data = str(infile.readline())
    
data = data.split(' ')
arr = [int(i) for i in data]

    
with open('D:\\Lab CTDL  - GT\\Чан Тхи Лиен_Лаб0 - Copy\\Лаб_2\\Task3\\output.txt', 'w') as outfile:
    outfile.write(bubbleSort(arr))
t1_stop = perf_counter()
print('Время работы: %s секунд '% (t1_stop - t1_start))