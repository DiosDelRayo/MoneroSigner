from xmrsigner.models.base_encoder import BaseQrEncoder, BaseStaticQrEncoder
from xmrsigner.models.qr_type import QRType
from xmrsigner.helpers.compactseed import CompactSeed
from typing import List


class SeedQrEncoder(BaseStaticQrEncoder):

    def __init__(self, seed_phrase: List[str], wordlist: List[str]):
        super().__init__()
        self.seed_phrase = seed_phrase
        self.wordlist = wordlist
        
        if self.wordlist == None:
            raise Exception('Wordlist Required')

    def next_part(self):
        data = ""
        # Output as Numeric data format
        for word in self.seed_phrase:
            index = self.wordlist.index(word)
            data += str("%04d" % index)
        return data

    def get_qr_type(self):
        return QRType.SEED__SEEDQR


class CompactSeedQrEncoder(SeedQrEncoder):

    def next_part(self):
        seed_phrase = self.seed_phrase.copy()
        if len(seed_phrase) in (13, 25):  # monero seed with checksum word, remove checksum word at the end
            del seed_phrase[-1]

        if len(seed_phrase) not in (12, 16, 24):  # results in (16, 22, 32) bytes per seed
            raise Exception('Neither a monero seed nor a polyseed!')

        return CompactSeed(self.wordlist).bytes(seed_phrase)

    def get_qr_type(self):
        return QRType.SEED__COMPACTSEEDQR
