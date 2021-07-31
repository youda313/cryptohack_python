import base64
import codecs

#HEXADECIMAL => DONE
#test = "696c6c75737472617465645f6e65636573736172696c795f686f6c6f6361757374"
#byte_array = bytearray.fromhex(test)
#print(byte_array.decode())

#BASE 64 =>DONE
#s_to_decode = "ZGV0ZWN0ZWRfZmlyZWRfdmVyYmFs"
#a = base64.b64decode(s_to_decode)
#print(a.decode("utf-8"))


#UTF-8 =>DONE
received = [101, 110, 103, 97, 103, 101, 95, 104, 101, 108, 100, 95, 115, 116, 114, 101, 110, 103, 116, 104, 101, 110, 105, 110, 103]
decoded = [chr(b) for b in received]
print(''.join(decoded))

#ROT13 => DONE
#rot13_s = 'tests_abcdefghig_demodemo'
#encoded = codecs.encode(rot13_s, 'rot_13')
#print(encoded)
#decoded = codecs.decode(encoded, 'rot-13')
#print(decoded)

#BIG INT => DONE
#received = "0x6c756369615f66756e6374696f6e616c5f6167726565"
#st_to_decode = received[2:]
#byte_array = bytearray.fromhex(st_to_decode)
#print(byte_array.decode())

#st_to_encode = "iam_the_answer"
#ciphertext_lenght = len(str(st_to_encode))
#encoded = hex(st_to_encode.to_bytes(ciphertext_lenght,'big'))
#print(encoded)
#bytearray_mess_ascii = ciphertext.to_bytes(ciphertext_lenght,'big')
#print(''.join(chr(i) for i in bytearray_mess_ascii))