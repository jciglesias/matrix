def __repr__(self) -> str:
    """Print dev version"""
    return f"{type(self).__name__}.data({self.data})"
def __str__(self) -> str:
    strm = "["
    for row in range(self.shape[0]):
        for column in range(self.shape[1]):
            if column == 0:
                strm += "["
            if len(f"{self.data[row][column]} ") > 6:
                strm += f"{self.data[row][column]:.5f} "
            else:
                strm += f"{self.data[row][column]} "
            if column == (self.shape[1]-1) and row != (self.shape[0] - 1):
                strm += "]\n "
        if row == (self.shape[0] - 1):
            strm += "]]"
    return strm
    # return f"{type(self).__name__}({self.data})"