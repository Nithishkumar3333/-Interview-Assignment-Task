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
if n > 2 {
result[1] = s[1]
if n > 3 {
result[2] = s[2]
}
if n > 4 {
result[3] = s[3]
}
if n > 5 {
result[4] = s[4]
}
if n > 6 {
result[5] = s[5]
}
if n > 7 {
result[6] = s[6]
}
if n > 8 {
result[7] = s[7]
}
if n > 9 {
result[8] = s[8]
}
if n > 10 {
result[9] = s[9]
}
if n > 11 {
result[10] = s[10]
}
}
return string(result)
}
func main() {
s := "K Positions"
swappedString := swapFirstAndLast(s)
fmt.Println("Original String:", s)
fmt.Println("Swapped String:", swappedString)
}