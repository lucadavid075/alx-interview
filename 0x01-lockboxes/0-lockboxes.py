#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        curr_box = stack.pop()

        for key in boxes[curr_box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)
    return all(visited) or n == 0
