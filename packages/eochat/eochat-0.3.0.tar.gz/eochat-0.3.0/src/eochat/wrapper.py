from eochat.periodic import *
from eochat.processer import *
from eochat.builder import *
import eochat.crypto as crypto

from tornado.platform.asyncio import to_asyncio_future
from aioconsole import ainput
from collections import deque
from pathlib import Path
from shutil import copyfile
from datetime import datetime
import tornado.websocket
import tornado.platform.asyncio
import tornado.httpclient
import asyncio
import base64
import os
import struct
import urllib.parse
import json
import toml
import sys
import platform

is_win = any(platform.win32_ver())

OP_AUTH_RESPONSE    = 0x0014
OP_AUTH_CHALLENGE   = 0x8021
OP_AUTH_RESULT      = 0x8022

MODE_SSO            = 0
MODE_LOCAL          = 1

host = 'main'

def getCurrDate():
  return datetime.now().strftime('%H:%M:%S')

def select_host(host):
    return (True if host == 'main' else False)


if not host:
    assert False, 'unknown OUTPOST_HOST: %r' % host
    sys.exit(1)

which       = select_host(host)
AUTH_HOST   = 'auth.everfree-outpost.com' if which else 'localhost:5000'
AUTH_BASE   = f'https://{AUTH_HOST}'
AUTH_ORIGIN = 'http://play.everfree-outpost.com' if which else 'http://localhost:8889'
GAME_URL    = 'ws://game2.everfree-outpost.com:8888/ws' if which else 'ws://localhost:8888/ws'
del host, which

async def do_login(user, password):
    auth_client = tornado.httpclient.AsyncHTTPClient()

    args    = { 'name': user, 'password': password}
    headers = { 'Host': AUTH_HOST, }
    resp = await auth_client.fetch(f'{AUTH_BASE}/login', method='POST',
                                   body=urllib.parse.urlencode(args), headers=headers,
                                   follow_redirects=False, raise_error=False)
    assert resp.code == 302
    cookie = resp.headers['Set-Cookie'].partition(';')[0]
    return cookie

async def get_response(challenge, cookie):
    auth_client = tornado.httpclient.AsyncHTTPClient()

    headers = {
        'Origin': AUTH_ORIGIN,
        'Host': AUTH_HOST,
        'Cookie': cookie,
    }
    body = json.dumps({
        'challenge': base64.urlsafe_b64encode(challenge).decode('ascii'),
    })
    resp = await auth_client.fetch(f'{AUTH_BASE}/api/sign_challenge', method='POST',
                                   body=body, headers=headers)
    j = json.loads(resp.body.decode('ascii'))
    assert j['status'] == 'ok'
    return base64.urlsafe_b64decode(j['response'].encode('ascii'))

async def do_auth(conn, cookie):
    response = await to_asyncio_future(get_response(conn.cb_token, cookie))
    await conn.send(struct.pack('<H', OP_AUTH_RESPONSE) + response)

    while True:
        msg = await to_asyncio_future(conn.recv())
        if msg is None:
            assert False, 'server disconnected unexpectedly'
        opcode, = struct.unpack('<H', msg[:2])

        if opcode == OP_AUTH_RESULT:
            flags, = struct.unpack('<H', msg[2:4])
            if flags == 1:
                name = msg[4:].decode('ascii')
                return name
            else:
                assert False, 'bad auth result: %s' % flags

        else:
            assert False, 'bad opcode: %x' % opcode


async def sender(conn):
    try:
        while True:
            msg = await ainput("")
            await conn.send(build_chat(msg))
    finally:
        asyncio.get_event_loop().stop()


async def receiver(conn):  # , stdout):
    try:
        while True:
            msg = await to_asyncio_future(conn.recv())
            if msg is None:
                assert False, 'server disconnected'
            op, msg = decode_message(msg)

            if op == CHAT_UPDATE:
                msg = msg.split('\t')                
                if msg[2] == "27686": msg[2] = " (local)"
                else: msg[2] = ""
                
                print(f'[{getCurrDate()}] {msg[0]}{msg[2]}: {msg[1]}')

    finally:
        asyncio.get_event_loop().stop()

class EncryptedSocket:
    def __init__(self):
        self.conn = None
        self.proto = None
        self.recv_queue = deque()
        self.cb_token = None

    async def connect(self, url):
        self.conn = await to_asyncio_future(tornado.websocket.websocket_connect(url))
        self.proto = crypto.Protocol(initiator=True)

        # Perform handshake
        self.proto.open()
        while True:
            evt = self.proto.next_event()
            if evt is None:
                msg = await to_asyncio_future(self.conn.read_message())
                self.proto.incoming(msg)
            elif isinstance(evt, crypto.RecvEvent):
                self.recv_queue.append(evt.data)
            elif isinstance(evt, crypto.OutgoingEvent):
                self.conn.write_message(evt.data, binary=True)
            elif isinstance(evt, crypto.HandshakeFinishedEvent):
                self.cb_token = evt.cb_token
                return
            elif isinstance(evt, crypto.ErrorEvent):
                raise ValueError('crypto error: %s' % evt.message)
            else:
                assert False, 'unknown event type in connect: %r' % (evt,)

    async def recv(self):
        if len(self.recv_queue) > 0:
            return self.recv_queue.popleft()

        while True:
            evt = self.proto.next_event()
            if evt is None:
                msg = await to_asyncio_future(self.conn.read_message())
                self.proto.incoming(msg)
            elif isinstance(evt, crypto.RecvEvent):
                return evt.data
            elif isinstance(evt, crypto.OutgoingEvent):
                self.conn.write_message(evt.data, binary=True)
            elif isinstance(evt, crypto.ErrorEvent):
                raise ValueError('crypto error: %s' % evt.message)
            else:
                assert False, 'unexpected event type in recv: %r' % (evt,)

    async def send(self, data):
        self.proto.send(data)

        while True:
            evt = self.proto.next_event()
            if evt is None:
                return
            elif isinstance(evt, crypto.RecvEvent):
                self.recv_queue.append(evt.data)
            elif isinstance(evt, crypto.OutgoingEvent):
                self.conn.write_message(evt.data, binary=True)
            elif isinstance(evt, crypto.ErrorEvent):
                raise ValueError('crypto error: %s' % evt.message)
            else:
                assert False, 'unexpected event type in send: %r' % (evt,)

def read_file(fname: str) -> str:
    file = open(fname, 'r')
    res = file.read()
    file.close()
    return res

async def amain(user, password):
    print('logging in as %r...' % user)
    cookie = await to_asyncio_future(do_login(user, password))
    print(f'{cookie}\nConnecting...')

    conn = EncryptedSocket()
    await conn.connect(GAME_URL)
    print(f'{conn.cb_token}\nAuthenticating...')

    name = await do_auth(conn, cookie)
    print(f'Connected as {name}')

    await conn.send([22,0])  # start
    await asyncio.sleep(2)

    # Customize Character Appearance
    appearance = []

    def read_cfg(cfgfp):
        cfg = toml.loads(read_file(cfgfp))
        appearance = cfg['character']['appearance']
        return appearance

    cfgfp = Path(r'%APPDATA%\eochat\config.toml').expanduser() if is_win else Path('~/.config/eochat/config.toml').expanduser()
    if (not cfgfp.exists()):
        os.makedirs(os.path.dirname(cfgfp), exist_ok = True)
        copyfile(f'{Path(__file__).resolve().parents[2]}/config.toml', cfgfp)
    appearance = read_cfg(cfgfp)

    await conn.send(build_appearance(*appearance))

    asyncio.get_event_loop().create_task(receiver(conn))
    asyncio.get_event_loop().create_task(sender(conn))
    asyncio.get_event_loop().create_task(iping(conn))

    print("Connected to Server")

def main():
    user = os.environ.get('OUTPOST_USER') or input('username: ')
    password = os.environ.get('OUTPOST_PASSWORD') or input('password: ')

    tornado.platform.asyncio.AsyncIOMainLoop().install()
    asyncio.get_event_loop().create_task(amain(user, password))
    asyncio.get_event_loop().run_forever()
