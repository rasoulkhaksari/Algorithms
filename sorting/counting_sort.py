
class CountingSort:
    def __init__(self,data:list) -> None:
        if data is None:
            raise TypeError("data cannot be None")
        self.data:list=data

    def sort(self):
        if len(self.data)==0:
            return []

        max_element = int(max(self.data))
        min_element = int(min(self.data))
        range_of_elements = max_element - min_element + 1
        count_arr = [0 for _ in range(range_of_elements)]
        output_arr = [0 for _ in range(len(self.data))]
        for i in range(0, len(self.data)):
            count_arr[self.data[i]-min_element] += 1
    
        # actual position of this element in output array
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1]
    
        # Build the output character array
        for i in range(len(self.data)-1, -1, -1):
            output_arr[count_arr[self.data[i] - min_element] - 1] = self.data[i]
            count_arr[self.data[i] - min_element] -= 1
    
        return output_arr



