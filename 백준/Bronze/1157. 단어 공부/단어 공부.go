package main

import (
	"fmt"
	"unicode"
)

func main() {
	var inputVal string
	var countArr [26]int
	var maxVal, maxCount, index int

	fmt.Scan(&inputVal)
	
	for _, v := range inputVal {
		conVal := unicode.ToUpper(v)
		countArr[conVal-'A']++
	}
	for i := 0; i < 26; i++ {
		if countArr[i] > maxVal {
			maxVal = countArr[i]
			index = i
		}
	}
	for i := 0; i < 26; i++ {
		if countArr[i] == maxVal {
			maxCount++
		}
	}
	if maxCount > 1 {
		fmt.Print("?")
	} else {
		fmt.Printf("%c", index+65)
	}

}