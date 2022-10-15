from graph import build_from, nodes_according_to, Graph

__to_r = {'a': 240, 'b': 186, 'c': 182, 'd': 163, 'e': 170, 'f': 150,
          'g': 165, 'h': 139, 'i': 120, 'j': 130, 'k': 122, 'l': 104,
          'm': 100, 'n':  77, 'o':  72, 'p':  65, 'q':  65, 'r':   0}  # As the heuristic function.


def cheapest_from(nodes) -> str:
    cheapest = ('a', __to_r['a'])  # Initialized with dummy value.

    for node in nodes:
        if __to_r[node] < cheapest[1]:
            cheapest = (node, __to_r[node])

    return cheapest[0]  # Returns only its label. As long as it's the cheapest, it's value doesn't matter.


def make_path(came_from, current) -> list:
    """:returns: a list, from start to finish, with all nodes that were passed through in the way."""
    path = [current]

    while current in came_from.keys():
        current = came_from[current]
        path.append(current)

    return path[::-1]  # We must revert its order to ensure it will deliver the result from start..finish.


def a_star(start, goal, relations: Graph) -> list:
    unseen = {start}
    came_from = dict()

    score = nodes_according_to(len(__to_r))
    score = {label: float('INF') for label in score.keys()}
    score[start] = 0

    combination = nodes_according_to(len(__to_r))
    combination = {label: float('INF') for label in combination.keys()}
    combination[start] = __to_r[start]

    while unseen:
        current = cheapest_from(unseen)

        if current == goal:
            return make_path(came_from, current)

        unseen -= {current}

        for neighbor, distance in relations.nodes[current].items():
            tentative = score[current] + distance

            if tentative < score[neighbor]:
                came_from[neighbor] = current
                score[neighbor] = tentative
                combination[neighbor] = tentative + __to_r[neighbor]

                unseen |= {neighbor}

    return list()  # As none ways were found.


if __name__ == '__main__':
    graph = build_from('resources/routes.txt')
    print(a_star('a', 'r', graph))
