class BinarySearch:
    def __init__(self, data: list) -> None:
        self.data: list = sorted(data)

    def find(self, target) -> int:
        left, right = 0, len(self.data)-1
        while left <= right:
            mid = (left+right)//2
            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1
