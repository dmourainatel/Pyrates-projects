import requests,json

op = 1

while(op == 1): #main
    cidade = input('Entre com a cidade:')
    siglaPais = input('Entre com o pais:')
    
    uri = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s'%(cidade, siglaPais)

    resposta = requests.get(uri)
    informacoes = json.loads(resposta.text)

    temperatura = int(informacoes['main']['temp']) - 273
    print('\nA temperatura em %s'%cidade + ' é %d'%temperatura)
    op = int(input('\ndeseja continuar? \n 1 - sim \n 2 - nao'))
    print('-'*60)
    
                                                                   
    
    
    
    
