import webbrowser

idols = ['iu', 'ziont', 'bts']

for i in idols : 
    webbrowser.open('https://www.google.com/search?&q={}'.format(i))
