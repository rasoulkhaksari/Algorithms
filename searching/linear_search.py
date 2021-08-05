class LinearSearch:
    def __init__(self,data:list) -> None:
        self.data = data

    def find(self,target)->int:
        if target is None:
            return -1
        for i in range(len(self.data)):
            if self.data[i]==target:
                return i
        return -1