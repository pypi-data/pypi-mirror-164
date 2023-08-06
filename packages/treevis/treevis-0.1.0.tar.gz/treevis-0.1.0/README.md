# treevis
A library for displaying binary trees in plain text.

## Features
- No tree implementation is provided. The library accepts any object that conforms to the node interface.
- Automatically calculates margins
- Can display multiple trees side-by-side like this: 
    ```
             _____7_______                            _____7_______
            /             \                          /             \
         __3_          ___17______                __3_          ___19___
        /    \        /           \              /    \        /        \
       1      5      11          _25            1      5      11       _25
      / \    / \    /  \        /   \          / \    / \    /  \     /   \
     0   2  4   6  9   15     _20   27        0   2  4   6  9   15   20   27
                             /
                            19
    ```
- Supports node coloring.

## Usage

Implement a tree node and construct a tree in any way you prefer.
A tree node must have `value`, `left`, `right` as its properties.

Optionally you may use a `color` property to assign a color to a node. Should be useful when working with Red-Black trees, and in general when it is needed to mark certain nodes with colors. Color must be an integer in range 0 - 255. For convenience there are pre-defined colors in the library.

```
class Node:
    def __init__(self, value, left, right, color=None):
        self.value = value
        self.left = left
        self.right = right
        self.color = color
```


Call draw function on the root node.
```
from treevis import draw, Colors
from node import Node # your node implementation

root = Node(5, Node(2, color=Colors.Red), Node(7, color=Colors.Gray), color=Colors.Blue)

draw(root)
```

Observe the result in terminal.
```
    5
   / \
  4   3

```

`draw` function accepts any number of root nodes. 
If multiple tree nodes are passed to `draw` function, the trees will be displayed side-by-side:

```
draw(root, root, root)
```

would result in:
```
    5      5      5
   / \    / \    / \
  4   3  4   3  4   3
```
