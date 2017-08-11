import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    # Make a random walk
    rw = RandomWalk(num_points=5000)
    rw.fill_walk()
    plt.figure(dpi=180, figsize=(14,6.5))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, edgecolor='none', c=point_numbers, cmap=plt.cm.rainbow, s=30)

    # Emphasis the first and last points
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='black', edgecolor='none', s=100)
    plt.axis('off')
    plt.savefig('random_walk.png')

    status = input("Make another walk?[y/n] ")
    if status == 'n':
        break
