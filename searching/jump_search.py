import math

class JumpSearch:
    def __init__(self,data:list) -> None:
        self.data = sorted(data)

    def find(self,target)->int:
        if target is None:
            return -1
        dataSize = len(self.data)
        stepSize = int(math.sqrt(dataSize))
        step=stepSize
        prev = 0
        while self.data[min(step, dataSize)-1] < target:
            prev = step
            step += stepSize
            if prev >= dataSize:
                return -1
        while self.data[prev]<target:
            prev+=1
            if prev==min(step,dataSize):
                return -1
        if self.data[prev]==target:
            return prev
        return -1
