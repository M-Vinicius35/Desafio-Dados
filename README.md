# 📊 Simulação de Engenharia de Dados

Este repositório contém uma série de scripts de **ETL (Extração, Transformação e Carga)** e análise de dados, desenvolvidos como preparação prática para desafios técnicos em Ciência de Dados.

O projeto simula cenários reais de manipulação de grandes volumes de dados, tratamento de erros e normalização de estruturas complexas.

## 🛠️ Tecnologias Utilizadas
* **Python 3.13**
* **Pandas** (Manipulação e Análise de Dados)
* **JSON & CSV** (Processamento de múltiplas fontes)
* **Git & GitHub** (Versionamento e Portfólio)

## 📂 Estrutura do Projeto
A organização segue os padrões de projetos de Data Science:

* `/src`: Códigos fonte e scripts de automação.
* `/data`: Arquivos de dados brutos (Raw Data) simulados.
* `/output`: Relatórios finais processados e prontos para análise.

## 🚀 Funcionalidades Implementadas

### 1. Análise de Logs de Bateria (`analise_bateria.py`)
* **Cenário:** Processamento de logs de sensores de hardware.
* **Técnicas:** Limpeza de strings (remoção de unidades de medida), tratamento de valores nulos (`dropna`) e remoção de duplicatas.
* **Output:** Relatório de dispositivos com superaquecimento.

### 2. Pipeline de Vendas (`consolidar_relatorio.py`)
* **Cenário:** Consolidação de múltiplos arquivos diários de vendas.
* **Técnicas:** Uso da biblioteca `glob` para leitura em lote e concatenação otimizada de DataFrames.

### 3. Processamento de JSON Aninhado (`analise_financeira.py`)
* **Cenário:** Análise de dados de streaming com estruturas complexas (dicionários dentro de listas).
* **Técnicas:** Normalização de dados (`json_normalize`), feature engineering e exportação para Excel.

---
*Projeto desenvolvido para fins de estudo e aprimoramento técnico.*
