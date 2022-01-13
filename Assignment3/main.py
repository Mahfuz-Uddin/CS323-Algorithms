import timeit

from cffi.backend_ctypes import xrange
from prettytable import PrettyTable

global comparisonCount
comparisonCount = 0


def read_file(input):
    with open(input + '.txt') as f:
        content = f.read().upper()
        f.close()
        return content


def read_pattern(input):
    with open(input + '.txt') as f:
        pattern = []
        for i in f.readlines():
            pattern.append(i.strip())
        return pattern


#  Naive Pattern Searching algorithm
def naive_search(pat, txt):
    global comparisonCount

    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0
        comparisonCount += 1
        while j < M:
            comparisonCount += 1
            if txt[i + j] != pat[j]:
                comparisonCount += 1
                # print('comparing', txt[i + j], 'to pattern', pat[j])
                break
            j += 1
        comparisonCount += 1
        if j == M:
            print("'" + pat+ "' found at index ", i, 'using Naive Algo')
            return
    print('-1')
    return


# End of Naive Pattern Search Algorithm


# Rabin Karp Algorithm
d = 256


def rabin_search(pat, txt, q):
    global comparisonCount
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in xrange(M - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in xrange(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in xrange(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        comparisonCount += 1
        if p == t:
            # Check for characters one by one
            for j in xrange(M):
                comparisonCount += 1
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1

            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            comparisonCount += 1
            if j == M:
                print(pat, " found at index " + str(i), 'using Rabin')
                return

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        comparisonCount += 1
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            comparisonCount += 1
            if t < 0:
                t = t + q
    print('-1')


# End of Rabin Karp Algorithim

# KMP Algorithm

def KMPSearch(pat, txt):
    global comparisonCount
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    comparisonCount += 1
    while i < N:
        comparisonCount += 1
        if pat[j] == txt[i]:
            i += 1
            j += 1
        comparisonCount += 1
        if j == M:
            print("'" + pat + "' Found pattern at index " + str(i - j), 'using KMP')
            return
            j = lps[j - 1]

        # mismatch after j matches

        elif (i < N and pat[j] != txt[i]):
            comparisonCount += 2
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            comparisonCount += 1
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    print('-1')
    return


def computeLPSArray(pat, M, lps):
    global comparisonCount
    len = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    comparisonCount += 1
    while i < M:
        comparisonCount += 1
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len - 1]

            # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


# End of KMP


# Python3 Program for Bad Character Heuristic
# of Boyer Moore String Matching Algorithm

NO_OF_CHARS = 50000


def badCharHeuristic(string, size):
    '''
	The preprocessing function for
	Boyer Moore's bad character heuristic
	'''

    # Initialize all occurrence as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i

    # retun initialized list
    return badChar


def Moore_search(pat, txt):
    global comparisonCount

    '''
	A pattern searching function that uses Bad Character
	Heuristic of Boyer Moore Algorithm
	'''
    m = len(pat)
    n = len(txt)

    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)

    # s is shift of the pattern with respect to text
    s = 0
    comparisonCount += 1
    while (s <= n - m):
        j = m - 1

        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        comparisonCount += 2
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        comparisonCount += 1
        if j < 0:
            print("'" + pat + "' Pattern occur at index {} using Moore".format(s))
            return

            '''
				Shift the pattern so that the next character in text
					aligns with the last occurrence of it in pattern.
				The condition s+m < n is necessary for the case when
				pattern occurs at the end of text
			'''
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            '''
			Shift the pattern so that the bad character in text
			aligns with the last occurrence of it in pattern. The
			max function is used to make sure that we get a positive
			shift. We may get a negative shift if the last occurrence
			of bad character in pattern is on the right side of the
			current character.
			'''
            s += max(1, j - badChar[ord(txt[s + j])])
    print('-1')
    return


timedata_for_naive = []
comparisons_for_naive = []
timedata_for_rabin = []
comparisons_for_rabin = []
timedata_for_KMP = []
comparisons_for_KMP = []
timedata_for_Moore = []
comparisons_for_Moore = []
txt = read_file('input')
q = 101
pat = "REMAINING"


# KMPSearch(pat,txt)
# Moore_search(pat,txt)

def timer(theFunction, timedata_for_x, comparisons_for_x):
    txt = read_file('input')
    for i in read_pattern('pattern'):
        global comparisonCount
        for test in range(1):
            t = timeit.timeit(lambda: theFunction(i, txt), number=1)
            timedata_for_x.append(t)
            print('Total time taken is', t)
            print('Total comparison taken is', comparisonCount, '\n')
            comparisons_for_x.append(comparisonCount)
            comparisonCount = 0


def timer_for_rabin(theFunction, comparisons_for_x, timedata_for_x):
    txt = read_file('input')

    global comparisonCount
    q = 101
    for test in range(1):
        for i in read_pattern('pattern'):
            t = timeit.timeit(lambda: theFunction(i, txt, q), number=1)
            timedata_for_x.append(t)
            print('Total time taken is', t)
            print('Total comparison taken is', comparisonCount, '\n')
            comparisons_for_x.append(comparisonCount)
            comparisonCount = 0


# table = PrettyTable(['Time for Naive Search', 'Comparisons Naive Search', 'Time for Rabin',
#                      'Comparisons for Rabin', 'Time for KMP', 'Comparisons for KMP', 'Time for Moore', 'Comparisons '
#                                                                                                        'for Moore'])
timer(naive_search, timedata_for_naive, comparisons_for_naive)
print("-----------------------------------------------------------------------------------------------------------------")
timer_for_rabin(rabin_search, comparisons_for_rabin, timedata_for_rabin)
print("-----------------------------------------------------------------------------------------------------------------")
timer(KMPSearch, timedata_for_KMP, comparisons_for_KMP)
print("-----------------------------------------------------------------------------------------------------------------")
timer(Moore_search, timedata_for_Moore, comparisons_for_Moore)

# for x in range(1):
#     table.add_row([timedata_for_naive[x], comparisons_for_naive[x], timedata_for_rabin[x], comparisons_for_rabin[x],
#                    timedata_for_KMP[x], comparisons_for_KMP[x], timedata_for_Moore[x], timedata_for_Moore[x]])
# print("This data is for all pattern search algos")
# print(table)
# table2 = PrettyTable(['Best Time for Naive Search', 'Worst Time for Naive Search', 'Best Time for Time for Rabin',
#                      'Worst Time for Time for Rabin', 'Best Time for Time for KMP', 'Worst Time for Time for KMP',
#                      'Best Time for Moore', 'Worst Time for Moore'])
#
#
# table2.add_row([min(timedata_for_naive), max(timedata_for_naive), min(timedata_for_rabin), max(timedata_for_rabin),
#                    min(timedata_for_KMP), max(timedata_for_KMP), min(timedata_for_Moore), max(timedata_for_Moore)])
# print(table2)
print("TIME FOR EACH")
print("         'FREE'                  'BRAVE'                       'NATION' ")
print('Naive: ',timedata_for_naive[0],'  |  ',timedata_for_naive[1],'  |  ',timedata_for_naive[2])
print('Rabin: ',timedata_for_rabin[0],'  |  ',timedata_for_rabin[1],'  |  ', timedata_for_rabin[2])
print('KMP:   ',timedata_for_KMP[0],'  |  ',timedata_for_KMP[1],'  |  ', timedata_for_KMP[2])
print('Moore  ',timedata_for_Moore[0],'  |  ',timedata_for_Moore[1],'  |  ',timedata_for_Moore[2])

print("COMPARISON FOR EACH")

print("       'FREE'  'BRAVE'    'NATION' ")
print('Naive: ',comparisons_for_naive[0],'  |  ',comparisons_for_naive[1],'  |  ',comparisons_for_naive[2])
print('Rabin: ',comparisons_for_rabin[0],'  |  ',comparisons_for_rabin[1],'  |  ', comparisons_for_rabin[2])
print('KMP:   ',comparisons_for_KMP[0],'  |  ',comparisons_for_KMP[1],'  |  ', comparisons_for_KMP[2])
print('Moore  ',comparisons_for_Moore[0],'   |  ',comparisons_for_Moore[1],'   |  ',comparisons_for_Moore[2])