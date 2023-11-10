import unittest
import numpy as np

from pythonase.general_algorithm import knee_point

# test set obtained from doi:10.1109/BigDataService.2018.00042.
elbow_x = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5,
           1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5,2.6, 2.7, 2.8, 2.9, 3)
elbow_y = (10, 5, 3.33333333333333, 2.5, 2, 1.66666666666667, 1.42857142857143, 1.25, 1.11111111111111,
           1, 0.909090909090909, 0.833333333333333, 0.769230769230769, 0.714285714285714, 0.666666666666667,
           0.625, 0.588235294117647, 0.555555555555555, 0.526315789473684, 0.5, 0.476190476190476, 0.454545454545455,
           0.434782608695652, 0.416666666666667, 0.4, 0.384615384615385, 0.37037037037037, 0.357142857142857,
           0.344827586206896, 0.333333333333333)
knee_x = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7,
          1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3)
knee_y = (-1, -0.698970004336019, -0.522878745280338, -0.397940008672038,
          -0.301029995663981, -0.221848749616356, -0.154901959985743, -0.096910013008056,
          -0.045757490560675, 0, 0.041392685158225, 0.079181246047625, 0.113943352306837,
          0.146128035678238, 0.176091259055681, 0.204119982655925, 0.230448921378274,
          0.255272505103306, 0.278753600952829, 0.301029995663981, 0.322219294733919,
          0.342422680822206, 0.361727836017593, 0.380211241711606, 0.397940008672038,
          0.414973347970818, 0.431363764158987, 0.447158031342219, 0.462397997898956,
          0.477121254719662)


class MengerTestCase(unittest.TestCase):
    def test_knee(self):
        obj = knee_point.Menger()
        x, y = obj.get_knee(X=knee_x, Y=knee_y, is_convex=False)
        self.assertEqual(x, knee_x[28], "Menger Curvature failed on finding knees")

    def test_elbow(self):
        obj = knee_point.Menger()
        x, y = obj.get_knee(X=elbow_x, Y=elbow_y, is_convex=True)
        self.assertEqual(x, elbow_x[9], "Menger Curvature failed on finding elbows")


class LMethodTestCase(unittest.TestCase):
    def test_knee(self):
        obj = knee_point.LMethod()
        x, y = obj.get_knee(X=knee_x, Y=knee_y, is_convex=False)
        self.assertEqual(x, knee_x[8], "L Method failed on finding knees")


class KneedleTestCase(unittest.TestCase):
    def test_knee(self):
        # test case from Satopaa, V., Albrecht, J., Irwin, D. & Raghavan, B.
        # Finding a ‘Kneedle’ in a Haystack: Detecting Knee Points in System Behavior.
        # in 2011 31st International Conference on Distributed Computing Systems Workshops 166–171 (2011).
        # doi:10.1109/ICDCSW.2011.20.
        demo_func = lambda x: -1 / x + 5
        X = np.arange(1, 11)
        Y = np.array(list(map(demo_func, X)))
        obj = knee_point.Kneedle()
        x, y = obj.get_knee(X=X, Y=Y, is_convex=False)
        self.assertEqual(x, 3, "Kneedle Method failed on finding knees")


if __name__ == '__main__':
    unittest.main()
