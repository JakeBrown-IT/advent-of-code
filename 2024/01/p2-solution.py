def main():
    # vars
    total = 0
    left = []
    right = []
    frequency = {}

    # split data from file into two lists
    with open("data.txt", 'r') as file:
        for line in file:
            nums = [int(num) for num in line.split() if num.strip()]
            
            if nums[0] not in frequency:
                frequency[nums[0]] = 0

            left.append(nums[0])
            right.append(nums[1])
    
    for i in right:
        if i in frequency:
            frequency[i] += 1

    for j in left:
        if j in frequency:
            total += (j * frequency[j])

    print(total)


if __name__ == "__main__":
    main()

