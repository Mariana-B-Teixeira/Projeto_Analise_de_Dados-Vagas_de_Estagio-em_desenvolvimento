# 📊 Análise de Vagas de Estágio em Tecnologia

> Projeto em desenvolvimento para analisar vagas de estágio e identificar as competências mais solicitadas pelo mercado de tecnologia.

O projeto combina **Python, CSV, n8n e WhatsApp** para transformar vagas encontradas durante a busca por oportunidades em dados que podem ser analisados.

---

## 🎯 Objetivo

A proposta é criar um fluxo que permita:

- registrar vagas de estágio de forma prática;
- organizar os dados coletados;
- identificar as competências presentes nos requisitos;
- contabilizar a frequência dessas competências;
- entender quais conhecimentos são mais solicitados nas vagas analisadas.

A análise considera tanto **hard skills** quanto **soft skills**.

---

## 🔄 Como funciona

O fluxo planejado conecta a coleta das vagas à análise dos dados:

**WhatsApp → n8n → CSV → Python → Análise → Resultados**

### 1. Coleta

A vaga é enviada pelo **WhatsApp** para facilitar o registro durante a busca por oportunidades.

### 2. Organização

O **n8n** será utilizado para automatizar o recebimento e a organização das informações em uma planilha, o que auxilia a guardar informações importantes que podem ser utilizadas, de maneira prática.

### 3. Armazenamento

Os dados são registrados em um arquivo **CSV**, formando a base utilizada na análise.

### 4. Análise

O **Python** identifica as competências presentes nos requisitos das vagas e contabiliza suas ocorrências.

### 5. Resultados

Os dados analisados poderão ser utilizados para gerar rankings e visualizar quais competências aparecem com maior frequência.

---

## 🧠 Competências analisadas

As competências são organizadas em categorias:

| Categoria | Exemplos |
|---|---|
| 📊 Dados | Python, SQL, análise de dados, ETL |
| 🤖 Inteligência Artificial | IA Generativa, RAG, LLM, Machine Learning |
| 💻 Desenvolvimento | Python, Java, APIs, Backend |
| ⚙️ Automação | n8n, workflows, webhooks |
| 🗄️ Banco de Dados | MySQL, PostgreSQL, SQL |
| 🛠️ Ferramentas | Git, GitHub, Docker, Linux |
| 🤝 Soft Skills | Comunicação, organização, proatividade, trabalho em equipe |

---

## 🐍 Análise com Python

A análise parte de um dicionário de competências organizado por categorias.

O programa percorre essas competências e verifica quais aparecem nos requisitos das vagas.

Exemplo:

```text
python : 3
sql : 4
rag : 1
n8n : 2
comunicação : 5
