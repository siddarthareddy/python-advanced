import time
import asyncio

def is_prime(x):
    return not any(x//i == x/i for i in range(x-1, 1, -1))
# Iteration #1, purely synchronous
def highest_prime_below(x):
    print('Highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('-> Highest prime below %d is %d' %(x, y))
            return y
        #time.sleep() is blocking call, thus not useful for async
        # so is socket.
        time.sleep(0.01)
    return None
def main():
    highest_prime_below(100000)
    highest_prime_below(10000)
    highest_prime_below(1000)

# purely synchronous
main()
'''
>>> main()
All functions get called one after another
Highest prime below 100000
-> Highest prime below 100000 is 99991
Highest prime below 10000
-> Highest prime below 10000 is 9973
Highest prime below 1000
-> Highest prime below 1000 is 997
'''

# Iteration #2, gradual transformation to async
def highest_prime_below(x):
    print('Highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('-> Highest prime below %d is %d' %(x, y))
            return y
        #time.sleep() is blocking call, thus not useful for async
        # so is socket.
        time.sleep(0.01)
    return None

#only change is to make main async
async def main1():
    highest_prime_below(100000)
    highest_prime_below(10000)
    highest_prime_below(1000)

# purely synchronous
main1()
'''
>>> main()
<coroutine object main at 0x106dc2440>
here call to main does run the function, just creates coroutine object
async functions are not intended to be called like that,
they either have to be awaited, or 
they have to be passed to the event loop - an async scheduler
# async functions need a "driver"
'''
loop = asyncio.get_event_loop()
loop.run_until_complete(main1())
'''
>>> loop.run_until_complete(main1())
Highest prime below 100000
-> Highest prime below 100000 is 99991
Highest prime below 10000
-> Highest prime below 10000 is 9973
Highest prime below 1000
-> Highest prime below 1000 is 997

But it Still runs sequentially, like synchronous code
because we have not mode any change to our code that allowed it to 
be asynchronous.

we can make highest_prime_below() function asynchronous
'''
loop.close()

# Iteration #3

# add async to highest_prime_below
async def highest_prime_below(x):
    print('Highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('-> Highest prime below %d is %d' %(x, y))
            return y
        #time.sleep() is blocking call, thus not useful for async
        # so is socket.
        time.sleep(0.01)
    return None

async def main2():
    highest_prime_below(100000)
    highest_prime_below(10000)
    highest_prime_below(1000)

loop = asyncio.get_event_loop()
loop.run_until_complete(main1())
'''
>>> loop.run_until_complete(main1())
__main__:2: RuntimeWarning: coroutine 'highest_prime_below' was never awaited
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
__main__:3: RuntimeWarning: coroutine 'highest_prime_below' was never awaited
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
__main__:4: RuntimeWarning: coroutine 'highest_prime_below' was never awaited
RuntimeWarning: Enable tracemalloc to get the object allocation traceback

warning saying that highest prime is async function
but have to be either called from event loop or with await
'''

#Iteration 4
async def highest_prime_below(x):
    print('Highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('-> Highest prime below %d is %d' %(x, y))
            return y
        #time.sleep() is blocking call, thus not useful for async
        # so is socket.
        time.sleep(0.01)
    return None

async def main2():
    # adding await to async function
    await highest_prime_below(100000)
    await highest_prime_below(10000)
    await highest_prime_below(1000)

loop = asyncio.get_event_loop()
loop.run_until_complete(main1())
'''
>>> loop.run_until_complete(main2())
Highest prime below 100000
-> Highest prime below 100000 is 99991
Highest prime below 10000
-> Highest prime below 10000 is 9973
Highest prime below 1000
-> Highest prime below 1000 is 997

running but still like synchronous code, because we have not given 
the program any explicit points at which it can suspend the function
and have another function take it over

so it will await till first is finished, then second, then third
this sequential calling of functions in a fixed order can be 
changed to random by using async.await(list_of_coroutines)
'''

#5 Iteration

'''
Instead of awaiting each of the functions inturn synchonously, 
we can use asyncio.wait(list of coroutines)
'''
async def highest_prime_below(x):
    print('Highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('-> Highest prime below %d is %d' %(x, y))
            return y
        time.sleep(0.01)
    return None

async def main2():
    '''
    Instead of awaiting each of the functions inturn synchonously,
    we can use asyncio.wait(list of coroutines)
    '''
    await asyncio.wait([
        highest_prime_below(100000),
        highest_prime_below(10000),
        highest_prime_below(1000)
    ])
loop = asyncio.get_event_loop()
loop.run_until_complete(main2())
'''
>>> loop.run_until_complete(main2())
Highest prime below 1000
-> Highest prime below 1000 is 997
Highest prime below 10000
-> Highest prime below 10000 is 9973
Highest prime below 100000
-> Highest prime below 100000 is 99991

Order changes for next call

>>> loop.run_until_complete(main2())
Highest prime below 100000
-> Highest prime below 100000 is 99991
Highest prime below 1000
-> Highest prime below 1000 is 997
Highest prime below 10000
-> Highest prime below 10000 is 9973

This is already slightly asynchronous,
as we have lost control over which function is called first

But still not really asyncronous, as each function scheduled
will finish before next function scheduled
only scheduling in random(asynchronous)


How to make this asynchronous?
adding somewhere in the function, a point, saying
"now I'm going to suspend"
 this can be at time.sleep() call, 
'''

#6 Iteration
async def highest_prime_below(x):
    print('Highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('-> Highest prime below %d is %d' %(x, y))
            return y
    #time.sleep(0.01)
    # this tells event loop to handover processing time to event loop
        await asyncio.sleep(0.01)
    # having await at this level again made function synchronous
    # because by the time you are reaching here, you have already
    # computed and here we are just waiting at the end
    # await asyncio.sleep(0.01)
    return None

async def main2():
    await asyncio.wait([
        highest_prime_below(100000),
        highest_prime_below(10000),
        highest_prime_below(1000)
    ])

loop = asyncio.get_event_loop()
loop.run_until_complete(main2())
'''
>>> loop.run_until_complete(main2())
Highest prime below 10000
Highest prime below 1000
Highest prime below 100000
-> Highest prime below 1000 is 997

-> Highest prime below 100000 is 99991
-> Highest prime below 10000 is 9973


'''
