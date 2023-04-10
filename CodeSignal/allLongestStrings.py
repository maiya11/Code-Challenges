'''
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
'''

def solution(inputArray):
    max_length = max(len(word) for word in inputArray)   
    res = [word for word in inputArray if len(word) == max_length]
    return res
