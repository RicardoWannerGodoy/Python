import Simulação

if __name__ == '__main__':
    passos = 10
    todas_as_medias = 0
    for Y in range(passos):
        sim = Simulação.Simulação()
        todas_as_medias += sim.run_model()
    print(f'A média da experiencia de simular {passos} número de vezes é: {todas_as_medias/passos}')
