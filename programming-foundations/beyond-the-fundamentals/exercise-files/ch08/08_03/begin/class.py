class Attendee:
    'common base class for all attendees'

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def dispayAttendee(self):
        print('Name : {}, Tickets : {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))


attendee1 = Attendee('B. Giles', 2)
attendee2 = Attendee('J. Ortega', 1)

attendee1.dispayAttendee()
attendee2.dispayAttendee()

attendee2.addTicket()
attendee2.addTicket()
