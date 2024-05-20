def is_palindrome(str):              
    left_pos = 0
    right_pos = len(str)-1
    while right_pos>=left_pos:
        if not str[right_pos] == str[left_pos]:
            return False
        left_pos = left_pos+1
        right_pos = right_pos-1
    return True
print(is_palindrome("ayya"))