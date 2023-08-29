package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	// open file
	f, err := os.Open("/home/fhui/Playplace/fiveletterset/fiveletterset.txt")
	if err != nil {
		log.Fatal(err)
	}
	// remember to close the file at the end of the program
	defer f.Close()

	// read the file line by line using scanner
	scanner := bufio.NewScanner(f)
	all_words := make([]string, 0)
	for scanner.Scan() {
		// do something with a line
		all_words = append(all_words, scanner.Text())
	}
	fmt.Println(len(all_words))

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

func get_distinct_words(all_words []string, n int) []string {

}

func helper(allowable_words []string, picked_words []string, depth int) []string {
	// pick a word
	// move all words that share letters to the left
	// if there are still words to the right,
	// pass slice with pointer starting where words are allowed, recursively
	// otherwise, move word to the left, pick another word and start again
}
