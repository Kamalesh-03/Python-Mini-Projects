class Tourist:
    def information(self):
        print("tourist place")


class TirunelveliTown(Tourist):
    def information(self):
        print("tirunelvelitown - nellaiyappar temple, iruttu kadai, and etc...")


class Courtallam(Tourist):
    def information(self):
        print("courtallam - falls, mountains, and etc...")


class JohnCollege(Tourist):
    def information(self):
        print("johncollege - studies, job fairs, culturals and etc...")


class Porunai(Tourist):
    def information(self):
        print("porunai - old age weapons, money, and etc...")


class Kalakaddam(Tourist):
    def information(self):
        print("kalakaddam - natural spots, scenic view and etc...")


while True:
    place = input("enter place: ").strip().lower()

    match place:
        case "tirunelvelitown":
            TirunelveliTown().information()
        case "courtallam":
            Courtallam().information()
        case "johncollege":
            JohnCollege().information()
        case "porunai":
            Porunai().information()
        case "kalakaddam":
            Kalakaddam().information()
        case "exit":
            print("program ended")
            break
        case _:
            print("place not available")
