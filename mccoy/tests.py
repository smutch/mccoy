from phytest import Alignment, Sequence, Tree


def test_alignment(alignment: Alignment):
    """
    Write alignment tests here.

    For example:
        alignment.assert_length(34)

    See docs for more information.
    https://phytest-devs.github.io/phytest/reference.html#alignment
    """
    pass


def test_sequence(sequence: Sequence):
    """
    Write sequence tests here.

    For example:
        sequence.assert_count_gaps(0)

    See docs for more information.
    https://phytest-devs.github.io/phytest/reference.html#sequence
    """
    pass


def test_tree(tree: Tree):
    """
    Write tree tests here.

    For example:
        tree.assert_is_bifurcating()

    See docs for more information.
    https://phytest-devs.github.io/phytest/reference.html#tree
    """
    pass


def test_root_to_tip(tree: Tree):
    """
    Test the tree for temporal signal with a root-to-tip regression.
    https://phytest-devs.github.io/phytest/reference.html#phytest.bio.tree.Tree.assert_root_to_tip
    """
    tree.assert_root_to_tip(min_r_squared=0)
