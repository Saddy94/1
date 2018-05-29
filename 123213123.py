## coding: utf-8
#import binascii


#def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
 #   n = int(bits, 2)
  #  return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

b = open('egnos_1', 'rb')
#b.seek(3)
#c = b.read()
c = b.read(6)
c = bytearray(c)
c = c.decode('ansi')

if "$GPGGA" in c:
    b.seek(7)
    time = float(b.read(9))
    b.seek(17)
    lat_deg = (b.read(12))
    lat = float(lat_deg[2:12])/60 + float(lat_deg[0:2])
    b.seek(32)
    lon_deg = b.read(13)
    lon = float(lon_deg[4:13])/60 + float(lon_deg[0:3])
    b.seek(58)
    h_0 = b.read(8)
    b.seek(69)
    h_geo = b.read(7)
    h = float(h_0) + float(h_geo)
   # x.decode('ascii')
   # x = float(x)
print(h)
