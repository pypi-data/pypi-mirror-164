# Tornado
Tornado is a Python web framework and asynchronous networking library, It is pretty useful because it provides non-blocking network I/O and async versions of its components. This is mostly used for the authentication process via HTTP/HTTPS and for creating the websocket to send and receive packages once we are logged in.

## httpclient
It is a non-blocking HTTP client. This is instantiated inside functions ```do_login``` and ```get_response```

```
async def do_login(user, password):
    auth_client = tornado.httpclient.AsyncHTTPClient()
    ...
    resp = await auth_client.fetch(...,method='POST')
    
async def get_response(challenge, cookie):
    auth_client = tornado.httpclient.AsyncHTTPClient()
    ...
    resp = await auth_client.fetch(...,method='POST')
```

Since this works together with asyncio, then ```await``` is used in order to wait for the server's response which will be retrieved with ```auth_client.fetch(url,...)```. They are both called inside async functions too.

## websocket
Websockets allow for bidirectional communication between the client and the server. This is useful because all the communication and interaction between all players go through websockets. In this case, only one is used.

```
async def connect(self, url):
        self.conn = await to_asyncio_future(tornado.websocket.websocket_connect(url))
        ...
```

```tornado.websocket.websocket_connect(url)``` returns a ```WebSocketClientConnection``` object that will allow the program to write and read messages to and from the server. OP encrypts and decrypts each message with his crypto library and is handled inside OP's ```send``` and ```recv``` functions in his class ```EncryptedSocket```. 

Once the player is logged in, all communication happens in functions ```sender``` and ```receiver``` 

```
async def sender(conn):    
    try:
        while True:
            msg = await ainput("")
            await conn.send(build_chat(msg))
    finally:
        asyncio.get_event_loop().stop()
```

User input will be stored in msg. In this case, it will be a chatline that will be sent to the server and then to other players. However, the string itself is not sent directly to the server, it needs to be split into an array before it is sent. This is done inside the ```build_chat(msg)``` function. Since ```input``` is blocking, then ```ainput()``` from the ```aioconsole``` library was used instead, Otherwise the client wouldn't process any incoming packets from the server while waiting for the user input.

```
async def receiver(conn):    
    try:
        while True:
            msg = await to_asyncio_future(conn.recv())
            if msg is None:
                assert False, 'server disconnected'          
            op,msg = decode_message(msg)
                    
            if op == CHAT_UPDATE:
                msg = msg.split('\t')
                print("{}: {}".format(msg[0],msg[1]))
    finally:
        f.close()
        asyncio.get_event_loop().stop()
```

Similarly, it waits for a message from the server and process it accordingly. There are many types of messages the server can send and each one has a different structure and an ```OP_CODE```; the latter is necessary so the client knows what structure the packet has. In this case, it is processed in the function ```decode_message(msg)``` which returns the type of message and, in this case, the chatline itself.

Keep in mind both conn used in ```sender``` and ```receiver``` is an ```EncryptedSocket``` object that uses ```tornado.websocket.websocket_connect(url)``` to create a  ```WebSocketClientConnection``` object that will handle writing and reading messages and the encryption part is handled by his crypto module.

## Asyncio integration
This is done with ```platform.asyncio``` which is the bridge between ```Tornado``` and ```asyncio```. However, nowadays, this is automatically enabled once ```asyncio``` becomes available so there is no need to refer to all of this directly (i.e. it is deprecated!). Regardless, it is used by OP, so, yeah.

```
def main():
    ...
    tornado.platform.asyncio.AsyncIOMainLoop().install()
    ...
```
In order for both of ```Tornado``` and ```asyncio``` to have the same event loop, or at least one corresponds to the other, then the method above is called. This will create an ```IOLoop``` that corresponds to the current ```asyncio``` event loop (i.e. ```asyncio.get_event_loop()```).

wrapper.py has many calls to ```await to_asyncio_future(...)``` which basically returns an ```asyncio.Future``` that will work with ```asyncio``` itself, so it can be awaited just like a regular async function. 


