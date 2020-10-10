def minion_game(s):
    vowels = "AIUEO"
    kevin_sc = 0
    stuart_sc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin_sc += (len(s)-i)
        else:
            stuart_sc += (len(s)-i)
    if kevin_sc > stuart_sc:
        print("Kevin", kevin_sc)
    if kevin_sc <stuart_sc:
        print("Stuart", stuart_sc)
    if kevin_sc == stuart_sc:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)