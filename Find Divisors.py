
# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer'
# s divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' 
# (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
def divisors(integer):
    r =[]
    for i in range(2,integer):
        if integer%i==0:
            r.append(i)
    if len(r)<1:
        return str(integer) +' is prime'
    else:
        return r