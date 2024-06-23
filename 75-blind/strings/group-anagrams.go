// https://leetcode.com/problems/group-anagrams/

package main

import (
	"crypto/md5"
	"fmt"
	"sort"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	var uniqueSignatures map[string][]string = make(map[string][]string, len(strs))
	for _, s := range strs {
		sign := signature(s)
		uniqueSignatures[sign] = append(uniqueSignatures[sign], s)
	}
	var result [][]string
	for _, val := range uniqueSignatures {
		result = append(result, val)
	}
	return result
}

func signature(str string) string {
	chars := strings.Split(str, "")
	sort.Strings(chars)
	str = strings.Join(chars, "")
	hasher := md5.New()
	hasher.Write([]byte(str))
	return fmt.Sprintf("%x", hasher.Sum(nil))
}
