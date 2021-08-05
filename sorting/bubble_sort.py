class BubbleSort:
    def __init__(self,data:list) -> None:
        if data is None:
            raise TypeError("data cannot be None")
        self.data:list =data 

    def sort(self):
        for i in range(len(self.data)):
            for j in range(0,len(self.data)-i-1):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
        return self.data




