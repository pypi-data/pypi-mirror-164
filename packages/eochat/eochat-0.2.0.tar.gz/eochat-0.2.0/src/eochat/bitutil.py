def put16bit(msg):  # time.time_ns() // 1000000
    msg &= 0xffff
    return msg & 0xff,msg >> 8  # is faster

def split_to_8bits(num, size):
    x = []
    while num:
        x.append(num & 0xff)
        num >>= 8
    while len(x) < size:
        x.append(0)
    return x
