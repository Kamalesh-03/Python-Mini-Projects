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
        print("Payment made through Net Banking")


class Wallet:
    def payment(self):
        print("Payment made through Wallet")


choice = input("Enter payment method: ").lower()

match choice:
    case "cash":
        cash = Cash()
        cash.payment()

    case "upi":
        upi = UPI()
        upi.payment()

    case "card":
        card = Card()
        card.payment()

    case "net banking":
        netbanking = NetBanking()
        netbanking.payment()

    case "wallet":
        wallet = Wallet()
        wallet.payment()

    case _:
        print("Invalid payment method")