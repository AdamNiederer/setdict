class SetDict(dict):
    def copy(self):
        return SetDict(**self)

    def union(self, other):
        return self | other

    def intersection(self, other):
        return self & other

    def symmetric_difference(self, other):
        return self & other

    def difference(self, other):
        return self - other

    def issuperset(self, other):
        return self > other

    def issubset(self, other):
        return self < other

    def __or__(self, other):
        if isinstance(other, set):
            return {key for key in set(self.keys()) | other}
        if isinstance(other, dict):
            return SetDict({key: self.get(key, other.get(key))
                            for key in set(self.keys()) | set(other.keys())})
        return NotImplemented

    def __ror__(self, other):
        return self | other

    def __and__(self, other):
        if isinstance(other, set):
            return SetDict({key: val
                            for key, val in self.items() if key in other})
        if isinstance(other, dict):
            return SetDict({key: val
                            for key, val in self.items() if key in other})
        return NotImplemented

    def __rand__(self, other):
        return self & other

    def __xor__(self, other):
        if isinstance(other, set):
            return {key for key in set(self.keys()) ^ other}
        if isinstance(other, dict):
            return SetDict({key: self.get(key, other.get(key))
                            for key in set(self.keys()) ^ set(other.keys())})
        return NotImplemented

    def __rxor__(self, other):
        return self ^ other

    def __sub__(self, other):
        if isinstance(other, set):
            return SetDict({key: self.get(key)
                            for key in set(self.keys()) - other})
        if isinstance(other, dict):
            return SetDict({key: self.get(key)
                            for key in set(self.keys()) - set(other.keys())})
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, set):
            return {key for key in other - set(self.keys())}
        if isinstance(other, dict):
            return SetDict({key: self.get(key)
                            for key in set(other.keys()) - set(self.keys())})
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, set) or isinstance(other, dict):
            return set(self) < set(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, set) or isinstance(other, dict):
            return set(self) <= set(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, set) or isinstance(other, dict):
            return set(self) > set(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, set) or isinstance(other, dict):
            return set(self) >= set(other)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, dict):
            return dict(self) == other
        if isinstance(other, set):
            return set(self) == other
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, dict):
            return dict(self) == other
        if isinstance(other, set):
            return set(self) == other
        return NotImplemented
