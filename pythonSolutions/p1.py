import time

def multiples_sum():
    multi=[]
    for i in range(1000):
        multi.append(i) if i%3 == 0 or i%5 == 0 else +1
    return sum(multi)

if __name__ == '__main__':
    start_time = time.time()
    time.sleep(5)
    print(multiples_sum())
    print("--- %s seconds ---" % (time.time() - start_time))

"""
multiples_sum:
--- 5.004144668579102 seconds ---
"""


""" def compute():
    ans = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return str(ans)


if __name__ == "__main__":
    start_time = time.time()
    time.sleep(5)
    print(compute())
    print("--- %s seconds ---" % (time.time() - start_time)) """

"""
Compute:
--- 5.007751941680908 seconds ---
"""
