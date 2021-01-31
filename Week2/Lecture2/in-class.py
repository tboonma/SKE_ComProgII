def fac(n):
    if n == 0:
        return 1
    else:
        return fac(n-1) * n

print(fac(5))

def gcd(num1, num2):
    if num1 > num2:
        return gcd(num1-num2, num2)
    elif num1 < num2:
        return gcd(num1, num2-num1)
    else:
        return num1

print(gcd(68,119))

def reverse(word):
    if word == "":
        return word
    else:
        return reverse(word[1:]) + word[0]

x = "olleH"
print(reverse(x))

def is_palindrome(word):
    word = word.lower()
    if len(word) < 2:
        return True
    if word[0] == word[len(word)-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

print(is_palindrome("Refer"))
print(is_palindrome("Referer"))