package main

import "fmt"

func main() {
	var palindrome string
	var flag int = 1
	fmt.Scan(&palindrome)
	for i, _ := range palindrome {
		if palindrome[i] != palindrome[len(palindrome)-i-1] {
			flag = 0
			break
		}
	}
	fmt.Print(flag)
}