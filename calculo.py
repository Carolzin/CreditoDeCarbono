from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route('/')  # Define a rota para a página inicial
def index():
    return render_template('index.html')  # Renderiza o template index.html

@app.route('/calcular', methods=['POST'])  # Define a rota para o cálculo
def calcular():
    try:
        nome = request.form.get('nome') # Obtem o primeiro nome do usuário
        if not nome:
            raise ValueError("O nome é obrigatório.")

    #ELETRICIDADE -------------------------------------------------------------------------------------------------------------------------
        # Defini as Regiões de acordo com o dado de entrada do Estado
        regioes = { 
            "Norte": ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"],
            "Nordeste": ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"],
            "Centro-Oeste": ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"],
            "Sudeste": ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"],
            "Sul": ["Paraná", "Rio Grande do Sul", "Santa Catarina"]
        }

        # Tarifas médias por região
        tarifas = { 
            "Norte": 0.90, 
            "Nordeste": 0.85, 
            "Centro-Oeste": 0.75,
            "Sudeste": 0.70, 
            "Sul": 0.80
        }

        estado = request.form.get('estado')  # Verifica o nome do Estado informado

        # Determina a região com base no estado informado
        regiao = next((r for r, estados in regioes.items() if estado in estados), None)
        if not regiao:
            raise ValueError("Estado inválido.")

        tarifa_media = tarifas[regiao]  # Obtém a tarifa média da região
        consumo_kwh = request.form.get('consumo_kwh')  # Consumo de eletricidade em kWh
        valor_reais = request.form.get('valor_reais')  # Valor em reais do consumo de eletricidade

        # Captura a entrada de consumo através do consumo expresso KWh ou Reais
        if consumo_kwh:
            consumo_kwh = float(consumo_kwh)
        elif valor_reais:
            valor_reais = float(valor_reais)
            consumo_kwh = valor_reais / tarifa_media  # Cálculo de consumo com base no valor e tarifa média por região
        else:
            raise ValueError("Consumo de eletricidade não informado.")  # Verifica se o campo de consumo de eletricidade foi preenchido

        #Fatores de Emissão para Eletricidade
        fator_emissao_eletricidade = 0.1  # kg CO2 por kWh

        # Calculo da pegada total de carbono por consumo de Eletricidade
        pegada_carbono_eletricidade = consumo_kwh * fator_emissao_eletricidade  # Calcula a pegada total de carbono da eletricidade
        media_anual_eletricidade = pegada_carbono_eletricidade * 12  # Emissão média anual da eletricidade

    #GÁS -------------------------------------------------------------------------------------------------------------------------
        # Obtém o consumo de gás
        consumo_botijao = request.form.get('consumo_botijao') # Consumo de gás pela quantidade de botijões
        consumo_gas_encanado = request.form.get('consumo_gas_encanado') # Consumo de gás em m³

        # Fatores de emissão para gás
        fator_emissao_botijao = 25.09  # kg de CO2 por botijão
        fator_emissao_gas_encanado = 2.04  # kg de CO2 por m³ de gás encanado

        # Calculo da pegada total de carbono por consumo de Gás
        pegada_carbono_gas = 0 
        if consumo_botijao:
            consumo_botijao = float(consumo_botijao)
            pegada_carbono_gas += consumo_botijao * fator_emissao_botijao  # Calcula a pegada de carbono do botijão

        if consumo_gas_encanado:
            consumo_gas_encanado = float(consumo_gas_encanado)
            pegada_carbono_gas += consumo_gas_encanado * fator_emissao_gas_encanado  # Calcula a pegada de carbono do gás encanado
        media_anual_gas = pegada_carbono_gas * 12  # Emissão média anual do gás

    #TRANSPORTE PARTICULARES -------------------------------------------------------------------------------------------------------------------------
        # Obtém o consumo de combustível
        tipo_combustivel = request.form.get('tipo_combustivel') # Tipo de combustível
        consumo_combustivel = request.form.get('consumo_combustivel') # Consumo de combustível em Litros ou Kg
        valor_combustivel = request.form.get('valor_combustivel') # Consumo de combustível em Reais

        # Fatores de emissão dos combustíveis
        fator_emissao_particular = { 
            "gasolina": 2.31,
            "diesel": 2.68,
            "cng": 2.75,
            "etanol": 1.93
        }
        # Preços dos combustíveis
        precos_combustivel = { 
            "gasolina": 6.09,
            "diesel": 5.94,
            "cng": 3.50,
            "etanol": 4.04
        }

        pegada_carbono_particular = 0  
        if tipo_combustivel in fator_emissao_particular:
            fator_emissao = fator_emissao_particular[tipo_combustivel]  # Obtém o fator de emissão de acordo com o tipo de combustível
            preco_combustivel = precos_combustivel[tipo_combustivel]  # Obtém o preço de acordo com tipo de combustível

            # Calculo da pegada total de carbono por uso de Transportes Particulares
            if consumo_combustivel:
                consumo_combustivel = float(consumo_combustivel)
            elif valor_combustivel:
                valor_combustivel = float(valor_combustivel)
                consumo_combustivel = valor_combustivel / preco_combustivel  # Cálculo de consumo a partir do valor
            else:
                raise ValueError("Consumo de combustível não informado.")  # Verifica se o campo de consumo do combustível foi preenchido

            pegada_carbono_particular += consumo_combustivel * fator_emissao  # Calcula a pegada total de carbono por uso de transportes particulares
        media_anual_particular = pegada_carbono_particular * 12  # Emissão média anual de transporte particular

    #TRANSPORTE AÉREOS -------------------------------------------------------------------------------------------------------------------------
        # Obtém o número de viagens aéreas
        viagens_nacionais = request.form.get('viagens_nacionais') # Viagens Nacionais
        viagens_internacionais = request.form.get('viagens_internacionais') # Viagens Internacionais

        # Fatores de emissão para viagens
        fator_emissao_nacional = 106.1  # kg de CO2 por viagem nacional
        fator_emissao_internacional = 605.6  # kg de CO2 por viagem internacional

        pegada_carbono_aereo = 0
        # Calculo da pegada total de carbono por uso de Transportes Aéreos
        if viagens_nacionais:
            viagens_nacionais = int(viagens_nacionais)
            pegada_carbono_aereo += viagens_nacionais * fator_emissao_nacional  # Calcula a pegada de carbono de viagens nacionais

        if viagens_internacionais:
            viagens_internacionais = int(viagens_internacionais)
            pegada_carbono_aereo += viagens_internacionais * fator_emissao_internacional  # Calcula a pegada de carbono de viagens internacionais
            
    #RESÍDUOS -------------------------------------------------------------------------------------------------------------------------
        # Obtém a quantidade de resíduos gerados
        consumo_residuos = request.form.get('residuos_gerados')

        # Fatores de emissão para resíduos -
        fator_emissao_residuos = 1.2  # kg CO2 por kg de resíduos

        pegada_carbono_residuos = 0 
        # Calculo da pegada total de carbono por Resíduos Gerados
        if consumo_residuos:
            consumo_residuos = float(consumo_residuos)
            pegada_carbono_residuos += consumo_residuos * fator_emissao_residuos  # Calcula a pegada de carbono dos resíduos
        media_anual_residuos = pegada_carbono_residuos * 12  # Emissão média anual de resíduos

    #CARNE BOVINA -------------------------------------------------------------------------------------------------------------------------
        # Obtém o consumo de carnes bovinas
        consumo_carne = request.form.get('consumo_carne')

        # Fatores de emissão para carne
        fator_emissao_carne = 27  # kg CO2 por kg de carne

        pegada_carbono_carne = 0 
        # Calculo da pegada total de carbono por Consumo de Carne Bovina
        if consumo_carne:
            consumo_carne = float(consumo_carne)
            pegada_carbono_carne += consumo_carne * fator_emissao_carne  # Calcula a pegada de carbono da carne
        media_anual_carne = pegada_carbono_carne * 12  # Emissão média anual de carne

    #EMISSÕES TOTAIS -------------------------------------------------------------------------------------------------------------------------
        total_emissoes = (
            pegada_carbono_eletricidade + 
            pegada_carbono_gas + 
            pegada_carbono_particular + 
            pegada_carbono_aereo + 
            pegada_carbono_residuos + 
            pegada_carbono_carne
        )/1000  # Convertendo total de kg CO2 para tCO2e

        total_emissoes_media = total_emissoes * 12

    #CRÉDITO DE CARBONO -------------------------------------------------------------------------------------------------------------------------
        credito_carbono = total_emissoes

    #ÁRVORES PLANTADAS -------------------------------------------------------------------------------------------------------------------------
        sequestro_arvore = 0.0059  # tCO2e/árvore
        arvores_plantadas = total_emissoes / sequestro_arvore

    #VALOR A SER PAGO -------------------------------------------------------------------------------------------------------------------------
        valor_credito = 63.50  # R$ 63,50 por crédito de carbono

        valor_total = credito_carbono * valor_credito # Total a ser pago em R$

        # Arredondando a saída dos valores
        pegada_carbono_eletricidade = round(pegada_carbono_eletricidade, 2)
        media_anual_eletricidade = round(media_anual_eletricidade, 2)
        pegada_carbono_gas = round(pegada_carbono_gas, 2)
        media_anual_gas = round(media_anual_gas, 2)
        media_anual_particular = round(media_anual_particular, 2)
        pegada_carbono_particular = round(pegada_carbono_particular, 2)
        media_anual_residuos = round(media_anual_residuos, 2)
        pegada_carbono_residuos = round(pegada_carbono_residuos, 2)
        media_anual_carne = round(media_anual_carne, 2)
        pegada_carbono_carne = round(pegada_carbono_carne, 2)
        total_emissoes = round(total_emissoes, 2)
        credito_carbono = round(credito_carbono, 0)
        arvores_plantadas = round(arvores_plantadas, 0)
        valor_total = round(valor_total, 2)
        total_emissoes_media = round(total_emissoes_media, 2)

        # Renderiza o template com o valor obtido em cada variável
        return render_template(
            'index.html',
            nome=nome,
            pegada_carbono_eletricidade=pegada_carbono_eletricidade,
            media_anual_eletricidade=media_anual_eletricidade,
            fator_emissao_eletricidade=fator_emissao_eletricidade,

            pegada_carbono_gas=pegada_carbono_gas,
            media_anual_gas=media_anual_gas,
            fator_emissao_botijao=fator_emissao_botijao,
            fator_emissao_gas_encanado=fator_emissao_gas_encanado,

            media_anual_particular=media_anual_particular,
            fator_emissao_nacional=fator_emissao_nacional,
            fator_emissao_internacional=fator_emissao_internacional,
            pegada_carbono_particular=pegada_carbono_particular,
            fator_emissao=fator_emissao,

            media_anual_residuos=media_anual_residuos,
            pegada_carbono_residuos=pegada_carbono_residuos,
            fator_emissao_residuos=fator_emissao_residuos,

            media_anual_carne=media_anual_carne,
            pegada_carbono_carne=pegada_carbono_carne,
            fator_emissao_carne=fator_emissao_carne,

            total_emissoes=total_emissoes,
            total_emissoes_media=total_emissoes_media,

            credito_carbono=int(credito_carbono),
            arvores_plantadas=int(arvores_plantadas),
            valor_total=valor_total,

            mostrar_secao4=True
        )
    except ValueError as e:
        return render_template('index.html', erro=str(e)) # Retornando mensagens de erro para o HTML 

if __name__ == '__main__':
    app.run(debug=True) 
