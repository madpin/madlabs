package main

import (
	"fmt"
)

func main() {
	v := "hello"
	f(*v)
	fmt.Println(v)
}

func f(n &string) {
	// fmt.Println("v", v)
	fmt.Println("n", n)
	// fmt.Println(n)
	// fmt.Println(*n)
	// *v = "ted"
	// fmt.Println(*n)
	// fmt.Println(v)
}
