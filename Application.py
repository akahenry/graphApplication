import sys

############################################## Functions ##################################################

## SPTree_organize: int -> SPTree
# Objective: given an index, this function returns the element which has this index in the SPTree (arvore).
def SPTree_organize(index):
    return arvore[index][1]

## SPTree_initialize: list -> SPTree
# Objective: given a SPTree, this function returns this tree with this tuple: (None, sys.maxsize).
def SPTree_initialize(DEV_list):
    SPTree = []	# Initializing this tree

    for router in range(len(DEV_list)):
    	SPTree += [(None, sys.maxsize)]

    return SPTree

###########################################################################################################

############################################## Application ################################################

# Reading all the elements

# Initializing matrix
DEV_matrix = []

nCampi = int(input())	# Getting number of campis

for count in range(0, nCampi):	# Reading them
	nDevices = int(input())	# Getting number of devices

	for i in range(0, nDevices):	# Reading all devices in one line
		DEV_matrix.append([int(x) for x in input().split()])

	nLimitedDevices = int(input())	# Getting number of limited devices

	listLimitedDevices = [int(x)-1 for x in input().split()]	# Reading all limited devices

# Passing all the elements read to

DEV_list = [int(x) for x in range(0, nDevices)]

protoroteadores_list = listLimitedDevices

# Removing all the routers which has issues
for router in protoroteadores_list:
	DEV_list.remove(router)

# Initializing SPTree
arvore = SPTree_initialize(DEV_list)

print(arvore)

# Setting root
root = 0

# Initialzing queue
Queue = []

# Setting the first one to begin
arvore[root] = (None, 0)

# Putting all the routers which hasn't any issues in the queue
for router in range(len(DEV_list)):
    Queue.append(DEV_list[router)

# Calculating the path without the routers which has issues
while len(Queue) > 0:
    base = Queue[0]
    del Queue[0]
    for router in range(len(DEV_matrix)):
        if router in Queue and DEV_matrix[base][DEV_list[router]] < arvore[DEV_list[router]][1]:
            arvore[DEV_list[router]] = (base, DEV[base][DEV_list[router]])
            Queue.sort(key=SPTree_organize)
    print(arvore)

# Calculating the path with the routers which has issues
for base in range(len(protoroteadores_list)):
    for router in range(len(DEV_list)):
        if DEV_matrix[protoroteadores_list[base]][DEV_list[router]] < arvore[protoroteadores_list[base]][1]:
            arvore[protoroteadores_list[base]] = (DEV_list[router], DEV_matrix[protoroteadores_list[base]][DEV_list[router]])
    print(arvore)
	
