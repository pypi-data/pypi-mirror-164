from collections import namedtuple
from ctypes import *
import os
import pathlib

import platform
is_win = any(platform.win32_ver())
client_dir = os.path.dirname(os.path.dirname(f'{os.getcwd()}/../'))

OCC_EVENT_NONE                  = 0
OCC_EVENT_RECV                  = 1
OCC_EVENT_OUTGOING              = 2
OCC_EVENT_HANDSHAKE_FINISHED    = 3
OCC_EVENT_ERROR                 = 4
OCC_CHANNEL_BINDING_TOKEN_LEN   = 32

class Library:
    def __init__(self, path):
        self.dll = CDLL(path)

        c_ubyte_p = POINTER(c_ubyte)
        c_size_t_p = POINTER(c_size_t)

        self._func('occ_protocol_new', [c_ubyte], c_void_p)
        self._func('occ_protocol_delete', [c_void_p], None)

        self._func('occ_protocol_next_event', [c_void_p], c_ubyte)
        self._func('occ_protocol_recv_data', [c_void_p, c_size_t_p], c_ubyte_p)
        self._func('occ_protocol_outgoing_data', [c_void_p, c_size_t_p], c_ubyte_p)
        self._func('occ_protocol_handshake_finished_channel_binding_token',
                   [c_void_p], c_ubyte_p)
        self._func('occ_protocol_error_message', [c_void_p, c_size_t_p], c_ubyte_p)

        self._func('occ_protocol_open', [c_void_p], None)
        self._func('occ_protocol_send', [c_void_p, c_ubyte_p, c_size_t], None)
        self._func('occ_protocol_incoming', [c_void_p, c_ubyte_p, c_size_t], None)

    def _func(self, name, args, res):
        f = getattr(self.dll, name)
        f.argtypes = args
        f.restype = res
        setattr(self, name, f)


# default: The default build location
# install: The default installed location for the library
libname = 'libeoclient_crypt.dll' if is_win else 'libeoclient_crypt.so'
default = f'target/release/{libname}'
install = f'C:\\Program Files\\Everfree Outpost\\{libname}' if is_win else f'/usr/local/lib/{libname}'

if (pathlib.Path(install).exists):
    crypto = Library(install)
else:
    crypto = Library(default)

class RawProtocol:
    def __init__(self, initiator):
        self.ptr = crypto.occ_protocol_new(int(initiator))

    def __del__(self):
        if self.ptr:
            crypto.occ_protocol_delete(self.ptr)
            self.ptr = None

    def next_event(self):
        return crypto.occ_protocol_next_event(self.ptr)

    def recv_data(self):
        size = c_size_t()
        buf_ptr = crypto.occ_protocol_recv_data(self.ptr, byref(size))
        assert buf_ptr
        return bytes(buf_ptr[0 : size.value])

    def outgoing_data(self):
        size = c_size_t()
        buf_ptr = crypto.occ_protocol_outgoing_data(self.ptr, byref(size))
        assert buf_ptr
        return bytes(buf_ptr[0 : size.value])

    def handshake_finished_channel_binding_token(self):
        buf_ptr = crypto.occ_protocol_handshake_finished_channel_binding_token(self.ptr)
        assert buf_ptr
        return bytes(buf_ptr[0 : OCC_CHANNEL_BINDING_TOKEN_LEN])

    def error_message(self):
        size = c_size_t()
        buf_ptr = crypto.occ_protocol_error_message(self.ptr, byref(size))
        assert buf_ptr
        return bytes(buf_ptr[0 : size.value])

    def open(self):
        crypto.occ_protocol_open(self.ptr)

    def send(self, b):
        arr = (c_ubyte * len(b))()
        arr[:] = b
        crypto.occ_protocol_send(self.ptr, arr, len(b))

    def incoming(self, b):
        arr = (c_ubyte * len(b))()
        arr[:] = b
        crypto.occ_protocol_incoming(self.ptr, arr, len(b))


RecvEvent = namedtuple('RecvEvent', ('data',))
OutgoingEvent = namedtuple('OutgoingEvent', ('data',))
HandshakeFinishedEvent = namedtuple('HandshakeFinishedEvent', ('cb_token',))
ErrorEvent = namedtuple('ErrorEvent', ('message',))

class Protocol:
    def __init__(self, initiator):
        self.raw = RawProtocol(initiator)

    def next_event(self):
        kind = self.raw.next_event()
        if kind == OCC_EVENT_NONE:
            return None
        elif kind == OCC_EVENT_RECV:
            return RecvEvent(self.raw.recv_data())
        elif kind == OCC_EVENT_OUTGOING:
            return OutgoingEvent(self.raw.outgoing_data())
        elif kind == OCC_EVENT_HANDSHAKE_FINISHED:
            return HandshakeFinishedEvent(
                self.raw.handshake_finished_channel_binding_token())
        elif kind == OCC_EVENT_ERROR:
            return ErrorEvent(self.raw.error_message().decode('utf-8'))

    def open(self):
        self.raw.open()

    def send(self, b):
        self.raw.send(b)

    def incoming(self, b):
        self.raw.incoming(b)
