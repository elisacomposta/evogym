import numpy as np
import math


class Grid():
    """
    Grid object to create map plot
    """

    def __init__(self, shape=[10, 10], feature1_domain=[0., 1.], feature2_domain=[0., 1.]):
        self.grid = np.zeros(shape)

        self.shape = shape
        self.feature1_domain = feature1_domain
        self.feature2_domain = feature2_domain

        self.step_0 = (feature1_domain[1] - feature1_domain[0]) / shape[0]
        self.step_1 = (feature2_domain[1] - feature2_domain[0]) / shape[1]


    def get_pos(self, feature_x, feature_y):
        """
        Args:       computed features values
        Returns:    position in the grid where the features are mapped
        """
        x = math.floor( feature_x / self.step_0)
        if x >= self.shape[0]:
            x = self.shape[0] - 1

        y = math.floor( feature_y / self.step_1)
        if y >= self.shape[1]:
            y = self.shape[1] - 1

        return x, y

    def insert(self, el, x, y):
        """
        Insert element 'el' in grid at pos ('x', 'y')
        """
        self.grid[x][y] = el

    def increment(self, x, y):
        """
        Increment value of element at pos ('x', 'y')
        """
        self.grid[x][y] += 1

    