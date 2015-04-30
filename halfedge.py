import sys


class Vectex:

    def __init__(self, x=0, y=0, z=0, index=None):

        self.x = x
        self.y = y
        self.z = z
        self.index = index

    def set_halfedge():
        None

    def set_point():
        return [self.x, self.y, self.z]


class Halfedge:

    def __init__(self, oppo_h=None, next_h=None, prev_h=None, vetex_h=[], facet_h=None, index=None):

        self.opposite_h = oppo_h
        self.next_h = next_h
        self.prev_h = prev_h
        self.vetex_h = vetex_h
        self.facet_h = facet_h

    def is_border(vetex_h):
        """
        judge whether the vetex_h is border

        """

    def set_next(h1=None, h2=None):
        """
        set h2 to be the next halfedge of h1

        """

    def set_prev(h1=None, h2=None):
        """
        set h2 to be the previous halfedge of h1

        """

    def set_vectex(h=None, v=None):
        """
        set v to be the start point of the halfedge h

        """

    def set_facet(h=None, f=None):
        """
        set facet f to be the face belong to h

        """


class Facet:

    def __init__(self, a, b, c, index=None, halfedge_f=None):
        self.a = a
        self.b = b
        self.c = c
        self.halfedge_f = halfedge_f
        self.index = index

    def set_halfedge(h=None):
        """
        set the halfedge h to belong to facet

        """


class HalfedgeMesh:

    def __init__(self, filename=None, vertices=[], halfedge=[], facets=[]):
        self.vertices = vertices
        self.halfedge = halfedge
        self.facet = facets

        self.edges = None

        if filename:
            self.vertices, self.halfedges, self.facets, self.edge = self.read_file(
                filename)

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                first_line = file.readline.strip()
                paser_dispatcher = {"OFF": self.parse_off(file)}

                return parser_dispatcher[first_line]
            except IOError as e:
        		print "I/O error({0}): {1}".format(e.errno, e.strerror)

    def parse_off(self, file_object):
    	facet, halfedge, vertices = [], [], []

    	vertices_faces_edges_counts = map(int, file_object.readline().split())
    	number_vertices = vertices_faces_edges_counts[0]
    	vertices = read_off_vertices(file_object, number_vertices)

    	number_facets = vertices_faces_edges_counts[1]
    	facets, Edges = parse_build_halfedge_off(
        	file_object, number_facets, vertices)

    	for key, value in Edges.iteritems():
        	halfedge.append(value)

    return vertices, halfedges, facets, Edges

    def read_off_vertices(self, file_object, number_vertices):

        vertices = []

        for index in range(number_vertices):
            line = file_object.readline.split()

            line = map(float, line)
            vertices.append(Vertex(line[0], line[1], line[2], index))

        return vertices

    def parse_build_halfedge_off(self, file_object, number_facets, vertices):
        Edges = {}
        facets = []

        for index in number_facets:
            line = file_object.readline().split()

            line = map(int, line)

            facet = Facet(line[1], line[2], line[3], index)
            facets.append(facet)

            all_facet_edges = zip(line[1:], line[2:])
            all_facet_edges.append((line[3], line[1]))

            for i in range(3):
                Edges[all_facet_edges[i]] = Halfedge()
                Edges[all_facet_edges[i]].facet = facet
                Edges[all_facet_edges[i]].vertex = vertices[
                    all_facet_edges[i][1]]

            facet.halfedge = Edges[all_facet_edges[0]]

            for i in range(3):
                Edges[all_facet_edges[i]].next = Edges[
                    all_facet_edges[i + 1] % 3]
                Edges[all_facet_edges[i]].prev = Edges[
                    all_facet_edges[i - 1] % 3]

                if all_facet_edges[i][2::-1] in Edges:
                    Edges[all_facet_edges[i]].opposite = Edges[
                        all_facet_edges[i][2::-1]]
                    Edges[
                        all_facet_edges[i][2::-1]].opposite = Edges[all_facet_edges[i]]

        return facets, Edges
