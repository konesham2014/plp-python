class Smartphone:
    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self.battery = battery

    def make_call(self, number):
        if self.battery <= 0:
            print(f"{self.model}: Battery dead! Please charge.")
        else:
            self.battery -= 5
            print(f"{self.model}: Calling {number}... (Battery: {self.battery}%)")

    def charge(self, amount=10):
        self.battery = min(100, self.battery + amount)
        print(f"{self.model}: Charged! Battery now at {self.battery}%.")

    def __str__(self):
        return f"{self.brand} {self.model} (Battery: {self.battery}%)"


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery=100, cooling_system=True):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery <= 0:
            print(f"{self.model}: Battery dead! Can't play {game}.")
        else:
            drain = 20 if self.cooling_system else 30
            self.battery = max(0, self.battery - drain)
            print(f"{self.model}: Playing {game} 🎮 (Battery: {self.battery}%)")

    def charge(self, amount=10):  # Polymorphism
        self.battery = min(100, self.battery + amount * 2)
        print(f"{self.model}: Turbo-charged! Battery now at {self.battery}%.")


# -------------------------
# Interactive menu program
# -------------------------

def main():
    print("📱 Welcome to Smartphone Simulator!")
    phone_type = input("Choose phone type (1=Smartphone, 2=GamingSmartphone): ")

    brand = input("Enter brand: ")
    model = input("Enter model: ")

    if phone_type == "2":
        phone = GamingSmartphone(brand, model)
    else:
        phone = Smartphone(brand, model)

    while True:
        print("\n--- Menu ---")
        print("1. Show phone info")
        print("2. Make a call")
        print("3. Charge phone")
        if isinstance(phone, GamingSmartphone):
            print("4. Play game")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(phone)
        elif choice == "2":
            number = input("Enter number to call: ")
            phone.make_call(number)
        elif choice == "3":
            amt = int(input("Enter amount to charge: "))
            phone.charge(amt)
        elif choice == "4" and isinstance(phone, GamingSmartphone):
            game = input("Enter game name: ")
            phone.play_game(game)
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
