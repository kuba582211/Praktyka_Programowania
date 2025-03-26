import unittest

def Add(number):
    if number == "":
        return 0
    if number.endswith(",") or number.endswith("\n"):
        raise(ValueError)

    d = [",","\n"]
    for d in d:
        number = number.replace(d," ")
    return sum(map(int,number.split()))

class Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""),0)

    def test_one(self):
        self.assertEqual(Add("-1"),-1)
        self.assertEqual(Add("49"),49)

    def test_two(self):
        self.assertEqual(Add("1,2"),3)
        self.assertEqual(Add("-1,1"),0)

    def test_multiple(self):
        self.assertEqual(Add("1,2,3,4"),10)
        self.assertEqual(Add("-1,-1,-3,2"),-3)

    def test_n(self):
        self.assertEqual(Add("1\n2"),3)
        self.assertEqual(Add("-1\n2,0\n12"),13)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Add("1,")
        with self.assertRaises(ValueError):
            Add("2,3,4\n")
        with self.assertRaises(ValueError):
            Add("\n")
        with self.assertRaises(ValueError):
            Add(",")