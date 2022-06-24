
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
def pig_it(text):
    #your code here
    
    t = text.split(' ')
    r = []
    for i in t:
        if i == '!' or i == '?':
            r.append(i)
        else:
            i = i[1:]+i[0] +'ay'
            r.append(i)
    return ' '.join(r)