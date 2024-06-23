// https://leetcode.com/problems/clone-graph/
package main

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

type Node struct {
	Val       int
	Neighbors []*Node
}

func clone(seen map[int]*Node, node *Node) *Node {
	if node == nil {
		return nil
	}

	newNode := &Node{Val: node.Val}
	seen[node.Val] = newNode
	newNode.Neighbors = make([]*Node, len(node.Neighbors))
	for index, neighbor := range node.Neighbors {
		n, isSeen := seen[neighbor.Val]
		if !isSeen {
			n = clone(seen, neighbor)
		}
		newNode.Neighbors[index] = n
	}

	return newNode
}

func cloneGraph(node *Node) *Node {
	var seen map[int]*Node = map[int]*Node{}
	return clone(seen, node)
}
