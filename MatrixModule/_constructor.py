def initMatrix(self, arg):
        """Init with a tuple or a list of lists"""
        if isinstance(arg, list):
            if not arg or not len(arg) or not isinstance(arg[0], list):
                raise TypeError("Argument must be a list of lists")
            self.data = arg
            self.shape = (len(arg), len(arg[0]))
            for row in self.data:
                if not isinstance(row, list):
                    raise TypeError("Argument must be a list of lists")
                if len(row) != self.shape[1]:
                    raise TypeError("Bad dimentions for matrix")
        elif isinstance(arg, tuple):
            self.shape = arg
            self.data = []
            for i in range(self.shape[0]):
                self.data.append([])
                for j in range(self.shape[1]):
                    self.data[i].append(0)
        else:
            raise TypeError("Argument must be of type List of Lists or tuple.")
        