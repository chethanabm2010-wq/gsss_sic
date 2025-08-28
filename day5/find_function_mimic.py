# Implement a function find similar(mimic) to the find method of string class

def find_similar(s, sub, start=0, end=None):
    if end is None:
        end = len(s)

    for i in range(start, end - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1 
print(find_similar("hello world", "world"))      # 6
print(find_similar("hello world", "python"))     # -1
print(find_similar("chethana", "a", 5))          
print(find_similar("hello world", "hello"))      # 0
