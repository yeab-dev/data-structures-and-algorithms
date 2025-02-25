class NumberContainers:

    def __init__(self):
        self.number_map = collections.defaultdict(SortedSet)
        self.index_map = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            self.number_map[old_number].remove(index)
            if not self.number_map[old_number]:
                del self.number_map[old_number]

        self.index_map[index] = number
        self.number_map[number].add(index)

    def find(self, number: int) -> int:
        if number in self.number_map and self.number_map[number]:
            return self.number_map[number][0]
        return -1
