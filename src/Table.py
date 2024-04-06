class Table:
    def __init__(self, __sizeX, __sizeY):
        self.sizeX = __sizeX
        self.sizeY = __sizeY
        self.table = [[str(i*j) for i in range(self.sizeX)] for j in range(self.sizeY)]
    
    def get(self, x, y) -> str:
        return self.table[x][y]
    
    def getMx() -> int:
        pass

    def getMy() -> int:
        pass