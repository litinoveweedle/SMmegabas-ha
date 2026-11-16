"""Adapt Building Automation driver operations."""

import megabas


def __getattr__(name):
    return getattr(megabas, name)


def set_contact_count_edge(stack, channel, edge):
    """Clear old edge bits before applying the driver's new edge selection."""
    if edge not in (0, 1, 2, 3):
        raise ValueError("Invalid contact counter edge")
    current = megabas.getContactCountEdge(stack, channel)
    if current == edge:
        return
    if current & ~edge:
        megabas.setContactCountEdge(stack, channel, 0)
    if edge:
        megabas.setContactCountEdge(stack, channel, edge)
