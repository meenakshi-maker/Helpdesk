from Tickets import Ticket
def create_ticket():
 #------->>>>>>>>> prompt the user for ticket info<<<<<<<<<<<<<-----------------
    ticket_creator = input("Enter ticket creator: ")
    staff_id = input("Enter staff ID: ")
    email_address = input("Enter email address: ")
    description = input("Enter description: ")

    ticket = Ticket(ticket_creator, staff_id, email_address, description)
    return ticket

def resolve_ticket(ticket):
    response = input("Enter response: ")
    ticket.resolve_ticket(response)

#------------------ >>>>>>>>>>>>>Menu maker<<<<<<<<<<<<----------------------------------------
def menuLoad(menu):
    count = 1

    for z in menu:
        print(f"{count}. {z}")
        count += 1

    print(f"0. EXIT")

    choice = input("Enter Number: ")

    if choice.isnumeric():
        choice = int(choice)

        if choice in range(0, count):
            answer = choice
        else:
            print("Error: Number out of RANGE.")
            answer = 99
    else:
        print("Error: Input NOT a number.")
        answer = 99

    return answer


tickets = []

while True:
    menu = ["Create Ticket", "Resolve Ticket", "Display Ticket Statistics"]
    choice = menuLoad(menu)

    if choice == 1:
        ticket = create_ticket()
        tickets.append(ticket)
        print("\nTicket created successfully.")

    elif choice == 2:
        ticket_number = int(input("Enter ticket number to resolve: "))
        found = False

        for ticket in tickets:
            if ticket.ticket_number == ticket.ticket_count:
                resolve_ticket(ticket)
                found = True
                print("\nTicket resolved successfully.")
                break

        if not found:
            print("\nTicket number not found.")

    elif choice == 3:
        print("\nTicket number:", 2000+ Ticket.ticket_count)
        print("Tickets Created:", Ticket.ticket_count)
        print("Tickets Resolved:", Ticket.tickets_resolved)
        print("Tickets To Solve:", Ticket.tickets_to_solve)

    elif choice == 0:
        break
#---------------->>>>>>EXIT<<<<<<<<<<<-----------------
    else:
        print("\n Invalid choice")
