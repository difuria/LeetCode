# https://leetcode.com/problems/logger-rate-limiter/
class Logger:

    def __init__(self):
        self.previous_messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.previous_messages:
            if timestamp >= self.previous_messages[message] + 10:
                self.previous_messages[message] = timestamp    
                return True
        else:
            self.previous_messages[message] = timestamp
            return True    

        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
