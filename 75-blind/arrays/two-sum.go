// https://leetcode.com/problems/two-sum/

package main

func twoSum(nums []int, target int) []int {
	partials := map[int]int{}
	for index, num := range nums {
		p, ok := partials[num]
		if ok {
			return []int{p, index}
		} else {
			partialSum := target - num
			partials[partialSum] = index
		}
	}
	return []int{}
}
