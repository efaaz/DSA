def reverse_string(str):
    reverse = ""

    for char in str:
        reverse = char + reverse
    print(reverse)
    
def reverse_recursive(str):
        if len(str) <= 0:
            return str
        return reverse_recursive(str[1:]) + str[0]
        
str = "hello"
print(reverse_recursive(str))

# Time complexity: O(n^2) due to repeated slicing and concatenation.
# Auxiliary space complexity: O(n)