class Table:
    def __init__(self):
        self.table = [[str(i*j) for i in range(1000)] for j in range(1000)]
    
    def get(self, x, y) -> str:
        return self.table[x][y]
    
    def getMx() -> int:
        pass

    def getMy() -> int:
        pass