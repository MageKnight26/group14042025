class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        if not min_value <= current <= max_value:
            raise ValueError("Початкове значення має бути в межах мінімуму і максимуму")
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if not self.min_value <= start <= self.max_value:
            raise ValueError("Поточне значення має бути в межах мінімуму і максимуму")
        self.current = start

    def set_max(self, max_max):
        if max_max < self.current or max_max < self.min_value:
            raise ValueError("Максимум має бути ≥ поточного значення і мінімуму")
        self.max_value = max_max

    def set_min(self, min_min):
        if min_min > self.current or min_min > self.max_value:
            raise ValueError("Мінімум має бути ≤ поточного значення і максимуму")
        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current -= 1

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, "Test1"
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Досягнуто максимуму
assert counter.get_current() == 10, "Test2"

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, "Test3"
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Досягнуто мінімуму
assert counter.get_current() == 7, "Test4"
