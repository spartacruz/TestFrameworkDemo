import softest


class Utilities(softest.TestCase):
    def assertListItemText(self, list, value):

        for stop in list:
            print("The text is: " + stop.text)

            try:
                self.soft_assert(self.assertEqual, stop.text, value)
            except AssertionError:
                pass

            # try:
            #     assert stop.text == value
            # except AssertionError:
            #     pass

            if stop.text == value:
                print("Test Passed")
            else:
                print("Test Failed")