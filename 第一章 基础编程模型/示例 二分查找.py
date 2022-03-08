def BinarySearch(arr,guess):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if guess < arr[mid]:
            high = mid - 1
        elif guess > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    num = int(input("请输入你要查询的数字:"))
    res = BinarySearch(arr,num)
    if res == -1:
        print('查无此数！')
    else:
        print('该数字的位置在:{}'.format(res + 1))


