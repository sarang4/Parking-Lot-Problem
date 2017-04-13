
class PSlot(object):
    """
    This is class which represents parking slot and
    operation related to it.
    """

    def __init__(self):
        self._car = None
        self._slot_no = None
        self._available = None

    @property
    def car(self):
        return self._reg_no

    @car.setter
    def car(self, value):
        self._car = value

    @property
    def slot_no(self):
        return self._slot_no

    @slot_no.setter
    def slot_no(self, value):
        self._slot_no = value

    @property
    def available(self):
        return self._slot_no

    @available.setter
    def available(self, value):
        self._available = value



