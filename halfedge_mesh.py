import config
import math

# TODO: Reorder functions


class HalfedgeMesh:

    def __init__(self, filename=None, vertices=[], halfedges=[], facets=[]):
        """Make an empty halfedge mesh.

           filename   - a string that holds the directory location and name of
               the mesh
            vertices  - a list of Vertex types
            halfedges - a list of HalfEdge types
            facets    - a list of Facet types
        """

        self.vertices = vertices
        self.halfedges = halfedges
        self.facets = facets
        # dictionary of all the edges given indexes
        # TODO: Figure out if I need halfedges or if I should just use edges
        # Which is faster?
        self.edges = None

        if filename:
            self.vertices, self.halfedges, self.facets, self.edges = \
                self.read_file(filename)

    def __eq__(self, other):
        # TODO: Test
        return self.vertices == other.vertices and \
            self.halfedges == other.halfedges and \
            self.facets == other.facet

    def __hash__(self):
        return hash(self.vertices) ^ hash(self.halfedges) ^ hash(self.facets) ^ \
            hash((self.vertices, self.halfedges, self.facets))

    def read_file(self, filename):
        """Determine the type of file and use the appropriate parser.

        Returns a HalfedgeMesh
        """
        try:
            with open(filename, 'r') as file:

                first_line = file.readline().strip()

                # TODO: build OBJ, PLY parsers
                parser_dispatcher = {"OFF": self.parse_off(file),
                                     "PLY": None,
                                     "OBJ": None}

                return parser_dispatcher[first_line]

        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)

    def read_off_vertices(self, file_object, number_vertices):
        """Read each line of the file_object and return a list of Vertex types.
        The list will be as [V1, V2, ..., Vn] for n vertices

        Return a list of vertices.
        """
        vertices = []

        # Read all the vertices in
        for index in range(number_vertices):
            line = file_object.readline().split()

            # convert strings to floats
            line = map(float, line)
            vertices.append(Vertex(line[0], line[1], line[2], index))

        return vertices

    def parse_build_halfedge_off(self, file_object, number_facets, vertices):
        """Link to the code:
        http://stackoverflow.com/questions/15365471/initializing-half-edge-
        data-structure-from-vertices

        Pseudo code:
        map< pair<unsigned int, unsigned int>, HalfEdge* > Edges;

        for each face F
        {
            for each edge (u,v) of F
            {
                Edges[ pair(u,v) ] = new HalfEdge();
                Edges[ pair(u,v) ]->face = F;
            }
            for each edge (u,v) of F
            {
                set Edges[ pair(u,v) ]->nextHalfEdge to next half-edge in F
                if ( Edges.find( pair(v,u) ) != Edges.end() )
                {
                    Edges[ pair(u,v) ]->oppositeHalfEdge = Edges[ pair(v,u) ];
                    Edges[ pair(v,u) ]->oppositeHalfEdge = Edges[ pair(u,v) ];
            }
        }

        """
        Edges = {}
        facets = []

        # For each facet
        for index in range(number_facets):
            line = file_object.readline().split()

            # convert strings to ints
            line = map(int, line)

            # TODO: make general to support non-triangular meshes
            # Facets vertices are in counter-clockwise order
            facet = Facet(line[1], line[2], line[3], index)
            facets.append(facet)

            # create pairing of vertices for example if the vertices are
            # verts = [1,2,3] then zip(verts, verts[1:]) = [(1,2),(2,3)]
            # note: we skip line[0] because it represents the number of vertices
            # in the facet.
            all_facet_edges = zip(line[1:], line[2:])
            all_facet_edges.append((line[3], line[1]))

            # For every halfedge around the facet
            for i in range(3):
                Edges[all_facet_edges[i]] = Halfedge()
                Edges[all_facet_edges[i]].facet = facet
                Edges[all_facet_edges[i]].vertex = vertices[
                    all_facet_edges[i][1]]

            facet.halfedge = Edges[all_facet_edges[0]]

            for i in range(3):
                Edges[all_facet_edges[i]].next = Edges[
                    all_facet_edges[(i + 1) % 3]]
                Edges[all_facet_edges[i]].prev = Edges[
                    all_facet_edges[(i - 1) % 3]]

                # reverse edge ordering of vertex, e.g. (1,2)->(2,1)
                if all_facet_edges[i][2::-1] in Edges:
                    Edges[all_facet_edges[i]].opposite = \
                        Edges[all_facet_edges[i][2::-1]]

                    Edges[all_facet_edges[i][2::-1]].opposite = \
                        Edges[all_facet_edges[i]]

        return facets, Edges

    def parse_off(self, file_object):
        """Parses OFF files

        Returns a HalfedgeMesh
        """
        facets, halfedges, vertices = [], [], []

        vertices_faces_edges_counts = map(int, file_object.readline().split())

        number_vertices = vertices_faces_edges_counts[0]
        vertices = self.read_off_vertices(file_object, number_vertices)

        number_facets = vertices_faces_edges_counts[1]
        facets, Edges = self.parse_build_halfedge_off(file_object,
                                                      number_facets, vertices)

        for key, value in Edges.iteritems():
            halfedges.append(value)

        return vertices, halfedges, facets, Edges

    def get_halfedge(self, u, v):
        """Retrieve halfedge with starting vertex u and target vertex v

        u - starting vertex
        v - target vertex

        Returns a halfedge
        """
        return self.edges[(u, v)]


class Vertex:

    def __init__(self, x=0, y=0, z=0, index=None):
        """Create a vertex with given index at given point.

        x     - x-coordinate of the point
        y     - y-coordinate of the point
        z     - z-coordinate of the point
        index - integer index of this vertex
        """

        self.x = x
        self.y = y
        self.z = z

        self.index = index

    def __eq__(x, y):
        return x.__key() == y.__key() and type(x) == type(y)

    def __key(self):
        return (self.x, self.y, self.z, self.index)

    def __hash__(self):
        return hash(self.__key())

    def get_vertex(self):
        return [self.x, self.y, self.z]


class Facet:

    def __init__(self, a=-1, b=-1, c=-1, index=None, halfedge=None):
        """Create a facet with the given index with three vertices.

        a, b, c - indices for the vertices in the facet, counter clockwise.
        index - index of facet in the mesh
        halfedge - a Halfedge that belongs to the facet
        """
        self.a = a
        self.b = b
        self.c = c
        self.index = index
        # halfedge going ccw around this facet.
        self.halfedge = halfedge

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c \
            and self.index == other.index and self.halfedge == other.halfedge

    def __hash__(self):
        return hash(self.halfedge) ^ hash(self.a) ^ hash(self.b) ^ \
            hash(self.c) ^ hash(self.index) ^ \
            hash((self.halfedges, self.a, self.b, self.c, self.index))

    def get_normal(self):
        """Calculate the normal of facet

        Return a python list that contains the normal
        """
        vertex_a = [self.halfedge.vertex.x, self.halfedge.vertex.y,
                    self.halfedge.vertex.z]

        vertex_b = [self.halfedge.next.vertex.x, self.halfedge.next.vertex.y,
                    self.halfedge.next.vertex.z]

        vertex_c = [self.halfedge.prev.vertex.x, self.halfedge.prev.vertex.y,
                    self.halfedge.prev.vertex.z]

        # create edge 1 with vector difference
        edge1 = [u - v for u, v in zip(vertex_b, vertex_a)]
        # create edge 2 ...
        edge2 = [u - v for u, v in zip(vertex_c, vertex_b)]
        # cross product
        normal = cross_product(edge1, edge2)

        normal = normalize(normal)

        return normal


class Halfedge:

    def __init__(self, next=None, opposite=None, prev=None, vertex=None,
                 facet=None):
        """Create a halfedge with given index.
        """
        self.opposite = opposite
        self.next = next
        self.prev = prev
        self.vertex = vertex
        self.facet = facet

    def __eq__(self, other):
        # TODO Test more
        return (self.vertex == other.vertex) and \
               (self.prev.vertex == other.prev.vertex)

    def __hash__(self):
        return hash(self.opposite) ^ hash(self.next) ^ hash(self.prev) ^ \
            hash(self.vertex) ^ hash(self.facet) ^ hash((self.opposite,
                                                         self.next,
                                                         self.prev,
                                                         self.vertex,
                                                         self.facet))

    # TODO: test convex
    def get_angle_normal(self):
        """Calculate the angle between the normals that neighbor the edge.

        Return an angle in radians
        """
        a = self.facet.get_normal()
        b = self.opposite.facet.get_normal()

        dir = [self.vertex.x - self.prev.vertex.x,
               self.vertex.y - self.prev.vertex.y,
               self.vertex.z - self.prev.vertex.z]
        dir = normalize(dir)

        ab = dot(a, b)
        args = ab / (norm(a) * norm(b))

        if allclose(args, 1):
            args = 1
        elif allclose(args, -1):
            args = -1

        assert (args <= 1.0 and args >= -1.0)

        angle = math.acos(args)

        if not (angle % math.pi == 0):
            e = cross_product(a, b)
            e = normalize(e)

            vec = dir
            vec = normalize(vec)

            if (allclose(vec, e)):
                return angle
            else:
                return -angle
        else:
            return 0


def allclose(v1, v2):
    """Compare if v1 and v2 are close

    v1, v2 - any numerical type or list/tuple of numerical types

    Return bool if vectors are close, up to some epsilon specified in config.py
    """

    v1 = make_iterable(v1)
    v2 = make_iterable(v2)

    elementwise_compare = map(
        (lambda x, y: abs(x - y) < config.EPSILON), v1, v2)
    return reduce((lambda x, y: x and y), elementwise_compare)


def make_iterable(obj):
    """Check if obj is iterable, if not return an iterable with obj inside it.
    Otherwise just return obj.

    obj - any type

    Return an iterable
    """
    try:
        iter(obj)
    except:
        return [obj]
    else:
        return obj


def dot(v1, v2):
    """Dot product(inner product) of v1 and v2

    v1, v2 - python list

    Return v1 dot v2
    """
    elementwise_multiply = map((lambda x, y: x * y), v1, v2)
    return reduce((lambda x, y: x + y), elementwise_multiply)


def norm(vec):
    """ Return the Euclidean norm of a 3d vector.

    vec - a 3d vector expressed as a list of 3 floats.
    """
    return math.sqrt(reduce((lambda x, y: x + y * y), vec, 0.0))


def normalize(vec):
    """Normalize a vector

    vec - python list

    Return normalized vector
    """
    if norm(vec) < 1e-6:
        return [0 for i in range(len(vec))]
    return map(lambda x: x / norm(vec), vec)


def cross_product(v1, v2):
    """ Return the cross product of v1, v2.

    v1, v2 - 3d vector expressed as a list of 3 floats.
    """
    x3 = v1[1] * v2[2] - v2[1] * v1[2]
    y3 = -(v1[0] * v2[2] - v2[0] * v1[2])
    z3 = v1[0] * v2[1] - v2[0] * v1[1]
    return [x3, y3, z3]

def create_vector(p1, p2):
    """Contruct a vector going from p1 to p2.

    p1, p2 - python list wth coordinates [x,y,z].

    Return a list [x,y,z] for the coordinates of vector
    """ 
    return map((lambda x,y: x-y), p2, p1)
