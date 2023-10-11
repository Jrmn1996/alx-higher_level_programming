#!/usr/bin/python3
"""defines pascal_triangle func"""


def pascal_triangle(n):
    """represent pascal triangle of size n
    return a list of lists of int representing the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
