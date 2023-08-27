class Codec:
    def __init__(self):
        self.salt = 'puru'
    
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return self.salt.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(self.salt)
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))