def atualizar_hist(hist, paciente):
    if paciente in hist:
        hist.remove(paciente)
    hist.append(paciente)
    return hist


def main():
    hist = ['Ana', 'Carlos', 'Beatriz']
    novo = 'Carlos'
    print(f'Historico atual {hist}')
    hist = atualizar_hist(hist,novo)
    print(f'Historico atualizado: {hist}')


main()