RED = 0
BLACK = 1


def _left_rotate(tree, x):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x
    y.parent = x.parent
    if not x.parent:
        tree.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    return x, y


def _right_rotate(tree, x):
    y = x.left
    x.left = y.right
    if y.right:
        y.right.parent = x
    y.parent = x.parent
    if not x.parent:
        tree.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y
    return x, y


def _left(x):
    return x.left if x else None


def _right(x):
    return x.right if x else None


def _parent(x):
    return x.parent if x else None


def _color(x):
    return x.color if x else BLACK


def _set_color(x, c):
    if x:
        x.color = c


def _height(x):
    return x.height if x else 0
