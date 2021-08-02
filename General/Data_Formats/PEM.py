#TODO

import pem
import base64


#Extract the private key d as a decimal integer from this PEM-formatted RSA key.
cert = pem.parse_file(r"c:\Users\User\Github\cryptohack_python\General\Data_Formats\privacy_enhanced_mail.pem")


private_key = str(cert[0])
pk_firstline = '\n'.join(private_key.split('\n')[1:-1])
pk_secondline = '\n'.join(pk_firstline.split('\n')[0:-1])
without_line_breaks = pk_secondline.replace("\n", "")

b64decoded_hex = base64.b64decode(without_line_breaks).hex()
private_key_decimal = int(b64decoded_hex, 16)
print(private_key_decimal)
