def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    split = string.split(" ")
    print(split)
    return "a"

# 1. a,b,c 처럼 문자가 해당 문자열에 얼마나 있는지 파악하고, 그 개수가 가장 크다면 반환해줘야 하는 값을 그 알파벳으로 변환한다.
# a -> hello my name is dingcodingco -> 0 max max_alphabet = a

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))