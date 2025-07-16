#working with binary files (bin)
## binary file we append bytes

data= b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
with open('python\\example.bin', 'wb') as file:  # 'wb' for write binary
    file.write(data)


with open('python\\example.bin', 'rb') as file:
    content = file.read()  # 'rb' for read binary
    print(content)