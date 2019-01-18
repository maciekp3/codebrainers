from googlesearch import search
import newspaper

for url in search("Maciej Pierek", stop=1):
    art = newspaper.Article (url)
    art.download()
    art.parse()
    print(art.text)

#parsowanie