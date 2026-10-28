# 1- ()
# 2- **
# 3- * / // %
# 4- + - 

# , end=''
# \n

# {:>n}, {:<n}, {:^n}, {:n}
# {:x>n}, {:x<n}, {:x^n}, {:xn}
# {:.nf}

#exemplos:

#nome = input('qual seu nome? ')
#print(f'{nome :=^20}')

#nome = input('qual seu nome? ')
#print(f'{nome :^20}')

a = 10
for e in range(a):
    print('.' * (2 *(a - e)), '=' * (2 * e), 'oi', '=' * (2 * e), '.' * (2 *(a - e)))

for e in range(a):
    print('.' * (2 * e), '=' * (2 *(a - e)), 'oi', '=' * (2 *(a - e)), '.' * (2 * e))
