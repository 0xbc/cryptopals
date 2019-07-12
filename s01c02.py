import base64
import binascii
import codecs

s = '1c0111001f010100061a024b53535009181c'
r = '686974207468652062756c6c277320657965'
result = '746865206b696420646f6e277420706c6179'

#out = codecs.encode(codecs.decode(s, 'hex'), 'base64').strip()
s_bytes = codecs.decode(s, 'hex').strip()
r_bytes = codecs.decode(r, 'hex').strip()

z_bytes = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s_bytes, r_bytes))
print z_bytes

z = codecs.encode(z_bytes, 'hex')
assert(z == result)

#print out
#print result
