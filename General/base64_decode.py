import base64
code = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#decode hex
byte_array = bytearray.fromhex(code)

#convert to base64 from byte array
print(base64.b64encode(byte_array))