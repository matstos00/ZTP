import unittest
import numpy as np
from model import Model

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        self.gray_image = np.random.rand(100, 100) * 255
        self.color_image = np.random.rand(100, 100, 3) * 255

    def test_svd_compression_gray(self):
        compressed = self.model.svd_compression(self.gray_image, 'L', 10)
        self.assertEqual(compressed.shape, self.gray_image.shape)

    def test_svd_compression_color(self):
        compressed = self.model.svd_compression(self.color_image, 'RGB', 10)
        self.assertEqual(compressed.shape, self.color_image.shape)

