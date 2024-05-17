class MergeSort:
    def __init__(self):
        self.comparison_count = 0

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            # Merge the two halves
            while i < len(left_half) and j < len(right_half):
                self.comparison_count += 1
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def sort_and_count(self, arr):
        self.comparison_count = 0
        self.merge_sort(arr)
        return arr, self.comparison_count

# Example usage:
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    sorter = MergeSort()
    sorted_array, comparisons = sorter.sort_and_count(array)
    print(f"Sorted array: {sorted_array}")
    print(f"Number of comparisons: {comparisons}")
