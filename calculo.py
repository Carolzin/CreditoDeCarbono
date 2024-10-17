def calcular_eletricidade():
    try:
        consumo_kwh = float(input("Digite o consumo de energia em kWh: "))
        if consumo_kwh < 0:
            raise ValueError("O consumo de energia deve ser um número positivo.")
        
        print("Selecione a fonte de energia utilizada:")
        print("[1] Carvão (0,91 kg CO₂/kWh)")
        print("[2] Gás Natural (0,40 kg CO₂/kWh)")
        print("[3] Energia Renovável (0 kg CO₂/kWh)")
        opcao = int(input("Escolha a fonte de energia [1, 2 ou 3]: "))
        
        if opcao == 1:
            fator_emissao = 0.91
        elif opcao == 2:
            fator_emissao = 0.40
        elif opcao == 3:
            fator_emissao = 0.0
        else:
            print("Opção inválida.")
            return
        
        # Cálculo da pegada de carbono
        pegada_carbono = consumo_kwh * fator_emissao
        print(f"Pegada de carbono da eletricidade: {pegada_carbono:.2f} kg CO₂e")
    except ValueError as e:
        print(f"Erro: {e}")

def calcular_transporte():
    try:
        distancia_km = float(input("Digite a distância percorrida em km: "))
        if distancia_km < 0:
            raise ValueError("A distância percorrida deve ser um número positivo.")
        
        consumo_litro_km = float(input("Digite o consumo do veículo em litros/km: "))
        if consumo_litro_km < 0:
            raise ValueError("O consumo do veículo deve ser um número positivo.")
        
        print("Selecione o tipo de combustível:")
        print("[1] Gasolina (2,31 kg CO₂/litro)")
        print("[2] Diesel (2,68 kg CO₂/litro)")
        print("[3] Gás Natural Comprimido (2,75 kg CO₂/kg)")
        opcao = int(input("Escolha o combustível [1, 2 ou 3]: "))
        
        if opcao == 1:
            fator_emissao = 2.31
        elif opcao == 2:
            fator_emissao = 2.68
        elif opcao == 3:
            fator_emissao = 2.75
        else:
            print("Opção inválida.")
            return
        
        # Cálculo da pegada de carbono
        pegada_carbono = distancia_km * consumo_litro_km * fator_emissao
        print(f"Pegada de carbono do transporte: {pegada_carbono:.2f} kg CO₂e")
    except ValueError as e:
        print(f"Erro: {e}")

def calcular_desmatamento():
    try:
        area_desmatada = float(input("Digite a área desmatada em hectares: "))
        if area_desmatada < 0:
            raise ValueError("A área desmatada deve ser um número positivo.")
        
        biomassa = float(input("Digite a biomassa (tC/ha): "))
        if biomassa < 0:
            raise ValueError("A biomassa deve ser um número positivo.")
        
        # Cálculo das emissões de CO₂
        pegada_carbono = area_desmatada * biomassa * 3.67
        print(f"Emissões de CO₂ pelo desmatamento: {pegada_carbono:.2f} tCO₂e")
    except ValueError as e:
        print(f"Erro: {e}")

def calcular_credito_carbono():
    try:
        emissoes_totais = float(input("Digite as emissões totais (em toneladas de CO₂e): "))
        if emissoes_totais < 0:
            raise ValueError("As emissões totais devem ser um número positivo.")
        
        reducoes = float(input("Digite as reduções/compensações feitas (em toneladas de CO₂e): "))
        if reducoes < 0:
            raise ValueError("As reduções/compensações devem ser um número positivo.")
        
        # Cálculo dos créditos de carbono
        creditos_carbono = emissoes_totais - reducoes
        print(f"Créditos de carbono: {creditos_carbono:.2f} tCO₂e")
    except ValueError as e:
        print(f"Erro: {e}")

def menu():
    while True:
        print("\nCalculadora de Crédito de Carbono")
        print("[1] Calcular pegada de carbono - Eletricidade")
        print("[2] Calcular pegada de carbono - Transporte")
        print("[3] Calcular pegada de carbono - Desmatamento")
        print("[4] Calcular Créditos de Carbono")
        print("[5] Sair")
        opcao = int(input("Escolha uma opção [1, 2, 3, 4 ou 5]: "))
        
        if opcao == 1:
            calcular_eletricidade()
        elif opcao == 2:
            calcular_transporte()
        elif opcao == 3:
            calcular_desmatamento()
        elif opcao == 4:
            calcular_credito_carbono()
        elif opcao == 5:
            print("Obrigada por usar nossa calculadora!")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
