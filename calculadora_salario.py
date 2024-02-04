# Calculadora para saber valor de horas trabalhadas.

salario_mensal = int(input('Salario Mensal: '))
horas_mes = int(input('Horas trabalhadas dia: '))
dias_trabalhados = int(input('Dias trabalhados: '))


valor_hora = salario_mensal / (horas_mes * dias_trabalhados)

print(f'Esse mes voce trabalhou: {horas_mes * dias_trabalhados} horas.')

print(f'E o valor da sua hora e: R${valor_hora:.2f}')
