import io
import struct
import sys

''' 
 ##########  Refer https://www.devdungeon.com/content/working-binary-data-python   #################
'''
# Initializing empty byte
empty_bytes = bytes(1)
print(type(empty_bytes))

# Create a byte that represents string
byte = bytes('Hello', 'utf-8')
print(type(byte))
print(byte)

# Another way to create a byte
byte = b'1234'
print(type(byte))

# This is a string type
byte = '0123456789'
print(type(byte))
print(byte[5]) # byte can be treated like an array
for s in byte: print(s)  # iterate over every byte and print value

# byte array is mutable
print(bytes([3]))
byte = bytearray('Hello', 'utf-8')
print(type(byte))
print(byte)
byte[0]=3
print(byte)
for s in byte: print(s)  # iterate over every byte and print value
for s in b'c': print(f"c: {s}") # print integer value of any char


# binary stream
stream = io.BytesIO()
stream.write('hello world'.encode('ascii'))
stream.write('hello world'.encode('utf-8'))

print(stream.seek(0))  # move cursor to the begining of the buffer
print(stream.read())  # Read the entire buffer

mutable_buffer = stream.getbuffer()
print(type(mutable_buffer))  # class 'memoryview'
mutable_buffer[0] = 99
print(stream.seek(0))  # move cursor to the begining of the buffer
print(stream.read())  # Read the entire buffer


# write byte array to a file


# Reading bytes from a file


# bit wise operator
byte1 = int('11110000', 2)  # 240
byte2 = int('00001111', 2)  # 15
byte3 = int('01010101', 2)  # 85


print(byte1)
print(~byte1)  # Complement bits

print(byte1 & byte3)  # And

print(byte1 | byte2)  # OR

print(byte2 >> 2)  # Shift bytes right

print(16+32+64+128)
print(1+2+4+8)

# convert integer to a binary format
byte1 = int('11110000', 2)  # 240
byte2 = 1
byte3 = 2
print(bin(byte1).lstrip('0b'))
print(bin(byte2).lstrip('0b'))
print(bin(byte3).lstrip('0b'))

i=240
print("{0:b}".format(i)) # binary: 11111111
print("{0:x}".format(i)) # hexadecimal: ff
print("{0:o}".format(i)) # octal: 377

# Convert integer to bytes
print(byte1)
b = byte1.to_bytes(4, sys.byteorder)
print(f"Byte1:{byte1.to_bytes(4, sys.byteorder)}")
print(struct.pack('i', 240))  # convert integer to byte

# Convert byte to integer
a_byte = b'\xff'  # 255
i = ord(a_byte)   # Get the integer value of the byte
print(i)
print (int.from_bytes(b'\xf0\x00\x00\x00', sys.byteorder)) # convert integer from bytes


# Text encoding
# Binary to Text
binary_data = b'I am text.'
print(binary_data)
text = binary_data.decode('utf-8')
print(text)

binary_data = bytes([65, 66, 67])  # ASCII values for A, B, C
print(binary_data)
text = binary_data.decode('utf-8')
print(text)

# Text to Binary
message = "Hello"  # str
binary_message = message.encode('utf-8')
print(type(binary_message))  # bytes


binary_data = struct.pack("icc", 8499000, b'A', b'Z')
print(binary_data)
tuple_of_data = struct.unpack("icc", binary_data)
print(tuple_of_data)


print("Native byteorder: ", sys.byteorder)