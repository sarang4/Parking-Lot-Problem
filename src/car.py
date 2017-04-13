
class Car(object):
    """
    This is class which represents details of a car.
    """

    def __init__(self):
        self._reg_no = None
        self._color = None

    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

