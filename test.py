
usr = '13036790254@csyxy'
data = b'\x03\x01\x00' + bytes([len(usr) + 20])
print(data)
