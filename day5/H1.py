 # Accept a Number from the user and find the next possible smallest number which is bigger than the given number having all the digits of the given number  

def next_bigger_number(num):
    digits = list(str(num))
    n = len(digits)

    # Step 1: Find pivot (from right)
    for i in range(n-2, -1, -1):
        if digits[i] < digits[i+1]:
            break
    else:
        return "Not possible"

    # Step 2: Find smallest digit bigger than digits[i] on right
    pivot = i
    for j in range(n-1, pivot, -1):
        if digits[j] > digits[pivot]:
            # Step 3: Swap
            digits[pivot], digits[j] = digits[j], digits[pivot]
            break

    # Step 4: Reverse/sort the right side
    digits[pivot+1:] = sorted(digits[pivot+1:])

    return int("".join(digits))


# 🔎 Examples
print(next_bigger_number(218765))  # 251678
print(next_bigger_number(1234))    # 1243
print(next_bigger_number(4321))    # Not possible
print(next_bigger_number(534976))  # 536479

