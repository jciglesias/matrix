def __repr__(self) -> str:
    """Print dev version"""
    return f"{type(self).__name__}.data({self.data})"
def __str__(self) -> str:
    strm = "["
    for row in range(self.shape[0]):
        if row < (self.shape[0] - 1):
            strm += f"{self.data[row]}\n"
        else:
            strm += f"{self.data[row]}]"
    # return f"{type(self).__name__}({self.data})"
    return strm