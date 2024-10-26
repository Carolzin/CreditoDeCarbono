def calcular_pegada_carbono():
    try:
    #Atividades Cotianas em relação ao consumo de Energia
        regioes = { # Dividindo os Estados de acordo com a região correspondente para receber valor da tarifa
            "Norte": ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"],
            "Nordeste": ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"],
            "Centro-Oeste": ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"],
            "Sudeste": ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"],
            "Sul": ["Paraná", "Rio Grande do Sul", "Santa Catarina"]
        }


        tarifas = { # Tarifas médias por região (em R$/kWh)
            "Norte": 0.80, 
            "Nordeste": 0.75, 
            "Centro-Oeste": 0.78,
            "Sudeste": 0.85, 
            "Sul": 0.82
        }

        # Entrada de dados referente ao consumo de Eletricidade ------------------------------------------
        estado = input("Em qual Estado do Brasil você mora: ").strip()
        regiao = next((r for r, estados in regioes.items() if estado in estados), None)

        if regiao is None:
            print("Estado inválido. Tente novamente.")
            return

        tarifa_media = tarifas[regiao]
        consumo_kwh = input("Digite o consumo de energia em kWh: ").strip()
        valor_reais = input("Digite o valor gasto em reais: ").strip()

        if consumo_kwh: # Valida o tipo de dado informado, sendo ele expresso pelo consumo em KWh ou em R$
            consumo_kwh = float(consumo_kwh)
            if consumo_kwh < 0:
                raise ValueError("O consumo de energia deve ser positivo.")
        elif valor_reais:
            valor_reais = float(valor_reais)
            if valor_reais < 0:
                raise ValueError("O valor da conta deve ser positivo.")
            consumo_kwh = valor_reais / tarifa_media
        else: # Valida se um dos campos foram preenchidos
            print("Informe o consumo (kWh) ou o valor gasto (R$).")
            return

        fator_emissao_eletricidade = 0.1  # Fator médio de kg/CO₂ por kWh
        pegada_carbono_eletricidade = consumo_kwh * fator_emissao_eletricidade # Cálculo da pegada de carbono em relação ao consumo de eletricidade


        # Entrada de dados referente ao consumo de Gás ------------------------------------------
        consumo_botijao = input("Informe a quantidade de botijões consumidos por mês: ").strip()
        consumo_gas_encanado = input("Informe a quantidade de gás encanado consumida em m³ por mês: ").strip()

        fator_emissao_botijao = 25.09 # Emissão em nº de botijões de gás por Kg/CO2
        fator_emissao_gas_encanado = 2.04 # Emissão em m³ de gás encanado por Kg/CO2

        pegada_carbono_gas = 0 # Inicializando variável da pegada de carbono

        if consumo_botijao: # Valida o tipo de consumo de gás informado
            consumo_botijao = float(consumo_botijao)
            if consumo_botijao < 0:
                raise ValueError("A quantidade de botijões deve ser positiva.")
            pegada_carbono_gas += consumo_botijao * fator_emissao_botijao

        if consumo_gas_encanado:
            consumo_gas_encanado = float(consumo_gas_encanado)
            if consumo_gas_encanado < 0:
                raise ValueError("A quantidade de gás encanado deve ser positiva.")
            pegada_carbono_gas += consumo_gas_encanado * fator_emissao_gas_encanado # Cálculo da pegada de carbono em relação ao consumo de gás


    #Atividades Cotianas em relação ao uso de Transportes
        # Entrada de dados referente ao uso de Transportes Particulares ------------------------------------------
        tipo_combustivel = input("Informe o tipo de combustível (Gasolina, Diesel, CNG, Etanol): ").strip().lower()
        consumo_combustivel = input("Digite o consumo de combustível em litros/kg: ").strip()
        valor_combustivel = input("Digite o valor gasto em combustível (R$): ").strip()

        fator_emissao_particular = { # Fatores médios de emissão (kg/CO₂ por unidade)
            "gasolina": 2.31,
            "diesel": 2.68,
            "cng": 2.75,
            "etanol": 1.93
        }
        precos_combustivel = { # Preços médios  por tipo de combustível
            "gasolina": 6.09,
            "diesel": 5.94,
            "cng": 3.50,
            "etanol": 4.04
        }

        pegada_carbono_particular = 0  # Inicializando variável da pegada de carbono

        if tipo_combustivel in fator_emissao_particular: # Valida o tipo de combustível
            fator_emissao = fator_emissao_particular[tipo_combustivel]
            preco_combustivel = precos_combustivel[tipo_combustivel]

            if consumo_combustivel: # A condição verifica se o usuário informou o consumo em litros/kg ou o valor gasto em reais
                consumo_combustivel = float(consumo_combustivel)
                if consumo_combustivel < 0:
                    raise ValueError("O consumo de combustível deve ser positivo.")
            elif valor_combustivel:
                valor_combustivel = float(valor_combustivel)
                if valor_combustivel < 0:
                    raise ValueError("O valor gasto em combustível deve ser positivo.")
                consumo_combustivel = valor_combustivel / preco_combustivel  # Calcula o consumo em litros/kg
            else: # Valida se um dos campos foram preenchidos
                print("Informe o consumo de combustível (litros/kg) ou o valor gasto (R$).")
                return

            pegada_carbono_particular += consumo_combustivel * fator_emissao # Calculo da pegada de carbono referente ao uso de transportes particulares 
        else: 
            print("Tipo de combustível inválido. Tente novamente.")
            return
        

        # Entrada de dados referente ao uso de Transportes Aéreos ------------------------------------------
        viagens_nacionais = input("Informe o número de viagens nacionais realizadas por mês: ").strip()
        viagens_internacionais = input("Informe o número de viagens internacionais realizadas por mês: ").strip()

        fator_emissao_nacional = 106.1  # Fator médio de kg/CO₂ por voo por passageiro
        fator_emissao_internacional = 605.6  # Fator médio de kg/CO₂ por voo por passageiro
        
        pegada_carbono_aereo = 0  # Inicializando variável da pegada de carbono

        if viagens_nacionais:  # Verifica se o usuário informou o número de viagens nacionais
            viagens_nacionais = float(viagens_nacionais)
            if viagens_nacionais < 0:
                raise ValueError("O número de viagens nacionais deve ser positivo.")
            pegada_carbono_aereo += viagens_nacionais * fator_emissao_nacional

        if viagens_internacionais:  # Verifica se o usuário informou o número de viagens internacionais
            viagens_internacionais = float(viagens_internacionais)
            if viagens_internacionais < 0:
                raise ValueError("O número de viagens internacionais deve ser positivo.")
            pegada_carbono_aereo += viagens_internacionais * fator_emissao_internacional


    #Atividades Cotianas em relação a Produção de Resíduos
        # Entrada de dados referente a produção de resíduos ------------------------------------------
        residuos_gerados = input("Informe a quantidade total de resíduos sólidos gerados mensalmente em kg: ").strip()

        if residuos_gerados:  # Valida o tipo de dado informado
            residuos_gerados = float(residuos_gerados)
            if residuos_gerados < 0:
                raise ValueError("A quantidade de resíduos deve ser positiva.")
        else:  # Valida se o campo foi preenchido
            print("Informe a quantidade de resíduos gerados.")
            return

        fator_emissao_residuos = 1.2 # Fator de emissão para resíduos sólidos em aterros sanitários (kg CO₂e por kg de resíduo)
        pegada_carbono_residuos = 0 # Inicializando variável da pegada de carbono

        pegada_carbono_residuos += residuos_gerados * fator_emissao_residuos # Cálculo da pegada de carbono em relação ao consumo de resíduos
        

    #Atividades Cotianas em relação ao consumo de Carne Bovina
        # Entrada de dados referente ao consumo de carne bovina ------------------------------------------
        consumo_carne = input("Informe a quantidade de carne bovina consumida por mês (em kg): ").strip()

        if consumo_carne:  # Valida o tipo de dado informado
            consumo_carne = float(consumo_carne)
            if consumo_carne < 0:
                raise ValueError("A quantidade de carne deve ser positiva.")
        else:  # Valida se o campo foi preenchido
            print("Informe a quantidade de carne consumida.")
            return

        fator_emissao_carne = 27  # Fator de emissão para carne bovina (kg CO₂ por kg de carne)
        pegada_carbono_carne = 0

        pegada_carbono_carne += consumo_carne * fator_emissao_carne  # Cálculo da pegada de carbono em relação ao consumo de carne bovina

    # Calculando o valor total das emissões somadas de todas as atividades
        emissao_total_carbono = (pegada_carbono_eletricidade + pegada_carbono_gas + pegada_carbono_particular + pegada_carbono_aereo + pegada_carbono_residuos + pegada_carbono_carne)/1000
        print(f"Emissões Totais de Carbono: {emissao_total_carbono:.2f} CO₂e")

    # Calculando a qauantidade total de Créditos de Carbono através das Emissões Totais -> 1 crédito equivale a 1 tonelada de CO2
        creditos_carbono = 0
        creditos_carbono += round(emissao_total_carbono)  # Arredondando o total de créditos de carbono
        print(f"Créditos de Carbono: {creditos_carbono:.0f} CO₂e")


    except ValueError as e:
        print(f"Erro: {e}")

# Executar o cálculo
calcular_pegada_carbono()
