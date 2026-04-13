import unittest

# Assuming your function looks something like this:
def categorize_age(age):
    if 0 <= age <= 9:
        return "child"
    elif 10 <= age <= 19:
        return "adolescent"
    elif 20 <= age <= 64:
        return "adult"
    return "unknown"

class TestSubtestAge(unittest.TestCase):

    def test_child_range(self):
        for age in range(10):
            with self.subTest(age=age):
                print(f"{age} is considered as a child.")
                self.assertEqual(categorize_age(age), "child")
        print("--------------------------------------------------------")

    def test_adolescent_range(self):
        for age in range(10, 20):
            with self.subTest(age=age):
                print(f"{age} is considered as an adolescent.")
                self.assertEqual(categorize_age(age), "adolescent")
        print("--------------------------------------------------------")

    def test_adult_range(self):
        for age in range(20, 26):
            with self.subTest(age=age):
                print(f"{age} is considered as an adult.")
                self.assertEqual(categorize_age(age), "adult")
        print("--------------------------------------------------------")

if __name__ == '__main__':
    unittest.main()