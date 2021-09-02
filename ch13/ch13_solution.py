from array import array


class ClockFaceTime:
    typecode = "I"

    def __init__(self, components):

        """
        Unimplmented input validations:
        Check that input tuple is length 3
        Check that hour is in range 1-12
        Check that minute is in range 0-59
        Check that second is in range 0-59
        """

        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __str__(self):
        return str(tuple(self))

    def __getitem__(self, index):
        return self._components[index]

    def __eq__(self, other):
        if isinstance(other, ClockFaceTime):
            return all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, ClockFaceTime):
            if self.__convert_hms_to_seconds(self) > self.__convert_hms_to_seconds(other):
                return True
            else:
                return False
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, ClockFaceTime):
            if self.__convert_hms_to_seconds(self) < self.__convert_hms_to_seconds(other):
                return True
            else:
                return False
        else:
            return NotImplemented

    def __ge__(self, other):
        lt_result = self < other
        if lt_result is NotImplemented:
            return NotImplemented
        else:
            return not lt_result

    def __le__(self, other):
        gt_result = self > other
        if gt_result is NotImplemented:
            return NotImplemented
        else:
            return not gt_result

    def __convert_hms_to_seconds(self, hms):
        # Need to account for the fact that the 12-hour clock starts at (12, 0, 0)
        if hms[0] == 12:
            return hms[1]*60 + hms[2]
        else:
            return hms[0]*3600 + hms[1]*60 + hms[2]


class ClockFaceTimeDelta:
    typecode = "i"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __getitem__(self, index):
        return self._components[index]

    def __str__(self):
        return str(tuple(self))

    def __abs__(self):
        return ClockFaceTimeDelta(abs(x) for x in self)

    def __neg__(self):
        return ClockFaceTimeDelta(-x for x in self)

    def __pos__(self):
        return ClockFaceTimeDelta(self)

    def __add__(self, other):
        if isinstance(other, ClockFaceTime):
            pairs = zip(self, other)
            return ClockFaceTime(self.__convert_to_12_hour_clock(tuple(a + b for a, b in pairs)))
        elif isinstance(other, ClockFaceTimeDelta):
            pairs = zip(self, other)
            return ClockFaceTimeDelta(a + b for a, b in pairs)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, ClockFaceTime):
            return self + other
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, ClockFaceTime):
            return -self + other
        else:
            return NotImplemented

    def __mul__(self, scalar):
        return ClockFaceTimeDelta(n * scalar for n in self)

    def __rmul__(self, scalar):
        return self * scalar

    def __eq__(self, other):
        if isinstance(other, ClockFaceTimeDelta):
            return all(a == b for a, b in zip(self, other))
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, ClockFaceTimeDelta):
            if self.__convert_delta_to_seconds(self) > self.__convert_delta_to_seconds(other):
                return True
            else:
                return False
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, ClockFaceTimeDelta):
            if self.__convert_delta_to_seconds(self) < self.__convert_delta_to_seconds(other):
                return True
            else:
                return False
        else:
            return NotImplemented

    def __ge__(self, other):
        lt_result = self < other
        if lt_result is NotImplemented:
            return NotImplemented
        else:
            return not lt_result

    def __le__(self, other):
        gt_result = self > other
        if gt_result is NotImplemented:
            return NotImplemented
        else:
            return not gt_result

    def __convert_to_12_hour_clock(self, raw_hms):
        """
        Convert the result of an addition or subtraction operation back to 12 hour time
        """
        minutes, seconds = divmod(raw_hms[2], 60)
        minutes += raw_hms[1]
        hours, minutes = divmod(minutes, 60)
        hours += raw_hms[0]
        # Hours go from 1-12 so we need to shift it before and after the division
        hours = divmod(hours-1, 12)[1]+1

        return (hours, minutes, seconds)

    def __convert_delta_to_seconds(self, delta):
        return delta[0]*3600 + delta[1]*60 + delta[2]