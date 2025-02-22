class ProductOfNumbers:
    def __init__(self):
        self.list = []
        self.product = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.list = []
            self.product = 1
        else:
            self.product *= num
            self.list.append(self.product)

    def getProduct(self, k: int) -> int:
        if len(self.list) < k:
            return 0
        elif len(self.list) == k:
            return self.list[-1]
        else:
            return self.list[-1] // self.list[-k -1]