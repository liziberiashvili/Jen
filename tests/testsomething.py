import random


class VolumeController:

    def raise_volume(self):
        minimal_value = 0
        maximal_value = 100
        random_value = random.randint(minimal_value, maximal_value)
        print(random_value)

        action = str(input("raise volume or dicrease volume?"))
        number = int(input("how many times?"))
        if action == "raise":
            raise_volume = number * 15
            random_value += raise_volume
        else:
            dicrease_volume = number * 15
            random_value -= dicrease_volume

        if random_value > maximal_value:
            random_value = maximal_value
        elif random_value < minimal_value:
            random_value = minimal_value


        print(random_value)





volume_controll = VolumeController()
volume_controll.raise_volume()
