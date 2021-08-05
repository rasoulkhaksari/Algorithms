class MergeSort:
    def __init__(self, data: list = None) -> None:
        if data is None:
            raise TypeError("data cannot be None")
        self.data: list = data

    def sort(self, data=None) -> list:
        if data is None:
            data = self.data
        if len(data) < 2:
            return data
        mid = len(data)//2
        leftPart = data[:mid]
        rightPart = data[mid:]
        leftPart = self.sort(leftPart)
        rightPart = self.sort(rightPart)
        return self.merge(leftPart, rightPart)

    def merge(self, leftPart, rightPart):
        left, right, result = 0, 0, []
        while left < len(leftPart) and right < len(rightPart):
            if leftPart[left] < rightPart[right]:
                result.append(leftPart[left])
                left += 1
            else:
                result.append(rightPart[right])
                right += 1
        while left < len(leftPart):
            result.append(leftPart[left])
            left += 1
        while right < len(rightPart):
            result.append(rightPart[right])
            right += 1
        return result
