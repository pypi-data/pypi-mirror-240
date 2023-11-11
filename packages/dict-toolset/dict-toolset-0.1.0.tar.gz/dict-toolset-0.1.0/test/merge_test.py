import unittest

from dict_toolset import merge


class MergeTest(unittest.TestCase):

    def test_c1(self):
        data_1 = {
            "test": "sadhsdha",
            "wann": {
                "name": "kann",
                "index": "sad"
            }
        }
        data_2 = {
            "test": "sadhsdha",
            "wann": {
                "name": "kann2",
                "wisch": "adhsjhkdjkasjkd"
            }
        }

        merge(data_1, data_2)
        print(data_2)

    def test_c2(self):
        data_1 = [
            "name"
            "wann"
        ]

        data_2 = [
            "test",
            "wann",
            "wink"
        ]

        merge(data_1, data_2)
        print(data_2)