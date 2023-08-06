from eochat.bitutil import put16bit,split_to_8bits

def ping(client_time):
    t1,t2 = put16bit(client_time)
    return [3,0,t1,t2]

def build_chat(chatline):
  x = [10,0,0,0]
  for char in chatline:
    for byte in char.encode('utf-8'):
      x.append(byte)
  x[2],x[3] = put16bit(len(x)-4)
  return x 

def build_appearance(sex, tribe, mane, tail, eyes,
                     coat_r, coat_g, coat_b,
                     mane_r, mane_g, mane_b,
                     equip0, equip1, equip2):
    appearance = (coat_r << 32) | (coat_g << 3) | coat_b
    appearance |= (mane_r << 41) | (mane_g << 38) | (mane_b << 35)
    appearance |= (tribe << 6) | (sex << 8)
    appearance |= (mane << 10) | (tail << 13) | (eyes << 16)

    return [21,0] + split_to_8bits(appearance, 8)
