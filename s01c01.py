import base64
import binascii
import codecs

s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

#out = base64.b64encode(s.decode("hex"))
out = codecs.encode(codecs.decode(s, 'hex'), 'base64').strip()
print out
print result
assert(out == result)
