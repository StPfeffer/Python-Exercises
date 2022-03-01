import zlib


s = b"hello world!hello world!hello world!hello world!"

compressed = zlib.compress(s)
decompressed = zlib.decompress(compressed)

print(compressed)
print(decompressed)
