#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [];

    things = {};

    start = 0;

    index = 0;

    for t in tickets:
        if t.source == 'NONE':
            start = index;
        else:
            index += 1;
            things[t.source] = t.destination; 

    dest = tickets[start].destination;

    while dest != 'NONE':
        print(dest);
        route.append(dest);
        dest = things[dest];

    route.append('NONE');

    print(route);

    return route;

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3));