def counting_sort_for_radix(input_array, place_value, n):
    count = [0] * 26  # As there are 26 English letters
    output = [''] * n

    # Creating the count array
    for string in input_array:
        index = ord(string[place_value]) - ord('a')
        count[index] += 1

    # Modifying the count array
    for i in range(1, 26):
        count[i] += count[i - 1]

    # Creating the output array
    i = n - 1
    while i >= 0:
        character = input_array[i][place_value]
        output[count[ord(character) - ord('a')] - 1] = input_array[i]
        count[ord(character) - ord('a')] -= 1
        i -= 1

    return output


def radix_sort(input_array):
    max_length = len(max(input_array, key=len))

    for string in input_array:
        if len(string) < max_length:
            string += 'a' * (max_length - len(string))

    for place_value in range(max_length - 1, -1, -1):
        input_array = counting_sort_for_radix(input_array, place_value, len(input_array))

    return input_array
