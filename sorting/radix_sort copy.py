
class RadixSort:
    def __init__(self,data:list) -> None:
        if data is None:
            raise TypeError("data cannot be None")
        self.data:list=data

        


    def _countingSort(self,exp1):

        n = len(self.data)

        # The output array elements that will have sorted arr
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = (self.data[i] / exp1)
            count[int(index % 10)] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = (self.data[i] / exp1)
            output[count[int(index % 10)] - 1] = self.data[i]
            count[int(index % 10)] -= 1
            i -= 1

        # # Copying the output array to arr[],
        # # so that arr now contains sorted numbers
        # i = 0
        # for i in range(0, len(self.data)):
        #     self.data[i] = output[i]
        return output

    # Method to do Radix Sort
    def sort(self):
        if len(self.data)==0:
            return []
        # Find the maximum number to know number of digits
        max1 = max(self.data)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp > 0:
            self._countingSort(exp)
            exp *= 10


rs=RadixSort([2,1])
print(rs.sort())

