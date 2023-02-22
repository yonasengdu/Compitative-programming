class Link:
    def __init__(self,url):
        self.url = url
        self.next = None
        self.previous = None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.page = Link(homepage)
        self.current = self.page
        
    def visit(self, url: str) -> None:
        newpage = Link(url)
        newpage.previous = self.current
        self.current.next = newpage
        
        self.current = newpage
        # print(self.current.url)
        
        
    def back(self, steps: int) -> str:
        temp_current = self.current
        # print(temp_current.url)
        while temp_current.previous and steps:
            temp_current = temp_current.previous
            # print(self.current.url)
            steps -= 1
        self.current = temp_current
        
        return self.current.url
    

    def forward(self, steps: int) -> str:
        temp_current = self.current
        while temp_current.next and steps:
            temp_current = temp_current.next
            steps -= 1
        self.current = temp_current
        
        return self.current.url
         

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)