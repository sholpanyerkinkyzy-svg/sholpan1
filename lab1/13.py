
#3
def top_k_words(text, k):
    text = text.lower()
    clean = ""

    for ch in text:
        if ch.isalpha() or ch == " ":
            clean += ch

    words = clean.split()
    freq = {}

    for w in words:
        freq[w] = freq.get(w, 0) + 1

    result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return [w for w, _ in result[:k]]


print(top_k_words("Hello hello world world world test test", 2))
#6
esep = map(lambda s :)










