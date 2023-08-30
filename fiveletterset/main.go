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

	fmt.Println(get_distinct_words(all_words, 5))
}

func get_distinct_words(all_words []string, n int) []string {
	return helper(all_words, n)
}

func string_to_set(s string) map[int32]bool {
	output := make(map[int32]bool)
	for _, letter := range s {
		output[letter] = true
	}
	return output
}

func word_shares_letters(word string, letters map[int32]bool) bool {
	for _, ch := range word {
		if _, exists := letters[ch]; exists {
			return true
		}
	}
	return false
}

func helper(allowable_words []string, depth int) []string {
	fmt.Println(len(allowable_words))
	// while the current picked word is less than len of allowable word
	for i := 0; i < len(allowable_words); i++ {
		i_discard := i + 1
		// pick the first word that is not discarded
		current_word := allowable_words[i]
		// move all words that share letters to the left
		current_letters := string_to_set(current_word)
		for j := i + 1; j < len(allowable_words); j++ {
			if word_shares_letters(allowable_words[j], current_letters) {
				allowable_words[j], allowable_words[i_discard] = allowable_words[i_discard], allowable_words[j]
				i_discard++
			}
		}
		// if there are still words to the right,
		if i_discard < len(allowable_words) {
			// end if we've reached sufficient depth
			if depth == 1 {
				output := make([]string, 0)
				return append(output, current_word)
			} else {
				// pass slice with pointer starting where words are allowed, recursively
				output := helper(allowable_words[i_discard:], depth-1)
				// If the output is not None, break and return the result with chosen word added to picked_words
				if output != nil {
					return append(output, current_word)
				}
			}
		}
	}
	return nil
}
