#Write a program to sort the elements of an array using Bucket Sort.
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Determine minimum and maximum values
    min_value = min(arr)
    max_value = max(arr)

    # Create buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for i in range(len(arr)):
        index = int((arr[i] - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(arr[i])

    # Sort each bucket and concatenate the result
    sorted_array = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_array.extend(bucket)

    return sorted_array

# Example usage
if __name__ == "__main__":
    array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Original array:", array)
    sorted_array = bucket_sort(array)
    print("Sorted array:", sorted_array)
