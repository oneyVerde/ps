package main

import "fmt"

func main() {
	var h, m int
	fmt.Scan(&h, &m)
	if m < 45 {
		h--
	}
	h += 24
	m += 60
	fmt.Print(h%24, (m-45)%60)
}