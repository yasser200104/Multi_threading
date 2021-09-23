import threading
import time


def Thread_tracker(n, thread_name):
    print(thread_name + ' started executing and will be suspended for ' + str(n) + ' seconds')
    time.sleep(n)
    print('{} resumed execution \n'.format(thread_name))


t = threading.Thread(target=Thread_tracker, name='Initial_thread', args=(3, 'Initial_thread'))

# start the first thread
t.start()


threads_list = []

# to track the time taken in the execution of the threads we used time() method
start = time.time()

for i in range(5):
    t = threading.Thread(target=Thread_tracker,
                         name='thread{}'.format(i),
                         args=(i, 'thread {}'.format(i)))
    threads_list.append(t)
    t.start()


#t.join() will block the program from executing untill the threads terminate
for t in threads_list:
    t.join()


end = time.time()

print('time taken: {}'.format(end - start))
print('All the threads have finished ')