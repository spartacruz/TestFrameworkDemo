import softest


class Utilities(softest.TestCase):
    def assertListItemText(self, list, value):

        for stop in list:
            print("The text is: " + stop.text)

            self.soft_assert(self.assertEqual, stop.text, value)
            # assert stop.text == value
            # print("assert pass")

            if stop.text == value:
                print("Test Passed")
            else:
                print("Test Failed")