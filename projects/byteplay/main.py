str1 = "Hello World"
barr = bytearray()
for byteItem in list(bytes(str1, encoding='utf-8')):
    barr.append(byteItem)
print(barr)
print(bytes(barr))
print(bytes(barr).decode())
print(b''.join([x.encode() for x in bytes(barr).decode()]))
print(bytes(str1, encoding='utf-8'))