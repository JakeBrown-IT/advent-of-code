# QUICKSORT IMPLEMENTATION
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def main():
    # vars
    i = 0
    total = 0
    left = []
    right = []

    # split data from file into two lists
    with open("data.txt", 'r') as file:
        for line in file:
            nums = [int(num) for num in line.split() if num.strip()]
            left.append(nums[0])
            right.append(nums[1])

    # sort lists using quicksort
    quicksort(left, 0, len(left) - 1)
    quicksort(right, 0, len(right) - 1)

    # sum up absolute differences and display
    while i < len(left):
        total += abs(left[i] - right[i])
        i += 1
    
    print(total)


if __name__ == "__main__":
    main()

