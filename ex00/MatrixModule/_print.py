def __repr__(self) -> str:
    """Print dev version"""
    return f"{type(self).__name__}.data({self.data})"
def __str__(self) -> str:
    return f"{type(self).__name__}({self.data})"