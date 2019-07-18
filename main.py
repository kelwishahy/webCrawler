from webCrawler import crawler
import time

exTimes = []
avg = 0

spider_man = crawler()

start = time.time()
spider_man.webSearch(query='chest')
end = time.time()
exTimes.append(end-start)

start = time.time()
spider_man.webSearch(query='legs')
end = time.time()
exTimes.append(end-start)

start = time.time()
spider_man.webSearch(query='biceps')
end = time.time()
exTimes.append(end-start)

start = time.time()
spider_man.webSearch(query='tricep')
end = time.time()
exTimes.append(end-start)

start = time.time()
spider_man.webSearch(query='shoulders')
end = time.time()
exTimes.append(end-start)

start = time.time()
spider_man.webSearch(query='abs')
end = time.time()
exTimes.append(end-start)

start = time.time()
spider_man.webSearch(query='back')
end = time.time()
exTimes.append(end-start)

for time in exTimes:
    avg = avg + time
avg = avg/len(exTimes)

print('Average time elapsed: ' + str(avg))