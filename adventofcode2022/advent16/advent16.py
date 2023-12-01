# Advent of code 2022, day 16
import networkx as nx

# open file
# input = open("advent16_input.txt", "r")
input = open("advent16_test_input.txt", "r")

input_array = []
# read string into array
for line in input:
    input_array.append(line)

def part1():

    flow_rates = {}
    connected_to = {}

    for input_line in input_array:
        splitspace = input_line.split(" ")

        valve = splitspace[1]

        flow_rates[valve] = int(splitspace[4][5:-1])

        connected_to[valve] = []
        for n in range(9, len(splitspace)):
             connected_to[valve].append(splitspace[n][:-1])

    print(flow_rates)
    print(connected_to)

    graph = nx.Graph()
    nonz_flows = {}

    for node in flow_rates.keys():
        graph.add_node(node)
        for conn_node in connected_to[node]:
            graph.add_edge(node, conn_node, weight=1.0)

        if flow_rates[node] == 0:
            nonz_flows[node] = flow_rates[node]

    print(graph)
    shortest_path = dict(nx.all_pairs_shortest_path_length(graph))

    print(shortest_path)

    # print(shortest_path["AA"]["EE"])

    current = "AA"

    # Build all paths that go from AA and include each of the other valves that
    # have a flow rate value?
    # path1 = nx.single_source_dijkstra_path(graph, "AA", cutoff=30)
    #
    # print(path1)

    # print(list(nx.dfs_edges(graph, source="AA", depth_limit=30)))

    minutes = 30
    # open_valves = []

    # states is valve ID, opened valves, pressure
    states = [["AA", [], 0]]

    best = {}

    for minute in range(minutes):
        print(minute, len(states), best)

        # Loop over the current states
        new_states = []
        for valve_id, open_valves, pressure in states:
            key = valve_id
            if key in best and pressure <= best[key]:
                new_states.append([valve_id, open_valves, pressure])
                continue

            # new_states = []

            best[key] = pressure

            flow_rate = flow_rates[valve_id]
            connected = connected_to[valve_id]
            if (valve_id not in open_valves):
                open_valves.append(valve_id)
                new_states.append([valve_id, open_valves, pressure + (flow_rate * (minutes-minute))])
            # else:
            #     new_states.append([valve_id, open_valves, pressure])

            for conn in connected:
                new_states.append([conn, open_valves, pressure])

        states = new_states
        # print("states is now ", states)

    #     # Consider how long it takes to move from current to any other valve
    #     # and the pressure release this would give for the remaining time
    #     # and choose the maximum... unfortunately this doesn't work
    #     minutes_elapsed_this_step = 0
    #     max_pressure = 0
    #     max_pressure_valve = ""
    #     # for valve in flow_rates.keys():
    #     if target not in open_valves:
    #         pressure = flow_rates[target] * (
    #             minutes - (1 + shortest_path[current][target]))
    #         # print("valve ", valve, " will give pressure ", pressure)
    #         if pressure > max_pressure:
    #             max_pressure = pressure
    #             max_pressure_valve = target
    #
    #     # Go to max_pressure_valve and open it
    #     if max_pressure > 0:
    #         print("max from current ", current, " is ", max_pressure_valve)
    #         minute += shortest_path[current][max_pressure_valve] + 1
    #         minutes_elapsed_this_step += shortest_path[current][max_pressure_valve] + 1
    #         current = max_pressure_valve
    #         open_valves.append(max_pressure_valve)
    #         open_minute[max_pressure_valve] = minute
    #     else:
    #         minute += 1
    #         minutes_elapsed_this_step += 1
    #
    #
    # for open_valve in open_valves:
    #     total_pressure += (flow_rates[open_valve] * (minutes - open_minute[open_valve]))

    answer = max(pressure for _, _, pressure in states)

    return answer

def part2():

    answer = 0

    return answer

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())
