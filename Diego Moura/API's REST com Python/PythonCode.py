link http://jsonplaceholder.typicode.com/   site API fake
     http://en.wikipedia.org/wiki/List_of_HTTP_status_codes      site HTTP status code
     
     http://openweathermap.org/    site API Open Wheather

     
//pip install requests

import requests, json

resposta = requests.get('http://jsonplaceholder.typicode.com/albums')

print(resposta.status_code)

//Mostrar resultado da resposta na tabela de requisições HTTP

print(resposta.content) // explicar o retorno comparando com resposta.text
type(resposta.content)  // retorno do conteudo eh em bytes

print(resposta.text)
type(resposta.text)

help(json.loads) // mostrar o parametro que o metodo loads espera, que deve ser
                 // uma string
albuns = json.loads(resposta.text)//explicar Desserialização de um obj Json em um
                                  // List<Dict<string,value>> object

type(albuns)
print(albuns[0]) //mostrar dicionario de valores vindos do webservice

for album in albuns[0:50]:
	print(album['title']) //Assim eh possivel extrair informacao util
                              // para ser manipulada em nossa aplicacao

PARA O POST - Criação, é necessário criar um valor com o mesmo contido no JSON
/*
  {
    "userId": 10,
    "id": 100,
    "title": "enim repellat iste"
  }
*/

dados = {'userId':15,'id':1000,'title':'Pyrates POSTando'}
resposta = requests.post('http://jsonplaceholder.typicode.com/albums/',dados)

print(resposta.status_code) // verificar se o retorno é 200
print(resposta.text)

// PUT - alteração, utilizado para alterar um valor no endpoint
changeData = {'title':'YMCA'} 
resposta = requests.put('http://jsonplaceholder.typicode.com/albums/1000',changeData)

print(resposta.status_code)

// DELETE - remoção de dados no endpoint
resposta = requests.delete('http://jsonplaceholder.typicode.com/albums/1000')

print(resposta.status_code)

// explicar que os metodos GET, PUT, POST e DELETE são ou não possivel de ser
//executados dependendo da forma que o web service foi implementado, se o desenvolvedor
// que o criou o fez de forma a deixar o dados serem manipulados de todas as formas
// entao sera possivel utilizar todos os metodos padroes de REST

def clear():
    print('\n'*100)

