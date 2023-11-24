import os
from MatrixModule import Matrix
from projection import projection


if __name__=="__main__":
    fd = open("proj", "w")
    mat = projection(1,1,1,1)
    strm = ""
    for row in range(mat.shape[0]):
        for column in range(mat.shape[1]):
            strm += str(mat[row][column])
            if column != (mat.shape[1] - 1):
                strm += ", "
            else:
                strm += "\n"
    fd.write(strm)
    # os.system("matrix_display/display")