with open('egnos_1', 'rb') as f: d = f.read()
dd = d.split(b'$GPGGA')

#dd = bytearray(dd)
#dd.decode('ansi')
dc = [s[:s.find(b'\r')] for s in dd[1:]]
print(dd[:10])
