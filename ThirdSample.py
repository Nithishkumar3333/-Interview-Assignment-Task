package main

import (
    "fmt"
)

func swapFirstAndLast(s string) string {
    n := 0
    for range s {
        n++
    }
    if n <= 1 { 
        return s
    }

    result := make([]byte, n)
    result[0] = s[n-1]  
    result[n-1] = s[0]  
    copyMiddleCharacters(s, result, 1, n-2)

    swappedString := ""
    i := 0
    for ; i < n; i++ { 
        swappedString += string(result[i]) 
    }
    return swappedString
}

func copyMiddleCharacters(s string, result []byte, index, limit int) {
    if index > limit {
        return
    }
    result[index] = s[index]
    copyMiddleCharacters(s, result, index+1, limit)
}

func main() {
    testStrings := []string{
        "K Positions",
    }

    for _, s := range testStrings {
        swappedString := swapFirstAndLast(s)
        fmt.Printf("Original String: %q, Swapped String: %q\n", s, swappedString)
    }
}
