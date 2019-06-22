class Sum():

    def __init__(self):
        pass

    def sum(self, arr):
        return self.mySum(arr, 0)

    def mySum(self, arr, left):
        if left == len(arr):
            return 0
        return arr[left] + self.mySum(arr, left+1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum = Sum()
    print(sum.sum(arr))
