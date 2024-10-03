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
for j := 0; j < n; j++ {
swappedString += string(result[j])
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
inputString := "K Positions"
swappedString := swapFirstAndLast(inputString)
fmt.Println("Original String:", inputString)
fmt.Println("Swapped String:", swappedString)
}
