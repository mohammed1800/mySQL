#heap sort
#
class HeapSort:
    def __init__(self):
        self.comparison_count = 0

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparison_count += 1
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            self.comparison_count += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

    def sort_and_count(self, arr):
        self.comparison_count = 0
        self.heap_sort(arr)
        return arr, self.comparison_count

# Example usage:
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    sorter = HeapSort()
    sorted_array, comparisons = sorter.sort_and_count(array)
    print(f"Sorted array: {sorted_array}")
    print(f"Number of comparisons: {comparisons}")
