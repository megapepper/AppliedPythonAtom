#!/usr/bin/env python
# coding: utf-8


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    # TODO: реализовать функцию
    if head is None:
        return None
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next_node
        curr.next_node = prev
        prev = curr
        curr = next_node
    head = prev
    return head
