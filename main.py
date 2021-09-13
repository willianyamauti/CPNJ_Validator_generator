import cnpj

# CNPJ = input('Digite o cnpj: ')
CNPJ = '04.252.011/0001-10'

if cnpj.checar_cnpj(CNPJ):
    print(f'O CNPJ {CNPJ} é valido!')
else:
    print(f'O CNPJ {CNPJ} é invalido!')