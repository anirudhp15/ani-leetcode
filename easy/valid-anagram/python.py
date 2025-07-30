def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT


if __name__ == "__main__":
    print(valid_anagram("cars", "arcs"))
    print(valid_anagram("anirudh", "pooja"))
