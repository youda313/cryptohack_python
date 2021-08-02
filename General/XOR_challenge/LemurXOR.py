#https://crypto.stackexchange.com/questions/88430/how-to-decrypt-two-images-encrypted-using-xor-with-the-same-key
#https://stackoverflow.com/questions/61304857/calculating-xor-of-the-two-images
#pip install image

from PIL import Image, ImageChops
im1 = Image.open('c:/Users/User/Github/cryptohack_python/General/XOR_challenge/lemur.png')
im2 = Image.open('c:/Users/User/Github/cryptohack_python/General/XOR_challenge/flag.png')

im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
im3.show()