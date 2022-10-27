class Logger:

    def __init__(self):
        self.d = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.d[message] <= timestamp:
            self.d[message] = timestamp + 10
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)