"""Övningar på ADTn Graph."""


class Node():
    """Implementation av nod. Används tillsammans med `Graph`."""
    def __init__(self, key):
        """Initiera noden med `key` och utan grannar."""
        self.key = key
        self._connections = dict()

    def add_connection(self, neighbor, weight=None):
        """Lägg till en granne med den frivilliga vikten `weight`."""
        self._connections[neighbor] = weight

    def get_connections(self):
        """Returnera en lista med nodens grannar."""
        return self._connections.keys()

    def get_weight(self, neighbor):
        """Returnera vikten hos kanten till grannen `neighbor`."""
        return self._connections[neighbor]

    def __repr__(self):
        """Object representation med `self.key` som identifierar fem första
        neighbors."""

        connections = sorted(self._connections.keys())
        if len(connections) > 5:
            del connections[5:]
            connections.append('...')
        return '<Node: {}: {}>'.format(self.key, ', '.join(connections))


class Graph():
    """Implementation av ADTn Graph."""

    def __init__(self):
        """Initierar `self._nodes`."""
        self._nodes = dict()

    def add_node(self, key):
        """Lägger till en ny nod."""
        self._nodes[key] = Node(key)

    def add_edge(self, start, finish, weight=None):
        self._nodes[start].add_connection(finish, weight)

    def get_node(self, key):
        """Returnerar noden med matchande `key`."""
        return self._nodes[key]

    def get_graph_nodes(self):
        """Returnerar grafens alla noder."""
        return self._nodes.keys()

    def __contains__(self, key):
        """Kontrollera om noden med matchande `key` finns."""
        if key in self._nodes.keys():
            return True
        return False

    def __iter__(self):
        """Gör det enkelt att iterera över grafens alla noder."""
        return iter(self._nodes.values())