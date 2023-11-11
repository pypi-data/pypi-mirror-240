import unittest

from dict_toolset import flat, unflat


class FlatTest(unittest.TestCase):
    
    def test_c1(self):

        test_value = {
            "name": {
                "vorname": "George",
                "nachname": "Haddad"
            },
            "eigenschaften": {
                "alter": 36
            },
            "plad": [
                {
                    "id": "num",
                    "wann": "djashd"
                },
                "win"
            ]
        }

        flatten = list(flat(test_value))

        unflatten = unflat(flatten)

        print(unflatten)
        


        
