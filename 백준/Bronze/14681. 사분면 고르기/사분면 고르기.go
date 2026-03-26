package main

import "fmt"

func calc(a int, b int) (result int) {
	result = 0
	if a*b > 0 {
		if a > 0 {
			result = 1
		} else {
			result = 3
		}
	} else {
		if a > 0 {
			result = 4
		} else {
			result = 2
		}
	}
	return
}

func main() {
	var x, y int
	fmt.Scan(&x, &y)
	fmt.Print(calc(x, y))
}