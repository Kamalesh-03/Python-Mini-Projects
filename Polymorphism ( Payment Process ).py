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


choice = input("Enter payment method: ").strip().lower()

match choice:
    case "cash":
        method = Cash()
    case "upi":
        method = UPI()
    case "card":
        method = Card()
    case "netbanking":
        method = NetBanking()
    case "wallet":
        method = Wallet()
    case _:
        method = None

if method:
    method.payment()      # same call, different behaviour: polymorphism
else:
    print("Invalid payment method")
