#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    flights = {}
    for ticket in tickets:
        flights[ticket.source] = ticket.destination

    route = []
    next_flight = flights['NONE']

    while next_flight != 'NONE':
        route.append(next_flight)
        next_flight = flights[next_flight]
        if next_flight == 'NONE':
            # Add the final NONE for some reason...
            route.append(next_flight)

    return route
