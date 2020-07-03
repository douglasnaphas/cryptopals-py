# Set 1 Challenge 3: Single-byte XOR cipher

This pretty much works.

From the top-level directory for this repo, run

```
python -m set1.challenge3_1_byte_XOR_cipher.s1c3
```

I need to make a better solution based on this:

```
>>> s = '1b37373331363f'
'1b37373331363f'
>>> [chr(int(y, 16) ^ 88) for y in [''.join(x) for x in zip(s[0::2], s[1::2])]]
['C', 'o', 'o', 'k', 'i', 'n', 'g']
```
