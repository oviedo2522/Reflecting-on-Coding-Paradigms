class Podracer():
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def condition(self, condition):
        if condition in ['perfect', 'trashed', 'repaired']:
            self.condition = condition

    def repair(self):
        if self.condition == 'trashed':
            self.condition = 'repaired'
        else:
            print("No repair needed")


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self):
        if self.condition == 'perfect':
            self.condition = 'trashed'



podracer = Podracer(500, 'perfect', 1000)
print(podracer.condition)
podracer.repair()
print(podracer.condition)

anakins_pod = AnakinsPod(500, 'perfect', 1000)
print(anakins_pod.max_speed)
anakins_pod.boost()
print(anakins_pod.max_speed)

third_pod = SebulbasPod(500, 'perfect', 400)
print(third_pod.condition)
third_pod.flame_jet()
print(third_pod.condition)
third_pod.repair()
print(third_pod.condition)