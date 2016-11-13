class Solution(object):
    def reverseVowels(self, s):
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        if len(s)==0:
            return ""
        r = list(s)
        start=0
        end=len(s)-1
        
        while start!=end or start+1==end:
            #both consonants
            if r[start] not in vowels and r[end] not in vowels:
                if start+1 == end or end-1 == start:
                    break
                start += 1
                end -= 1
                #print "if1",start,end
            #one ptr - vowel one ptr - consonant
    
            elif (r[start] in vowels and r[end] not in vowels):
                end -= 1
                #print "if2", start, end
    
            elif (r[end] in vowels and r[start] not in vowels):
                start += 1
                #print "if3", start, end
    
            elif (r[start] in vowels and r[end] in vowels):
                r[start],r[end] = r[end],r[start]
                #print "if4", start, end
    
                if start == end or start+1==end or end-1==start:
                    break
                start += 1
                end -= 1
    
        return ''.join(r)
