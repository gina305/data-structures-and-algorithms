# Code Challenge 06: Linked List Insertions

A singly linked list is a set of connected nodes, linked in one direction. Each Node can only see the next node in the list.

## Challenge
Extend a Linked List to allow various insertion methods.

## Approach & Efficiency
Big O(n) as the list gets longer it will take longer to search as you must iterate over each item. Big O(1) adding a node one at a time.

## How it works
* append
  * arguments: new value
  * adds a new node with the given value to the end of the list

* insert before
  * arguments: value, new value
  * adds a new node with the given new value immediately before the first node that has the value specified

* insert after
  * arguments: value, new value
  * adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process ->
![Linked List Insertions](./White%20Board.png)