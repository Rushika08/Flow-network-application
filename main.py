from collections import defaultdict, deque

# Class for implementing the flow network
class FlowNetwork:
    def __init__(self):
        self.graph = defaultdict(lambda: defaultdict(int))
        self.vertices = set()

    def add_edge(self, u, v, capacity):
        self.graph[u][v] += capacity
        self.graph[v][u] += 0  # Reverse edge for residual graph
        self.vertices.add(u)
        self.vertices.add(v)

    def bfs(self, source, sink, parent):
        visited = {node: False for node in self.vertices}
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = {}
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

        return max_flow

# Parse the input file
def parse_input(file_name):
    with open(file_name, 'r') as file:
        data = file.read().splitlines()

    num_people = int(data[0])
    num_committees = int(data[1])

    people = data[2].split()
    committees = data[3].split()

    max_committees = []
    willing_committees = []
    for i in range(num_people):
        line = data[4 + i].split()
        max_committees.append(int(line[0]))
        willing_committees.append(line[1:])

    max_people_per_committee = list(map(int, data[4 + num_people:]))

    return people, committees, max_committees, willing_committees, max_people_per_committee

# Build the flow network and solve the problem
def solve_committee_assignment(input_file):
    people, committees, max_committees, willing_committees, max_people_per_committee = parse_input(input_file)

    source = 's'
    sink = 't'
    flow_network = FlowNetwork()

    # Add edges from source to people with capacity m_i
    for i, person in enumerate(people):
        flow_network.add_edge(source, person, max_committees[i])

    # Add edges from committees to sink with capacity z_i
    for i, committee in enumerate(committees):
        flow_network.add_edge(committee, sink, max_people_per_committee[i])

    # Add edges from people to committees they are willing to join
    for i, person in enumerate(people):
        for committee in willing_committees[i]:
            flow_network.add_edge(person, committee, 1)

    # Find the maximum flow
    total_required_flow = sum(max_people_per_committee)
    max_flow = flow_network.ford_fulkerson(source, sink)

    if max_flow != total_required_flow:
        print("Not Possible")
        return

    # Parse the result to print assignments
    person_to_committee = defaultdict(list)
    committee_to_person = defaultdict(list)

    for person in people:
        for committee in flow_network.graph[person]:
            if committee in committees and flow_network.graph[person][committee] == 0:
                person_to_committee[person].append(committee)
                committee_to_person[committee].append(person)

    print("Person: Committee")
    for person in people:
        print(f"{person} : {' '.join(person_to_committee[person])}")

    print("\nCommittee: Person")
    for committee in committees:
        print(f"{committee} : {' '.join(committee_to_person[committee])}")

# Run the program
if __name__ == "__main__":
    solve_committee_assignment("input.txt")
  
