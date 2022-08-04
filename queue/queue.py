

# basic queue implementation with standard Python list

queue = list()

# add things to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)

queue.pop(0)

print(queue)

queue.pop(0)

print(queue)

queue.append(1)
queue.append(2)

print(queue)