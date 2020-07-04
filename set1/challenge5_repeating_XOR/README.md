# Set 1 Challenge 5: Implement repeating-key XOR

This:

```
cat set1/challenge5_repeating_XOR/stanza-no-nls.txt | tr -d '\n' | python -m set1.challenge5_repeating_XOR.s1c5 -k 'ICE'
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20690a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```

prints the same characters as the two expected output lines of https://cryptopals.com/sets/1/challenges/5 concatenated together.

This makes it seem like newlines are not a factor in the example input/output in the challenge.
