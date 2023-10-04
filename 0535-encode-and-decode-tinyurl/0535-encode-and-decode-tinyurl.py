class Codec:
    def __init__(self):
        self.Map = defaultdict(str)
        self.num = 0

    def encode(self, longUrl: str) -> str:
        tinyUrl = "http://tinyurl.com/" + str(self.num)
        self.num += 1
        self.Map[tinyUrl] = longUrl
        
        return tinyUrl 
        
       
        

    def decode(self, shortUrl: str) -> str:
        print(shortUrl)
        return self.Map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))