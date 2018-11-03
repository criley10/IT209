#--------------------------------------------------------------------------
# IT209_085.py - General Ticket superclass, NatsTick and Flight subclasses.
# Demonstrates inheritance.
#
# Gene Shuman       10/08/2018
#-------------------------------------------------------------------------
class Ticket(object):    # superclass
    """ Ticket Class - getSerial, toString methods """
   
    def __init__(self, event, name, date, agent):
        self.event = event
        self.cust_name = name
        self.date = date
        self.agent = agent
        
    def getAgent(self):     # Accessor method  
        return self.agent

    def __str__(self):
        return ('Event: ' + self.event + '\ncustomer: ' + self.cust_name +
                '\ndate: ' + self.date + '\nAgent: ' + self.agent)


class NatsTick(Ticket):    # subclass
    """ NatsTick Class - inherits from Ticket superclass"""
    ticketCount = 0             # counts tickets as they are created
    def __init__(self, event, name, date, agent, venue, opponent):
        super().__init__(event, name, date, agent)
        NatsTick.ticketCount += 1
        self.serialNumber = NatsTick.ticketCount 
        self.venue = venue
        self.opponent = opponent
                
    def getSerial(self):     # Accessor method  
        return self.serialNumber

    def getOpponent(self):   # Accessor specific to NatsTick 
        return self.opponent

    def __str__(self):
        return ((super().__str__( )) + '\nvenue: ' + self.venue +
                '  versus: ' + self.opponent + '\nTicket number: ' +
                str(self.serialNumber))
                      

class FlightTick(Ticket):    # subclass
    """ FlightTick Class - inherits from Ticket superclass"""
    ticketCount = 0             # counts tickets as they are created
    def __init__(self, event, name, date, agent, airport, destination, dep):
        super().__init__(event, name, date, agent)
        FlightTick.ticketCount += 1
        self.serialNumber = FlightTick.ticketCount 
        self.airport = airport
        self.destination = destination
        self.departureTime = dep
                
    def getSerial(self):     # Accessor method  
        return self.serialNumber

    def getAirport(self):    # Accessor method specific to FlightTick
        return self.airport

    def __str__(self):
        return ((super().__str__( )) + '\nFrom: ' + self.airport +
                '  to: ' + self.destination + '\nDeparting: ' +
                self.departureTime + '\nTicket number: ' +
                str(self.serialNumber))

nt1 = NatsTick('ballgame', 'GRS', 'April 1, 2018', 'MRizzo', 'Nats Park', 'Mets')
ft1 = FlightTick('Flight', 'Anthony', 'February 27, 2018', 'ElizabethR',
                 'Washington Dulles(IAD)', 'San Francisco','7:15 pm')

print('\nNats Ticket list, object "nt1": ')
print(nt1)

print('\nflight ticket list, object "ft1": ')
print(ft1)

input('\nIs "type(nt1) == NatsTick" true?')
print ((type(nt1) == NatsTick))
input('\nIs "isinstance(ft1, FlightTick)" true?')
print(isinstance(ft1, FlightTick))
input('\nIs "isinstance(nt1, FlightTick)" true?')
print(isinstance(nt1, FlightTick))
input('\nIs "type(ft1) == NatsTick" true? ')
print((type(ft1) == NatsTick))
input('\nIs "isinstance(nt1, Ticket)" true? ')
print(isinstance(nt1, Ticket))      
input('\nIs "type(ft1) == Ticket" true?')
print((type(ft1) == Ticket))
input('\nIs "isinstance(ft1, Ticket)" true?')
print(isinstance(ft1, Ticket))
input('\nIs "isinstance(nt1, Ticket)" true?')
print(isinstance(nt1, Ticket)) 
input('\nHit "Enter" to end Ticket super/subclass demo')





        
       
