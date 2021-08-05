from Data_Structures.MinHeap import MinHeap


class HeapSort:
    def __init__(self, data: list = None) -> None:
        if data is None:
            raise TypeError("data cannot be None")
        self.data: list = data

    def sort(self) -> list:
        minHeap = MinHeap()
        for item in self.data:
            minHeap.insert(item)
        result = []
        item = minHeap.extract_min()
        while item:
            result.append(item)
            item = minHeap.extract_min()
        return result
