class Parking():

    def __init__(self):
        self.tickets = list(range(1, 11))
        self.parkingSpaces = list(range(1, 11))
        self.currentTicket = {}

    def takeTicket(self):
        if self.parkingSpaces and self.tickets:
            ticket = self.tickets.pop(0)
            self.parkingSpaces.pop(0)
            self.currentTicket[ticket] = {"paid": False}
            print(f"Your ticket number is {ticket}.")
            print(f"Spaces left: {self.parkingSpaces}")
            print(f"Tickets left: {self.tickets}")
        else:
            print("The garage is full.")
            
    def payForParking(self):
        ticket = int(input('Enter your ticket number: '))
        if ticket in self.currentTicket and not self.currentTicket[ticket]["paid"]:
            payment = input("Enter the payment amount: ")
            if payment:
                self.currentTicket[ticket]["paid"] = True
                print("Status: PAID. You have 15 minutes")
            else:
                print("Payment is required.")

        elif ticket in self.currentTicket and self.currentTicket[ticket]["paid"]:
            print("this ticket has been paid.")
        else:
            print("Invalid ticket number.")
                
    def leaveGarage(self):
        ticket = int(input('Enter your ticket number: '))
        if ticket in self.currentTicket:
            if self.currentTicket[ticket]["paid"]:
                print("Thank you have a nice day!")
                del self.currentTicket[ticket]
                self.parkingSpaces.append(ticket)
                self.parkingSpaces.sort()
                self.tickets.append(ticket)
                self.tickets.sort()
            else:
                print("Please pay before leaving")
                self.payForParking()
                if self.currentTicket[ticket]["paid"]:
                    print("Thank you have a nice day!")
                    del self.currentTicket[ticket]
                    self.parkingSpaces.append(ticket)
                    self.parkingSpaces.sort()
                    self.tickets.append(ticket)
                    self.tickets.sort()
                    print(f"Spaces left: {self.parkingSpaces}")
                    print(f"Tickets left: {self.tickets}")
        else:
            print("Invalid ticket number.")
                        

    def park(self):
        while True:
            select = input("would you like to park/pay/exit or quit ? ").lower()
            if select == 'park':
                self.takeTicket()
            elif select == 'pay':
                self.payForParking()
            elif select == 'exit':
                self.leaveGarage()
            elif select == 'quit':
                break
            else:
                print("would you like to park/pay/exit or quit ? ").lower()

car1 = Parking()
car1.park()