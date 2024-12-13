import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

vertices_cube = np.array([
    [-1, 1, 1,-1,-1, 1, 1,-1],
    [-1,-1, 1, 1,-1,-1, 1, 1],
    [-1,-1,-1,-1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1, 1, 1]
])

faces_cube = np.array([
    [0, 1, 5, 4],
    [1, 2, 6, 5],
    [2, 3, 7, 6],
    [3, 0, 4, 7],
    [0, 1, 2, 3],
    [4, 5, 6, 7]
])


def draw_shape(vertices, faces, color):
    vertices = (vertices[:3, :] / vertices[3, :]).T
    ax.add_collection3d(Poly3DCollection(vertices[faces], facecolors=color, edgecolors='k', linewidths=0.2))

if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d', proj_type = 'ortho')
    draw_shape(vertices_cube, faces_cube, 'purple')
    ax.set_box_aspect([1,1,1])
    ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
    ax.view_init(azim=-37.5, elev=30)
    ax.set_xticks(np.linspace(-1, 1, 5)); ax.set_yticks(np.linspace(-1, 1, 5)); ax.set_zticks(np.linspace(-1, 1, 5))

    plt.show()
