# Isabella Souza Kelles isakelles@#unifei.edu.br
path_gulosa = list()
path_estrela = list()

total_distance_gulosa = 0
total_distance_estrela = 0
total_percorrido_estrela = 0

#Base de Fatos
mapa = dict()
cidade_inicial = ''
cidade_final = ''

cidades = ['Arad', 'Bucharest', 'Craiova', 'Drobeta', 'Eforie', 'Fagaras', 'Giurgiu', 'Hirsova', 'Iasi', 'Lugoj', 'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu Vilcea', 'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui', 'Zerind']
distancia_relativa = [366, 0, 160, 242, 161, 176, 77, 151, 226, 244, 241, 234, 380, 100, 193, 253, 329, 80, 199, 374]
cidades_vizinhas = [['Zerind', 'Timisoara', 'Sibiu'],['Pitesti', 'Fagaras', 'Urziceni','Giurgiu'], ['Drobeta', 'Pitesti', 'Rimnicu Vilcea'], ['Mehadia', 'Craiova'], ['Hirsova'], ['Sibiu', 'Bucharest'], ['Bucharest'], ['Eforie'], ['Neamt', 'Vaslui'], ['Timisoara', 'Mehadia'], ['Lugoj', 'Drobeta'], ['Iasi'], ['Zerind', 'Sibiu'], ['Rimnicu Vilcea', 'Craiova', 'Bucharest'], ['Sibiu', 'Pitesti','Craiova'], ['Oradea', 'Arad', 'Rimnicu Vilcea', 'Fagaras'], ['Arad', 'Lugoj'], ['Bucharest', 'Vaslui', 'Hirsova'], ['Iasi', 'Urziceni'], ['Oradea', 'Arad']]
distancia_vizinha = [[75, 118, 140],[101, 211, 85, 90], [120, 138, 146], [75, 120], [86], [99, 211], [90], [86], [87, 92], [111, 70], [70, 75], [87], [71, 151], [97, 138, 101], [80, 97, 146], [151, 140, 80, 99], [118, 111], [85, 142, 98], [92, 142], [71, 75]]

for i in range(len(cidades)):
    mapa[cidades[i]] = {'CidadeAtual': cidades[i], 'DistanciaRelativa': distancia_relativa[i], 'CidadeVizinha': cidades_vizinhas[i], 'DistanciaVizinha': distancia_vizinha[i]}
    
def buscar_menor_Drelativa(cidade):
    current_relative_distance = mapa[cidade]['DistanciaRelativa']
    relative_distance_list = list()
    temp_names = list()
    temp_distances = list()

    for city,number in zip(mapa[cidade]['CidadeVizinha'], range(len(mapa[cidade]['DistanciaVizinha']))):
        relative_distance_list.append(int(mapa[city]['DistanciaRelativa']))
        temp_names.append(mapa[city]['CidadeAtual'])
        temp_distances.append(int(mapa[cidade]['DistanciaVizinha'][number]))
           
    min_relative = min(relative_distance_list)
    city_name = temp_names[relative_distance_list.index(min_relative)]
    city_distance = temp_distances[relative_distance_list.index(min_relative)]


    if current_relative_distance > min_relative:
        return city_name, city_distance
    else:
        return cidade, '0'    

def busca_gulosa(cidade_checar):
    global total_distance_gulosa, path_gulosa
    city_temp, real_distance_temp = buscar_menor_Drelativa(cidade_checar)
    
    

    if (cidade_checar != cidade_final):
        if cidade_checar not in path_gulosa:
            path_gulosa.append(cidade_checar)

            total_distance_gulosa = total_distance_gulosa + real_distance_temp
            busca_gulosa(city_temp)
    
    else:
        path_gulosa.append(cidade_checar)
        print('Busca Gulosa Finalizada!')
        print('Rota : ')
        print(path_gulosa)
        print('Distancia Real Percorrida : ' + str(total_distance_gulosa))


def buscar_menor_Destrela(cidade):
    temp_names = list()
    sum_distance = list()
    temp_distances = list()
    
    for city,number in zip(mapa[cidade]['CidadeVizinha'], range(len(mapa[cidade]['DistanciaVizinha']))):
        sum_distance.append(mapa[city]['DistanciaRelativa'] + mapa[cidade]['DistanciaVizinha'][number])
        temp_names.append(mapa[city]['CidadeAtual'])
        temp_distances.append(mapa[cidade]['DistanciaVizinha'][number])
           
    min_star_distance = min(sum_distance)
    city_name = temp_names[sum_distance.index(min_star_distance)]
    city_distance = temp_distances[sum_distance.index(min_star_distance)]
    if cidade != cidade_final:
        return min_star_distance, city_name, city_distance
    else:
        return 0, ' ', 0

def busca_estrela(cidade_checar):
    global total_distance_estrela, path_estrela, total_percorrido_estrela
    
    star_distance, city_temp, city_distance_real  = buscar_menor_Destrela(cidade_checar)

    
    
    if cidade_checar != cidade_final:
        if cidade_checar not in path_estrela:
            path_estrela.append(cidade_checar)
            total_distance_estrela += star_distance
            total_percorrido_estrela += city_distance_real
            busca_estrela(city_temp)
    else:
        path_estrela.append(cidade_checar)
        print('Busca Estrela Finalizada!')
        print('Rota : ')
        print(path_estrela)
        print('Distancia Estrela Total: ' + str(total_distance_estrela))
        print('Distancia Real Percorrida: ' + str(total_percorrido_estrela))

cidade_inicial = 'Arad'
#cidade_inicial = input('Escolha a cidade inicial: ')

cidade_final = 'Bucharest'


print('Será calculado o menor caminho de ' + cidade_inicial + ' até ' + cidade_final)
busca_gulosa(cidade_inicial)
busca_estrela(cidade_inicial)









'''for city, number in zip(mapa[cidade_inicial]['CidadeVizinha'], range(len(mapa[cidade_inicial]['CidadeVizinha']))):
    atual = mapa[cidade_inicial]['CidadeAtual'] + ' ' + mapa[city]['CidadeAtual']
    relative_a = (mapa[cidade_inicial]['DistanciaRelativa']) + " " + mapa[city]['DistanciaRelativa']
    neighboor_city_a = mapa[cidade_inicial]['CidadeVizinha'][number]  + " " + mapa[city]['CidadeVizinha'][number]
    neighboor_distance_a = mapa[cidade_inicial]['DistanciaVizinha'][number] + ' ' + mapa[city]['DistanciaVizinha'][number]

    print('\nCidade atual: '+ atual)
    print('relativa: '+ relative_a)
    print('neigCity: '+ neighboor_city_a)
    print('distance: '+ neighboor_distance_a)
    '''

    
   