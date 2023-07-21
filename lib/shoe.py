class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._condition = "New"

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        self._brand = value

    brand = property(get_brand, set_brand)

    def get_size(self):
        return self._size

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    size = property(get_size, set_size)

    def get_condition(self):
        return self._condition

    def set_condition(self, value):
        self._condition = value

    condition = property(get_condition, set_condition)

    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")