# Solicitar dados
tipo = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().capitalize()
consumo = float(input("Digite o consumo mensal de água em m³: "))

# Classificação de acordo com as regras
if tipo == "Comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo == "Apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif tipo == "Apartamento" or (tipo == "Casa" and consumo <= 25):
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
