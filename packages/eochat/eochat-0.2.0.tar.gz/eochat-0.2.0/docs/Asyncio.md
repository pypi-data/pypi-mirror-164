# Asyncio
Asyncio is a library to write concurrent code using the ```async/await``` syntax. Not to be confused with parallelism: your program will still be sequential because of CPython's Global Interpreter Lock (GIL). However, it will run multiple tasks in overlapping periods of time.

## Coroutines
These can be declared with the ```async/await``` syntax. Waiting for a coroutine to finish can be done with the ```await``` syntax only inside another coroutine. Calling a coroutine as if it were a normal function won't make it run.
```
    import asyncio
    async def my_sum(a,b):
        return a+b
        
    async def main():
        #await is inside a coroutine, and it will wait for my_sum(4,5) to finish.
        result = await my_sum(4,5) 
        print(result) #result will be 9
        
    await main() #This will raise an error: 'await' outside async function
```

Calling an async function inside a non async function is done with ```asyncio.run(main())``` instead of ```await main()``` in the example above. ```asyncio.run(function())``` will wait for the async function to finish.

## Tasks

If you don't want the program to wait for the async function to finish, you can create a task.with ```asyncio.get_event_loop().create_task(function())```. If the tasks run forever and you want the program to run forever too, then ```asyncio.get_event_loop().run_forever()``` is used. For instance, in OP's code:

```
#Creates task for async function amain
#amain calls functions to receive and send packets which run forever
asyncio.get_event_loop().create_task(amain(user, password))

#Therefore, program needs to run forever too. Otherwise it will end abruptly.
asyncio.get_event_loop().run_forever()
```


## Sleeping
From https://docs.python.org/3/library/asyncio-dev.html#concurrency-and-multithreading: 
>While a Task is running in the event loop, no other Tasks can run in the same thread. When a Task executes an await expression, the running Task gets suspended, and the event loop executes the next Task.

Adding ```await asyncio.sleep(x)``` inside each async function will make the current task wait for ```x``` seconds and  allow for the next task to be executed in case there are many tasks.

```
  #Both functions will be executed concurrently and print busy wait 1 and busy wait 2
  async def busy_wait_1():
    while True:
        print("busy wait 1")
        await asyncio.sleep(1) #Sleeps for 1 second, it can be less
        
  async def busy_wait_2():
    while True:
        print("busy wait 2")
        await asyncio.sleep(1) #Sleeps for 1 second, it can be less
        
asyncio.get_event_loop().create_task(busy_wait_1())
asyncio.get_event_loop().create_task(busy_wait_2())
asyncio.get_event_loop().run_forever()
```

In the example above, this will print "busy wait 1" and "busy wait 2" many times. If both asyncio.sleep(1) are removed, then it will only print "busy wait 1". This is different from ```time.sleep(1)``` because the latter blocks the whole program, so replacing ```await asyncio.sleep(1)``` with ```time.sleep(1)``` will only print "busy wait 1".

## Input
In ```async def sender(conn)``` async function, it waits for the user's input in order to send that to the server. However, input() is blocking and will block all tasks unfortunately. In order to avoid this, the library ```aioconsole``` was used