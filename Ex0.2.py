import hashlib
import os
def MD5_hash(string, encoding='utf-8'):
    md5_hasher = hashlib.md5()
    md5_hasher.update(string.encode(encoding))
    return md5_hasher.hexdigest()

with open('rockyou.txt', encoding='utf8') as f:
    for line in f:
        a= line.strip()
        if ( MD5_hash(a) == 'ab4f63f9ac65152575886860dde480a1'):
            print (a + ' md5 ab4f63f9ac65152575886860dde480a1' )
            break
f.close()
