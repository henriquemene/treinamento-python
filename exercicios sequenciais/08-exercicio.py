print("-------excercicio 8-------")
livro=float(input("qual é o preço do livro ? R$"))
bone=float(input("qual é o preço do boné ? R$"))
skate=float(input("qual é o preço do skete ? R$"))

if livro < bone and livro < skate:
    print("irei comprar o livro pois ele eo mais barato ! ")
if bone < livro and bone < skate:
       print("irei comprar o boné pois ele eo mais barato ! ")
if skate < bone and skate < livro:
        print("irei comprar o skate pois ele eo mais barato ! ")