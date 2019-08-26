

class Solution:
    def __init__(self):
        return

    @staticmethod
    def palindromeSubstring(string):
        palindrome_list = []

        #Get indexes of start and end of substring
        for len_substring in range(len(string)-1,1,-1):
            print("ANOTHER LOOP",len_substring)
            n=0

            # Get index of first and last substring
                # n = first index
                # n+a = last index
            while (n+len_substring)<len(string):
                print(len_substring, n, n+len_substring)
                substring = string[n:n+len_substring+1]
                print(substring)

                # Check if substring is palindrome
                if substring==substring[::-1]:
                    palindrome_list.append(substring)
                    return substring
                n+=1

        return palindrome_list




def main():
    string = "tracecars"
    string2 = "million"
    string3 = "banana"
    # answer = Solution.palindromeSubstring(string)
    # answer = Solution.palindromeSubstring(string2)
    answer = Solution.palindromeSubstring(string3)

    print(answer)

if __name__=="__main__":
    main()