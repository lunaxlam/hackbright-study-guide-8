"""Tree class and tree node class."""


class Node:
    """Node in a tree. Represents a member of a hierarchy, such as an employee within an org chart. Children of a node could be employees that the parent node, employee, supervises."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    def get_num_children(self):
        """Get number of children.

        For example::

            >>> a = Node("A", [Node("B"), Node("C")])
            >>> a.get_num_children()
            2
        """

        # FIXME

        pass


class Tree:
    """Tree. Helpful to keep track of hierarchical structures, such as a company org chart."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def depth_first_search(self, data):
        """Return node object with this data, traversing the tree depth-first.

        Start at the root, and return None if not found.

        Remember: depth-first is Stack structure, so LIFO (the last thing added is the first thing being examined).
        """

        to_visit = [self.root]

        while to_visit:
            node = to_visit.pop()

            if node.data == data:
                return node

            to_visit.extend(node.children)

    def breadth_first_search(self, data):
        """Return node object with this data, traversing the tree breadth-first.

        Start here (on this node), and return None if not found.

        Remember: breadth-first is Queue structure, so FIFO (the first thing added is the first thing being examined).

        Let's make a tree where we have two "B" nodes, but where one is far down an
        earlier branch and the other is higher-up in an earlier branch. Since this is
        a BFS, we should find the b2 node for "B"::

                       A
                     /   \
                    C     E
                   /       \
                  D        B2
                 /
                B1

            >>> a = Node("A")
            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> c = Node("C")
            >>> d = Node("D")
            >>> e = Node("E")
            >>> a.children = [c, e]
            >>> c.children = [d]
            >>> d.children = [b1]
            >>> e.children = [b2]
            >>> tree = Tree(a)

            >>> tree.breadth_first_search("B") is b2
            True

        """

        to_visit = [self.root]

        while to_visit:
            # Set the node we are looking at to the node at index 0; the first node
            node = to_visit.pop(0)

            if node.data == data:
                return node

            to_visit.extend(node.children)


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
