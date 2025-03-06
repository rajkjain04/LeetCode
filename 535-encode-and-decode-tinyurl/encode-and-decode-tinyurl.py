class Codec:

    def __init__(self):
        self.count = 0 
        self.encodeMap = {} 
        self.decodeMap = {} 

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.encodeMap[longUrl] = str(count) 
        self.decodeMap[str(count)] = longUrl 
        self.count += 1 
        return str(count)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))