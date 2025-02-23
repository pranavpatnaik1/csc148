def fun2(stuff, junk):
    stuff = stuff + ['hi!']
    junk = junk + 1
if __name__ == '__main__':
    letters = ['a', 'b', 'c']
    age = 6
    fun2(letters, age)
    print(letters, age)