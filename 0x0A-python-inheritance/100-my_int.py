#!/usr/bin/python3
"""Module with MyInt class rebel integer
    """


class MyInt(int):
    """MyInt Class has == and != operators inverted
    Arguments:
        int {[int]} -- Parent Class
    """

    def __eq__(self, num):
        """Equivalent method
        Arguments:
            num {[int]} -- integer to compare
        Returns:
            [bool] -- Inverted operator
        """
        return int(self) != int(num)

    def __ne__(self, num):
        """Non equivalent method
        Arguments:
            num {[int]} -- integer to compare
        Returns:
            [bool] -- Inverted operator
        """
        return int(self) == int(num)
