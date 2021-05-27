import unittest
from types import SimpleNamespace

from fastai.vision.core import PILImage

from classifier import Classifier
from PIL import Image


class MyTestCase(unittest.TestCase):
    def testYummyImageGreaterThanHalf(self):
        # Arrange:
        classifier = Classifier()
        uploader = SimpleNamespace(data=['yummy.jpg'])
        img = PILImage.create(uploader.data[0])

        # Act:
        is_yummy, result = classifier.isYummy(img)

        # Assert:
        print(result)
        self.assertGreater(result, 0.5)

    def testYummyImageIsYummy(self):
        # Arrange:
        classifier = Classifier()
        uploader = SimpleNamespace(data=['yummy.jpg'])
        img = PILImage.create(uploader.data[0])

        # Act:
        is_yummy, result = classifier.isYummy(img)

        # Assert:
        self.assertTrue(is_yummy)

    def testDisgustingFromPath(self):
        # Arrange:
        classifier = Classifier()
        path = "shitty.png"

        # Act:
        is_yummy, result = classifier.isYummyFromPath(path)

        # Assert:
        self.assertFalse(is_yummy)


if __name__ == '__main__':
    unittest.main()
