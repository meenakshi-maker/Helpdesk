class Ticket:
    ticket_count = 2000
    tickets_resolved = 0
    tickets_to_solve = 0

    def __init__(self, ticket_creator, staff_id, email_address, description):
        Ticket.ticket_count += 1
 #----------- Assign ticket attributes--------------
        self.ticket_number = Ticket.ticket_count
        self.ticket_creator = ticket_creator
        self.staff_id = staff_id
        self.email_address = email_address
        self.description = description
        self.response = ""
        self.status = True
        Ticket.tickets_to_solve += 1

    def generate_password(self):
        new_password = " "
        # first two characters of staff_id
        new_password = self.staff_id[0:2]

        # + first 3 characters of staff_name
        new_password += self.ticket_creator[0:3]
        return new_password

    def resolve_ticket(self, response):
        self.response = response
        self.status = True
        Ticket.tickets_resolved += 1
        Ticket.tickets_to_solve -= 1

    def display_ticket(self):
 #----------->>>>>>>>>>> print ticket info<<<<<<<<<<<<<-----------
        print(f"Ticket Number:, {self.ticket_number}\n"
             f"Ticket Creator: {self.ticket_creator}\n"
             f"Staff ID:, {self.staff_id}\n"
             f"Email Address:, {self.email_address}\n"
             f"Description:, {self.description}\n"
             f"Response:, {self.response}\n"
             f"Ticket Status:, {self.status}\n")



