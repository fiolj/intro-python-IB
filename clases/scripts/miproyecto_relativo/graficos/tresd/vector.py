import matplotlib.pyplot as plt

def plot_vector(vector):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Extracting coordinates from the vector
    x, y, z = vector

    # Plotting the vector
    ax.quiver(0, 0, 0, x, y, z, color='r', label='Vector')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Vector')

    # Set equal aspect ratio
    ax.set_box_aspect([1,1,1])

    # Show legend
    ax.legend()

    # Show plot
    plt.show()
