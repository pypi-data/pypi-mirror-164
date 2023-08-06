import struct

CHAT_UPDATE = 0x800b

def decode_message(msg):
    op = struct.unpack_from('H',msg,0)
    return (op[0], msg[7:].decode("utf_8")+"\t"+str(struct.unpack_from('H',msg,4)[0])) if op[0] == CHAT_UPDATE else (op[0], None)
