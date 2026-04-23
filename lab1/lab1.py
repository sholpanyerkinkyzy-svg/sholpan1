#1
def analyze_text(text):
    vowels = "aeiouy"
    unique_vowels = set()
    words = []
    current = ""

    for ch in text.lower():
        if ch.isalpha():
            current += ch
            if ch in vowels:
                unique_vowels.add(ch)
        else:
            if len(current) >= 5 and current[0] == current[-1] and current not in words:
                words.append(current)
            current = ""

    if len(current) >= 5 and current[0] == current[-1] and current not in words:
        words.append(current)

    return (len(unique_vowels), " ".join(words))
print("ЗАДАЧА 1:", analyze_text("Amazing radar level stats 12345"))

#2
task2 = lambda s: " ".join(
    filter(lambda w: len(w) % 2 == 0,
           map(lambda w: w[::-1],
               filter(lambda w: not any(c.isdigit() for c in w), s.split())))
)

print(task2("hello 123 world python test45"))

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

#4
task4 = lambda s: " ".join(
    w.lower() for w in s.split()
    if sum(1 for c in w if c.isupper()) == 1
    and not w[0].isupper()
    and not w[-1].isupper()
)

print(task4("heLlo worLd PyThoN TesT"))

#5
def compress_text(text):
    if not text:
        return ""

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i].lower() == text[i-1].lower():
            count += 1
        else:
            result += text[i-1] + (str(count) if count > 1 else "")
            count = 1

    result += text[-1] + (str(count) if count > 1 else "")
    return result


print(compress_text("aaBBcDDD"))

#6
task6 = lambda s: list(
    filter(lambda w: len(w) >= 4
                     and len(set(w)) == len(w)
                     and not any(c.isdigit() for c in w),
           s.split())
)
print(task6("hello test abcde aabb 1234 world"))

#7
def palindrome_words(text):
    clean = ""

    for ch in text.lower():
        if ch.isalpha() or ch == " ":
            clean += ch

    words = set(clean.split())

    pal = [w for w in words if len(w) >= 3 and w == w[::-1]]

    return sorted(pal, key=lambda x: (-len(x), x))


print(palindrome_words("level radar stats hello wow noon"))

task8 = lambda s: " ".join(
    "VOWEL" if w[0].lower() in "aeiouy"
    else "CONSONANT" if w.isalpha()
    else w
    for w in s.split()
)

print(task8("apple banana car 123test egg"))

#8
task8 = lambda s: " ".join(
    "VOWEL" if w[0].lower() in "aeiouy"
    else "CONSONANT" if w.isalpha()
    else w
    for w in s.split()
)

print(task8("apple banana car 123test egg"))

#9
def alternate_case_blocks(text, n):
    result = ""

    for i in range(0, len(text), n):
        block = text[i:i+n]
        if (i // n) % 2 == 0:
            result += block.upper()
        else:
            result += block.lower()

    return result.replace(" ", "")


print(alternate_case_blocks("abcdefghijk", 3))

#10
task10 = lambda s: sum(
    1 for w in s.split()
    if any(c.isdigit() for c in w)
    and not w[0].isdigit()
    and len(w) >= 5
)

print(task10("abc12 test123 word1 hello12345 a1b2c3"))

#11
def common_unique_chars(s1, s2):
    result = ""
    used = set()

    for ch in s1:
        if ch in s2 and ch not in used and not ch.isdigit() and ch != " ":
            result += ch
            used.add(ch)

    return result


print(common_unique_chars("hello world 123", "world hello"))

#12
task12 = lambda s: list(
    filter(lambda w: len(w) > 3
                     and w[0] == w[-1]
                     and w != w[::-1],
           s.split())
)

print(task12("level hello radar world refer test"))

#13
def replace_every_nth(text, n, char):
    result = list(text)
    words = text.split()

    index = 0
    for w in words:
        if len(w) < 3:
            index += len(w) + 1
            continue

        for i in range(len(w)):
            if (index + i + 1) % n == 0:
                if not w[i].isdigit():
                    result[index + i] = char

        index += len(w) + 1

    return "".join(result)


print(replace_every_nth("hello world python", 3, "*"))

#14
task14 = lambda s: ",".join(
    w for w in s.split()
    if len(set(w)) > 3
    and all(w.count(v) <= 1 for v in "aeiouy")
)

print(task14("hello world apple banana sky"))

#15
def word_pattern_sort(text):
    groups = {}

    for w in text.split():
        groups.setdefault(len(w), []).append(w)

    result = []

    for length in sorted(groups):
        words = groups[length]
        words.sort(key=lambda w: (-sum(1 for c in w if c.lower() in "aeiouy"), w))
        result.extend(words)

    return result


print(word_pattern_sort("hello world apple banana sky"))

#2.1
def invert_unique(d):
    result = {}

    for k, v in d.items():
        if v not in result:
            result[v] = []
        if k not in result[v]:
            result[v].append(k)

    return result


print(invert_unique({'a': 1, 'b': 2, 'c': 1}))

#2.2
task2 = lambda s: set(
    x for x in s
    if x > sum(s)/len(s) and x % 2 != 0 and x % 5 != 0
)

print(task2({1, 3, 5, 7, 9, 10}))

#2.3
def merge_dicts_sum(d1, d2):
    result = {}

    for k in d1:
        result[k] = d1[k]

    for k in d2:
        if k in result:
            result[k] += d2[k]
        else:
            result[k] = d2[k]

    return result


print(merge_dicts_sum({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

#2.4
def filter_sets(sets_list):
    result = []

    for s in sets_list:
        if len(s) > 3 and all(x >= 0 for x in s) and any(x % 2 == 0 for x in s):
            result.append(s)

    return result


print(filter_sets([{1,2,3,4}, {1,-2,3,4}, {2,4,6,8}, {1,3,5}]))

#2.5
task5 = lambda d: [k for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0]))][:5]

print(task5({'a': 5, 'b': 3, 'c': 5, 'd': 2, 'e': 4}))

#2.6
def deep_sum(d):
    total = 0

    for v in d.values():
        if isinstance(v, int):
            total += v
        elif isinstance(v, list):
            total += sum(v)
        elif isinstance(v, dict):
            total += deep_sum(v)

    return total


print(deep_sum({'a': 1, 'b': [2,3], 'c': {'d': 4}}))

#2.7
task7 = lambda a, b: set(x for x in a ^ b if x % 2 == 0)

print(task7({1,2,3,4}, {3,4,5,6}))

#2.8
def sort_dict_by_value_length(d):
    return sorted(d.items(), key=lambda x: (len(x[1]), x[0]))


print(sort_dict_by_value_length({'a': 'hi', 'b': 'hello', 'c': 'hey'}))

#2.9
def common_elements_all(sets_list):
    if not sets_list:
        return set()

    result = sets_list[0]

    for s in sets_list[1:]:
        result = result & s

    return result


print(common_elements_all([{1,2,3}, {2,3,4}, {2,5,3}]))

#2.10
task10 = lambda d: {
    k: sorted([x for x in v if x % 2 != 0])
    for k, v in d.items()
    if any(x % 2 != 0 for x in v)
}

print(task10({'a': [1,2,3], 'b': [2,4], 'c': [5,7]}))

#2.11
def group_by_length(words):
    result = {}

    for w in words:
        l = len(w)
        if l not in result:
            result[l] = []
        if w not in result[l]:
            result[l].append(w)

    return result


print(group_by_length(["hi", "hello", "hi", "hey"]))

#2.12
task12 = lambda s: set(
    w for w in s
    if w.isalpha() and len(w) > 4 and len(set(w)) == len(w)
)

print(task12({"hello", "world", "abcde", "aabb"}))

#2.13
def invert_dict_strict(d):
    result = {}
    count = {}

    for v in d.values():
        count[v] = count.get(v, 0) + 1

    for k, v in d.items():
        if count[v] == 1:
            result[v] = k

    return result


print(invert_dict_strict({'a': 1, 'b': 2, 'c': 1}))


#2.14
def top_k_frequent(nums, k):
    freq = {}

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    sorted_nums = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return set(n for n, _ in sorted_nums[:k])


print(top_k_frequent([1,1,2,2,2,3,3,4], 2))

#2.15
task15 = lambda d: {
    k: v for k, v in d.items()
    if v >= sum(d.values())/len(d) and v % 2 != 0
}

print(task15({'a': 1, 'b': 5, 'c': 3, 'd': 8}))