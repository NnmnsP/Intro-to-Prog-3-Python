import time
import threading
import requests

def search(qry):
    res = requests.get(f"https://www.google.com/search?q={qry}")
    print(f"Status code: {res.status_code} for {qry}")
    # save to file
    with open(f"results-{qry}.html", "a") as f:
        f.write(res.text)

# make web request
def searchAll(queries):
    threads = []
    for qry in queries:
        t = threading.Thread(target=search, args=(qry,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()


def demoOne():
    while True:
        print("*******************************!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(0.1)

def demoTwo():
    while True:
        print("Hello!")
        time.sleep(0.1)


# t2 = threading.Thread(target=demoTwo, args=())
# t2.start()
#
# t1 = threading.Thread(target=demoOne, args=())
# t1.start()

queries = ['test', 'rest', 'best', 'west', 'rat', 'bat', 'cat', 'mat']

# measure time
start = time.time()
searchAll(queries)
end = time.time()
diff = end - start
print(f"Time taken: {diff} seconds")