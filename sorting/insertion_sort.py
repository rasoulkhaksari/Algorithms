class InsertionSort:
    def __init__(self, data: list=None) -> None:
        if data is None:
            raise TypeError("data cannot be None")
        self.data: list = data

    def sort(self) -> list:
        for i in range(1, len(self.data)):
            for j in range(i):
                if self.data[i] < self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
        return self.data


# # iso = InsertionSort([4,2,5,7])
# iso = InsertionSort([4])
# print(iso.sort())
