import random
import threading
import time
start =time.time()
def showWaitTime(threadGroupName,waitTime):
  print("I am Thread - "+str(threadGroupName) +". I am sleeping for "+str(waitTime)+" seconds")
  time.sleep(waitTime)
#job_list = [random.randrange(0,7,1) for i in range(7)]
job_list = [6,3,2,7,6,1,6,7]
print(job_list)
l1,l2,l3=[],[],[]
ind=7
t1 = threading.Thread(target=showWaitTime, args=(1,job_list[ind]))
l1.append(job_list[ind])
t2 = threading.Thread(target=showWaitTime, args=(2,job_list[ind-1]))
l2.append(job_list[ind-1])
t3 = threading.Thread(target=showWaitTime, args=(3,job_list[ind-2]))
l2.append(job_list[ind-2])
t1.start()
t2.start()
t3.start()
ind = ind - 3
while ind>-1:
  if not t1.isAlive():
    t1 = threading.Thread(target=showWaitTime, args=(1,job_list[ind]))
    t1.start()
    l1.append(job_list[ind])
    ind=ind-1
  if not t2.isAlive():
    t2 = threading.Thread(target=showWaitTime, args=(2,job_list[ind]))
    t2.start()
    l2.append(job_list[ind])
    ind=ind-1
  if not t3.isAlive():
    t3 = threading.Thread(target=showWaitTime, args=(3,job_list[ind]))
    t3.start()
    l3.append(job_list[ind])
    ind=ind-1
t1.join()
t2.join()
t3.join()
end = time.time()
print("Total time:{}".format(end-start))
thread_dict = {}
thread_dict['thread-3'],thread_dict['thread-2'],thread_dict['thread-1'] = l3,l2,l1
print(thread_dict)
print("All jobs done!!")