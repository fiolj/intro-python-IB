import numpy as np

def matrix_rotation(angles):
  cx, cy, cz = np.cos(angles)
  sx, sy, sz = np.sin(angles)
  R = np.zeros((3, 3))
  R[0, 0] = cx * cz - sx * cy * sz
  R[0, 1] = cx * sz + sx * cy * cz
  R[0, 2] = sx * sy

  R[1, 0] = -sx * cz - cx * cy * sz
  R[1, 1] = -sx * sz + cx * cy * cz
  R[1, 2] = cx * sy

  R[2, 0] = sy * sz
  R[2, 1] = -sy * cz
  R[2, 2] = cy
  return R


def rotate(angles, v):
  return np.dot(matrix_rotation(angles), v)

