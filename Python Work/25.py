
import sys

handle = sys.argv[1]


f = open(handle, "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

def long(mat, bbb=''):
    if (len(mat) == 0):
        return bbb

    elif (len(bbb) == 0):
        bbb = mat.pop(0)
        return long(mat, bbb)

    else:
        for i in range(len(mat)):
            a = mat[i]
            for j in range(len(a) // 2):
                c = len(a) - j
                if bbb.startswith(a[j:]):
                    mat.pop(i)
                    return long(mat, a[:j] + bbb)
                if bbb.endswith(a[:c]):
                    mat.pop(i)
                    return long(mat, bbb + a[c:])
print(long(mat))