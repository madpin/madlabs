package main

import (
	"fmt"
	"time"
)

var soup = [4][4]string{
	[4]string{"M", "A", "S", "C"},
	[4]string{"O", "M", "D", "B"},
	[4]string{"G", "Y", "I", "R"},
	[4]string{"O", "W", "R", "E"}}

// var soup = [2][2]string{
// 	[2]string{"M", "A"},
// 	[2]string{"O", "M"}}

var lines int = len(soup)
var col int = len(soup[0])

var words_list = []string{"MOM", "MO", "AMDBR", "MAS"}

var found_words []string

func stringInSlice(a string, list []string) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

func word_from_0(x int, y int, previous_string string, used_x []int, used_y []int) int {
	if x >= lines || x < 0 {
		return 0
	}

	if y >= col || y < 0 {
		return 0
	}

	if len(used_x) == len(used_y) {
		for u := 0; u < len(used_x); u++ {
			if used_x[u] == x && used_y[u] == y {
				return 2
			}
		}
	} else {
		panic("Different Len's between x and y")
	}
	current_string := previous_string + soup[x][y]
	// fmt.Println(current_string)

	if stringInSlice(current_string, words_list) {
		found_words = append(found_words, current_string)
	}

	used_x = append(used_x, x)
	used_y = append(used_y, y)

	new_used_x := make([]int, len(used_x))
	new_used_y := make([]int, len(used_y))

	copy(new_used_x, used_x)
	copy(new_used_y, used_y)

	word_from_0(x, y+1, current_string, new_used_x, new_used_y)
	word_from_0(x+1, y, current_string, new_used_x, new_used_y)
	word_from_0(x+1, y+1, current_string, new_used_x, new_used_y)

	word_from_0(x, y-1, current_string, new_used_x, new_used_y)
	word_from_0(x-1, y, current_string, new_used_x, new_used_y)
	word_from_0(x-1, y-1, current_string, new_used_x, new_used_y)

	word_from_0(x+1, y-1, current_string, new_used_x, new_used_y)
	word_from_0(x-1, y+1, current_string, new_used_x, new_used_y)

	return 0
}

func main() {
	start := time.Now()
	for i := 0; i < lines; i++ {
		for j := 0; j < col; j++ {

			word_from_0(i, j, "", []int{}, []int{})
		}
	}
	duration := time.Since(start)
	fmt.Printf("Total time: %v\n", duration.Seconds())

	fmt.Println("###")
	fmt.Println(found_words)
}
