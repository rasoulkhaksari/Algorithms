
class QuickSort:
    def __init__(self, data: list) -> None:
        if data is None:
            raise TypeError("data cannot be None")
        self.data: list = data

    def sort(self, data: list = None):
        if data is None:
            data = self.data
        if len(data) < 2:
            return data
        equal, left, right = [], [], []
        pivot_index = len(data)//2
        pivot_value = data[pivot_index]
        for item in data:
            if item == pivot_value:
                equal.append(item)
            elif item < pivot_value:
                left.append(item)
            else:
                right.append(item)
        return self.sort(left)+equal+self.sort(right)

    def partition(self, start, end):
        pivot_index = start
        pivot = self.data[pivot_index]
        while start < end:
            # Increment the start pointer till it finds an element greater than  pivot
            while start < len(self.data) and self.data[start] <= pivot:
                start += 1
            # Decrement the end pointer till it finds an element less than pivot
            while self.data[end] > pivot:
                end -= 1
            # If start and end have not crossed each other, swap the numbers on start and end
            if start < end:
                self.data[start], self.data[end] = self.data[end], self.data[start]
        # Swap pivot element with element on end pointer. This puts pivot on its correct sorted place.
        self.data[end], self.data[pivot_index] = self.data[pivot_index], self.data[end]
        return end

    def sort_v2(self, start, end):
        if start < end:
            p = self.partition(start, end)
            self.sort_v2(start, p-1)
            self.sort_v2(p+1, end)
        return self.data
