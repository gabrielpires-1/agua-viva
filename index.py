# importa a biblioteca utilizada para fazer a comunicação com o arduino
import serial
import os

# porta serial em que o arduino está conectado
port = "COM5"
# baud rate do arduino
baudeRate = 9600

qtLiters = 0
price = 0
conectado = True

# tenta realizar a conexão
try: 
    # se conecta a porta serial do arduino na porta especificada e baud rate informado
    arduino = serial.Serial (port, baudeRate);
    print("Conectado com a porta", arduino.portstr)
# caso dê errado a tentativa de conexão
except serial.SerialException:
    print("Porta não detectada!")
    conectado = False

# enquanto o arduino estiver conectado este bloco irá rodar
while conectado:

    # lê a linha do monitor serial do arduino
    line = str(arduino.readline())
    # recorta a string para 'line' receber apenas o número, e o transforma em float
    line = float(line[2:-5])

    # acumula na variável qtLiters a quantidade de litros recebida
    qtLiters += line/1000
    # transforma para m³
    mCubic = qtLiters/1000
    # converte para o preço, em reais
    price = mCubic*19.74
    os.system('cls')
    print(f"Consumo em litros: {qtLiters:.2f}L || Custo da hospedagem em tempo Real: R${price:.4f}",end="\n")

