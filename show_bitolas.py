import csv

BITOLA_FILE = 'bitolas.csv'

def load_data():
    data = {}
    with open(BITOLA_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            family = row['family']
            bitola = row['bitola']
            data.setdefault(family, []).append(bitola)
    return data

def main():
    data = load_data()
    families = list(data.keys())
    print('Familias disponíveis:')
    for idx, fam in enumerate(families, start=1):
        print(f'{idx}. {fam}')
    choice = input('Escolha o numero da família: ')
    if not choice.isdigit() or not (1 <= int(choice) <= len(families)):
        print('Opção inválida.')
        return
    selected = families[int(choice) - 1]
    print(f'Bitolas para {selected}:')
    for b in data[selected]:
        print(f'- {b}')

if __name__ == '__main__':
    main()
