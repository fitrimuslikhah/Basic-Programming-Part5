def join_array_remove_duplicate(arrayA, arrayB):
    # your code here
    ans = []
    for data in arrayA:
        if data not in ans :
            ans.append(data)
    for data in arrayB:
        if data not in ans :
            ans.append(data)
    return ans
    

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
