#以一行陳述式來表示的匿名函式
#用來取代一般小涵函式
def edit_story(words,func):
    for word in words: #word 是iterator ,words是iterable
        print(func(word))
def enliven(word):
    return word.capitalize()+ '!' #mini function
stairs=['thud','meow','thud','hiss']
#mix element
#edit_story(stairs,enliven)

#lambda way
edit_story(stairs,lambda word:word.capitalize() +'!')
