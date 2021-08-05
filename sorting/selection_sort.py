class SelectionSort:
    def __init__(self, data: list=None) -> None:
        if data is None:
            raise TypeError("data cannot be None")
        self.data: list = data

    def sort(self) -> list:
        for i in range( len(self.data)-1):
            min=i
            for j in range(i+1,len(self.data)):
                if self.data[j] < self.data[min]:
                    min=j
            if self.data[min]<self.data[i]:
                self.data[i], self.data[min] = self.data[min], self.data[i]
        return self.data


