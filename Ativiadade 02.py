
# Exemplo de acesso lista de lista print(mapa[0]['CidadeVizinha'][0] + ' ' + mapa[0]['DistanciaVizinha'][0])
path = list()
total_distance = 0

#Base de Fatos
mapa = dict()

cidades = ['Arad', 'Bucharest', 'Craiova', 'Drobeta', 'Eforie', 'Fagaras', 'Giurgiu', 'Hirsova', 'Iasi', 'Lugoj', 'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu Vilcea', 'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui', 'Zerind']
distancia_relativa = ['366', '0', '160', '242', '161', '176', '77', '151', '226', '244', '241', '234', '380', '100', '193', '253', '329', '80', '199', '374']
cidades_vizinhas = [['Zerind', 'Timisoara', 'Sibiu'],['Pitesti', 'Fagaras', 'Urziceni','Giurgiu'], ['Drobeta', 'Pitesti', 'Rimnicu Vilcea'], ['Mehadia', 'Craiova'], ['Hirsova'], ['Sibiu', 'Bucharest'], ['Bucharest'], ['Eforie'], ['Neamt', 'Vaslui'], ['Timisoara', 'Mehadia'], ['Lugoj', 'Drobeta'], ['Iasi'], ['Zerind', 'Sibiu'], ['Rimnicu Vilcea', 'Craiova', 'Bucharest'], ['Sibiu', 'Pitest','Craiova'], ['Oradea', 'Arad', 'Rimnicu Vilcea', 'Fagaras'], ['Arad', 'Lugoj'], ['Bucharest', 'Vaslui', 'Hirsova'], ['Iasi', 'Urziceni'], ['Oradea', 'Arad']]
distancia_vizinha = [['75','118', '140'],['101','211','85','90'], ['120', '138', '146'], ['75', '120'], ['86'], ['99', '211'], ['90'], ['86'], ['87', '92'], ['111', '70'], ['70', '75'], ['87'], ['71', '151'], ['97', '138', '101'], ['80', '97', '146'], ['151', '140', '80', '99'], ['118', '111'], ['85', '142', '98'], ['92', '142'], ['71', '75']]

for i in range(len(cidades)):
    mapa[cidades[i]] = {'CidadeAtual': cidades[i], 'DistanciaRelativa': distancia_relativa[i], 'CidadeVizinha': cidades_vizinhas[i], 'DistanciaVizinha': distancia_vizinha[i]}
    
    
def buscar_proxima_cidade_Drelativa(cidade_atual):
    next_city_distance = '1000'
    next_city_name = ''

    for city, number in zip(mapa[cidade_atual]['CidadeVizinha'], range(len(mapa[cidade_atual]['CidadeVizinha']))):
        if int(mapa[city]['DistanciaRelativa']) < int(next_city_distance):
            next_city_distance = int(mapa[city]['DistanciaRelativa'])
            next_city_name = city
            next_city_real_distance = mapa[cidade_atual]['DistanciaVizinha'][number]
    return next_city_name, next_city_distance, next_city_real_distance

def busca_gulosa(cidade_atual):
    global total_distance, path
    city_temp, distanceRelativa_temp, distanceReal_temp = buscar_proxima_cidade_Drelativa(cidade_atual)

    path.append(cidade_atual)
    

    if str(cidade_atual) != 'Bucharest':
        total_distance = total_distance + int(distanceReal_temp)
        busca_gulosa(city_temp) 
        
    else:
        print('Busca Gulosa Finalizada')
        print('Distância total: ' + str(total_distance))
        print('Caminho Percorrido: ')
        print(path)

busca_gulosa('Arad')
   