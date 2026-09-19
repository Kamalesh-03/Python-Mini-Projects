class Cash:
    def payment(self):
        print("Payment made through Cash")


class UPI:
    def payment(self):
        print("Payment made through UPI")


class Card:
    def payment(self):
        print("Payment made through Card")


class NetBanking:
    def payment(self):
        print("Payment made through NetBanking")


class Wallet:
    def payment(self):
        print("Payment made through Wallet")


choice = input("Enter payment method: ")

match choice:
    case "Cash":
        Cash = Cash()
        Cash.payment()

    case "UPI":
        UPI = UPI()
        UPI.payment()

    case "Card":
        Card = Card()
        Card.payment()

    case "NetBanking":
        NetBanking = NetBanking()
        NetBanking.payment()

    case "Wallet":
        Wallet = Wallet()
        Wallet.payment()

    case _:
        print("Invalid payment method")