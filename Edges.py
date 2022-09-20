# Not sure if edges should be a class

# Algo to draw edges from adjacency matrix
# going through whole matrix draws double lines since
# graph is undirected
# go though half the matrix
# for i in range(0, m * n):
#   for j in range(i, m * n):
#       if 1 draw line from i to j
#       then hold that edge in an array, like vertices
#       this would really only be to change the color so show the path