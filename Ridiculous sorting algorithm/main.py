# TODO: make this in c++
test_list = [1, 5, 3, 2, 9]

def stalin_sort(people: list):
    passed = []
    passed.append(people[0])
    for i in range(len(people)-1):
        if people[i+1] > people[i]:
            passed.append(people[i+1])

    return passed

def hitler_sort(people: list):
    passed = []
    passed.append(people[0])
    auschwitz = []
    for i in range(len(people)-1):
        if people[i+1] > people[i]:
            passed.append(people[i+1])
        if people[i+1] < people[i]:
            auschwitz.append(people[i+1])

    return passed, auschwitz

print("Ridiculous sorting algorithm that will land me in jail")

print("Unsorted list: ")
print(test_list)
print("\n")
print("Stalin Sort: ")
print(stalin_sort(test_list))
print("\n")
print("Hitler Sort: ")
p, a = hitler_sort(test_list)
print("[" + ", ".join(map(str, p)) + "]" + " In auschwitz: " + "[" + ", ".join(map(str, a)) + "]")
