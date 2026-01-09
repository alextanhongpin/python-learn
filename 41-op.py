class Where:
    def __init__(self, field):
        self.field = field
        self.value = None

    def __eq__(self, other):
        """
        Defines the behavior for the '==' operator (Equality).
        """
        print('eql', other)
        self.value = other
        return self

    def __str__(self):
        return f"{self.field} = {self.value}"

res = Where("myfield") == 2
print(res.field, res.value)
print(str(res))
print(res)
