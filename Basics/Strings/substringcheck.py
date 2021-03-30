"""
This is a program that counts the number of times of substr in str
there is a difference from the count() method of the string
"""


def sub_count(substring):
    count = 0
    string_ = 'a'

    a = len(substring)
    for i in range(len(string_)):
        if string_[i:i + a] == substring:
            count += 1
    return count


if __name__ == '__main__':
    string = input()
    sub_string = input()
    print(sub_count(sub_string))
