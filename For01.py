import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    k = 0
    list1=[]
    while k<n:
        list1=list1+[k+1]
        k+=1
    return list1
print(main(5))