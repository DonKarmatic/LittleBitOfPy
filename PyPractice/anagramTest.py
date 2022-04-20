
s1 = "silent"
s2 = "listen"

def isAnagram(s1, s2):
    n1 = sort(s1);
    n2 = sort(s2);
    if n1 == n2:
        return True
    else:
        return False


isAnagram(s1, s2)
