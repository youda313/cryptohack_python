from pwn import * # pip install pwntools
import json
import base64
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range (1000):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])


    if received["type"] == "base64":
        st_to_decode = base64.b64decode(received["encoded"])
        decoded = st_to_decode.decode("utf-8")
    elif received["type"] == "hex":
        byte_array = bytearray.fromhex(received["encoded"])
        decoded = byte_array.decode()
    elif received["type"] == "rot13":
        decoded = codecs.decode(received["encoded"], 'rot-13')
    elif received["type"] == "bigint":
        st_to_decode = received["encoded"]
        st_to_decode = st_to_decode[2:]
        byte_array = bytearray.fromhex(st_to_decode)
        decoded = (byte_array.decode())
        
    elif received["type"] == "utf-8":
        array_answer = [chr(b) for b in received["encoded"]]
        decoded = ''.join(array_answer)

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)








