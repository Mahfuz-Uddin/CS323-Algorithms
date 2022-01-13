# Python3 Program for Bad Character Heuristic
# of Boyer Moore String Matching Algorithm

NO_OF_CHARS = 10000

def badCharHeuristic(string, size):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''

    # Initialize all occurrence as -1
    badChar = [-1]*NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i;

    # retun initialized list
    return badChar

def search(txt, pat):
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
    while(s <= n-m):
        j = m-1

        # Keep reducing index j of pattern while
        # characters of pattern and text are matching
        # at this shift s
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1

        # If the pattern is present at current shift,
        # then index j will become -1 after the above loop
        if j<0:
            print("Pattern occur at shift = {}".format(s))

            '''   
                Shift the pattern so that the next character in text
                      aligns with the last occurrence of it in pattern.
                The condition s+m < n is necessary for the case when
                   pattern occurs at the end of text
               '''
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            '''
               Shift the pattern so that the bad character in text
               aligns with the last occurrence of it in pattern. The
               max function is used to make sure that we get a positive
               shift. We may get a negative shift if the last occurrence
               of bad character in pattern is on the right side of the
               current character.
            '''
            s += max(1, j-badChar[ord(txt[s+j])])


# Driver program to test above function
def main():
    txt = '''Fourscore and seven years ago our fathers brought forth on this continent a new nation,
conceived in liberty and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so
conceived and so dedicated, can long endure. We are met on a great battlefield of that war.
We have come to dedicate a portion of that field as a final resting-place for those who here
gave their lives that that nation might live. It is altogether fitting and proper that we should
do this. But, in a larger sense, we cannot dedicate — we cannot consecrate — we cannot hallow —
this ground. The brave men, living and dead, who struggled here have consecrated it, far above our
poor power to add or detract. The world will little note, nor long remember what we say here, but
it can never forget what they did here. It is for us the living, rather, to be dedicated here to the
unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be
here dedicated to the great task remaining before us — that from these honored dead we take increased
devotion to that cause for which they gave the last full measure of devotion — that we here highly
resolve that these dead shall not have died in vain — that this nation shall have a new birth of freedom
and that government of the people, by the people, for the people, shall not perish from the earth.'''
    pat = "great"
    search(txt, pat)

if __name__ == '__main__':
    main()