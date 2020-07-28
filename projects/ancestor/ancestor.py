'''
   10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
'''
def parentLen (ancestors, starting_node, generation = 0):
    round = 0
    for a in ancestors:
        if a[1] == starting_node and round == 0:
            generation +=1
            round = 1
            return parentLen(ancestors, a[0], generation)
    return generation 

def earliest_ancestor(ancestors, starting_node, queue=[-1]):
    parent = 0
    found = 0
    for a in ancestors:
        if a[1] == starting_node:
            queue.append(a[0])
            parent = 1
    if parent == 0 and len(queue) == 1:
        return queue[0]
    elif parent == 0 and len(queue) == 2:
        if queue[0] < queue[1]:
            return queue[0]
        else:
            return queue[1]
    elif len(queue) > 1:
        queue.pop(0)
        if len(queue) > 1:
            # Helper function to get longest chain of parents between two parents
            if parentLen(ancestors, queue[0]) > parentLen(ancestors, queue[1]):
                queue.pop(1)
                return earliest_ancestor(ancestors, queue[0], queue)
            elif parentLen(ancestors, queue[0]) == parentLen(ancestors, queue[1]) and parentLen(ancestors,queue[0]) == 0:
                if queue[0] < queue[1]:
                    return queue[0]
                else:
                    return queue[1]
            else:
                queue.pop(0)
                return earliest_ancestor(ancestors, queue[1], queue)
        else:
            return earliest_ancestor(ancestors, queue[0], queue)
    else:
        return queue


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 1))
# print(earliest_ancestor(test_ancestors, 2))
# print(earliest_ancestor(test_ancestors, 3))
# print(earliest_ancestor(test_ancestors, 4))
# print(earliest_ancestor(test_ancestors, 5))
# print(earliest_ancestor(test_ancestors, 6))
# print(earliest_ancestor(test_ancestors, 7))
# print(earliest_ancestor(test_ancestors, 8))
# print(earliest_ancestor(test_ancestors, 9))
# print(earliest_ancestor(test_ancestors, 10))
# print(earliest_ancestor(test_ancestors, 11))

