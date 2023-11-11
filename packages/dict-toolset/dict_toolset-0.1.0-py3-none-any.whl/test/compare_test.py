from datetime import datetime
import os
import sys
import unittest

from dict_toolset import compare
from dict_toolset._compare import DifferenceType, DifferencePointer


class CompareTest(unittest.TestCase):

    def print_result(self, result):
        for entry in result:
            print(entry)

    def test_c1(self):
        data_1 = {
            "name": "Supi",
            "sub": {
                "name": "SupiSub"
            }
        }
        data_2 = {
            "name": "Supi",
            "sub": {
                "name": "SupiSub",
                "content": "Sdjjahsdh"
            }
        }

        result = list(compare(data_1, data_2))

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].type, DifferenceType.MISSING)
        self.assertEqual(result[0].pointer, DifferencePointer.A)

    def test_c2(self):
        data_1 = {
            "name": "Supi",
            "subs": [
                "str"
            ]
        }
        data_2 = {
            "name": "Supi",
            "subs": [
                "str",
                "duf"
            ]
        }

    def test_c3(self):
        data_1 = [
            {
                "id": "djajshd",
                "name": "supi",
                "kacki": "dsadasdasd"
            }
        ]
        data_2 = [
            {
                "id": "djajshd",
                "name": "supi",
                "kacki": "dsadasdasd"
            },
            {
                "id": "sdajsjdhas",
                "name": "supi2",
                "kacki": "dsad2asdasdd"
            },
        ]

        self.print_result(list(compare(data_1, data_2)))
        