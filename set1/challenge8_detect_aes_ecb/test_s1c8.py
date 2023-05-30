import unittest
from utils.utils import Utils


class TestDetectingAESECB(unittest.TestCase):
    def test_challenge_8_solution(self):
        with open("set1/challenge8_detect_aes_ecb/8.txt", "r") as f:
            ciphertexts = [line.rstrip() for line in f]
        self.assertEqual(
            ciphertexts[0],
            "8a10247f90d0a05538888ad6205882196f5f6d05c21ec8dca0cb0be02c3f8b09e382963f443aa514daa501257b09a36bf8c4c392d8ca1bf4395f0d5f2542148c7e5ff22237969874bf66cb85357ef99956accf13ba1af36ca7a91a50533c4d89b7353f908c5a166774293b0bf6247391df69c87dacc4125a99ec417221b58170e633381e3847c6b1c28dda2913c011e13fc4406f8fe73bbf78e803e1d995ce4d",
        )
        block_size = 16
        ecb_mode_ciphertexts = Utils.detect_duplicate_blocks(ciphertexts, block_size)
        self.assertEqual(len(ecb_mode_ciphertexts), 1)
        the_answer = ecb_mode_ciphertexts[0]
        # Split the answer into size 16 blocks. There should be duplicates.
        blocks = [
            the_answer[beg : beg + block_size]
            for beg in range(0, len(the_answer), block_size)
        ]
        block_set = set(blocks)
        self.assertGreater(len(blocks), len(block_set))
        self.assertEqual(
            the_answer,
            "d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a",
        )
