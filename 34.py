
v = open('auto_bad', 'rb')
b = v.seek(3)
b = v.read(1)

b = b.decode('ansi')

c = 'e'

while b == '$':
    v.read(1)
    c = v.readline()
print(c)
        
        #v.readlines()
        #v.read()
        #v = bytearray(v)
        #v = v.decode('ansi')
        #v = open('auto_bad')
        #v = (v.decode('ansi'))
        #v.readlines()
        #line = v.readline()

