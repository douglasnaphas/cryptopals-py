import unittest
from parameterized import parameterized
from utils.utils import Utils


class TestDetectDuplicateBlocks(unittest.TestCase):
    @parameterized.expand(
        [
            (["aa"], 1, ["aa"]),
            (["aa", "ab"], 1, ["aa"]),
            (
                [
                    "5c4ca78f8de3527788e7d1efcd6aad0adc3878ea70993ae20937ef0a601730494946f078de2099c62de9af1c47ee4f18216ed5a7268464f210374dbf421d55449c8f399d8824c5a0ff8526a940223ee999a6f945f0ba3eaa672c434ad867ac7adaa46bd3289729c6c7d920dd0d8237bf678d88bde91e0683e72e88fef50bdb23cceb6270acba5aeebd0a834ccf99cd3e6bad8c158f5819f1f1c785fdaa3df505",
                    "d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a",
                    "b563aac8275730bd4cf89ab32bb4b152be8fae16afab58ab3ea0e825c8ce28ddbe26c8cafef763f1d9c3f30d60335cd0b765b98a11d5cfbe7a2d75e8f8a5e851ee6a17de174d8bea5c1e089beffc99709d6dcc03e578220eccdfa99d3fa0a3d2f6736de041cd783ad7f866df5dcd2a752cfbfc380cf84da5c5dd3fc486cf1adc14d29d9e91737514e8c67d5c5aece4a19216e2b069f53b8ab4acaef17f815004",
                    "61750df604b4ddc333b9e669b218e46bbe50be4b2d3a76e8043e79e98eac204797138e0eae7f39ce256a1a315476039a8f0776a724270f32b32c973d6316f281081970dccb8c13b9f8df927b1dd29eec37f4b68a3e3179a62329bcee1407d00cb1ff2a636a42ca8e939e6a9c56a382289ae5cbb7eb07df1182a7ef10882f28a7fe5d8582a2fb93b4fdf02ccd5b9050b60665771a21c0f35cb29eea40710dec75",
                    "32d13a6e522e33e556b5b084b1e6811157e88ef0a897b6e62d31c984a51957eebf6b1e46ea80b1def31d34a99bb5a630d9127537537dda3f88eaf2bee4c37d859cf91387963e67748e7c09b3e0c1c8ce56937bded53e2b353dcb39e8aafe8ccdf71e82d88df62184750b125bd09064e296c5caca1122ec13aa030cf79ab9394746a377ae2e93a78986fa3531098c3e904a6b0cddaa4c8dea9b807cf63f464dce",
                ],
                16,
                [
                    "d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a"
                ],
            ),
        ]
    )
    def test_detect_duplicate_blocks(self, strs, block_size, expected):
        self.assertEqual(Utils.detect_duplicate_blocks(strs, block_size), expected)
