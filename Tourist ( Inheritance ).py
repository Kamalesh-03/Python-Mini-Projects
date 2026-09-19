class tourist:
    def information(self):
        print("tourist place")

class tirunelvelitown(tourist):
    def information(self):
        print("tirunelvelitown - nellaiyappar temple, iruttu kadai, and etc...")

class courtallam(tourist):
    def information(self):
        print("courtallam - falls, mountains, and etc...")

class johncollege(tourist):
    def information(self):
        print("johncollege - studies, job fairs, culturals and etc...")

class porunai(tourist):
    def information(self):
        print("porunai - old age weapons, money, and etc...")

class kalakad(tourist):
    def information(self):
        print("kalakaddam - natural spots, scenic view and etc...")

while True:

    place = input("enter place: ")

    match place:
        case "tirunelvelitown":
            tirunelvelitown().information()

        case "courtallam":
            courtallam().information()

        case "johncollege":
            johncollege().information()

        case "porunai":
            porunai().information()

        case "kalakaddam":
            kalakaddam().information()

        case "exit":
            print("program ended")
            break

        case _:
            print("place not available")