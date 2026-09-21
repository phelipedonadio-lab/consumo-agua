# 💧📊 Classificador de Consumo de Água por Perfil de Imóvel

![Python](https://skillicons.dev/icons?i=python) ![VS Code](https://skillicons.dev/icons?i=vscode)

![Nível](https://img.shields.io/badge/Nível-Iniciante-yellow?style=for-the-badge)

---

## Descrição

O objetivo é classificar o **consumo mensal de água** (em m³) de um imóvel de acordo com o seu **tipo** (comercial, casa ou apartamento), retornando uma mensagem que indica se o consumo está dentro do esperado, é econômico ou excessivo para aquele perfil.

---

## Objetivo do Projeto

Praticar conceitos fundamentais de programação, como:

- 📥📤 Entrada e saída de dados (`input()` / `print()`)
- 🔀 Estruturas condicionais encadeadas (`if` / `elif` / `else`)
- ✂️ Tratamento de strings (`.strip()`, `.capitalize()`)
- 🧠 Combinação de condições lógicas (`and` / `or`)

---

## Instruções de Uso

1. Execute o arquivo `classificador_agua.py`.
2. Informe o tipo de imóvel (comercial, casa ou apartamento) e o consumo mensal de água em m³.

   > ⚠️ **Observação:** informe o consumo apenas com o valor numérico, **sem unidade de medida** (ex.: digite `18`, não `18m³`).

3. Exemplo: `Apartamento`, `8` → o programa retorna "Consumo econômico – excelente controle de água!".

---

## 📋 Tabela de Regras de Classificação

Complementando o fluxograma, uma tabela de regras facilita consultas rápidas — é o mesmo tipo de artefato usado em documentações técnicas para deixar regras de negócio explícitas e fáceis de atualizar quando os limites (thresholds) mudarem.

| Tipo de Imóvel | Condição            | Classificação                  |
|-----------------|---------------------|---------------------------------|
| Comercial       | —                    | Tarifa comercial (plano corporativo) |
| Apartamento     | Consumo < 10 m³      | Consumo econômico               |
| Apartamento     | Consumo ≥ 10 m³      | Consumo moderado                |
| Casa            | Consumo ≤ 25 m³      | Consumo moderado                |
| Casa            | Consumo > 25 m³      | Consumo excessivo               |
