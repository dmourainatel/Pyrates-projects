import requests, json

listaNova = []   # cria lista para ser retornada no metodo trocaVazio
op = 1   # inteiro utilizado para controlar a aplicação na main
def trocaVazio(nome): # segundo
	listaNova.clear()
	nome = list(nome)
	for i in nome:
		if(i==' '):
			listaNova.append('+')
		else:
			listaNova.append(i)
	return listaNova

def convertListaParaString(lista): #terceiro
    parametroCidade = ''
    for i in lista:
        parametroCidade = parametroCidade + i
    return parametroCidade

         
while(op==1):  #criar a main primeiro
    cidade = input('Entre com o nome da cidade: ')
    siglaPais = input('Entre com uma sigla para pais (ex: br): ')

    cidadeList = trocaVazio(cidade)
    cidadeReady = convertListaParaString(cidadeList)
    uri = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s'%(cidadeReady,siglaPais)
    resposta = requests.get(uri)
    infos = json.loads(resposta.text)
    #print(infos['main']['temp'])
    temperatura = int(infos['main']['temp']) - 273
    print('A tempera tura de %s'%(cidade)+' é %d'%(temperatura)+' graus celsius')
    op = int(input('Deseja continuar verificando a temperatura? \n 1 para sim \n 0 para nao \n'))
    print('-'*60)
    

def clear():
    print('\n'*100)
    

    
