# def reverseVowels(self, s):
#     """
#     :type s: str
#     :rtype: str
#     """
    
#     vowels = "AaEeIiOoUu"
    
#     i = 0
#     j = len(s) - 1
    
#     l = list(s)
    
#     while i < j:
        
#         if l[i] in vowels and l[j] in vowels:
#             l[i], l[j] = l[j], l[i]
#             i += 1
#             j -= 1
#         elif l[i] in vowels:
#             j -= 1
#         elif l[j] in vowels:
#             i += 1
#         else:
#             i += 1
#             j -= 1
    
#     return "".join(l)



def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
print(reverse_vowels("w3resource"))
print(reverse_vowels("Python"))
print(reverse_vowels("Perl"))
print(reverse_vowels("USA"))