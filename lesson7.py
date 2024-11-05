# convert int to a string

def number_to_string(num):
    return str(num)

# Vowel Count

def get_count(sentence):
    count = 0
    vowels = 'aAeEiIoOuU'
    for char in sentence:
        if char in vowels:
            count += 1
    return count

sentence = "Everyone is a winner"
print("Number of vowels:", get_count(sentence))


# Even or Odd 

def odd_or_even(arr):
    return "odd" if sum (arr)%2 != 0 else "even"
