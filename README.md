# 📊 Análise das Skills Mais Pedidas em Vagas de Estágio

> Projeto em desenvolvimento para analisar vagas de estágio e identificar as competências mais solicitadas em oportunidades da área de tecnologia.

O projeto utiliza **Python e arquivos CSV** para organizar vagas, identificar competências nos requisitos e diferenciais e contabilizar sua frequência. Como próxima etapa, será desenvolvida uma automação com **n8n e Telegram** para facilitar o registro de novas vagas.

## 🎯 Objetivo

- Organizar vagas de estágio em uma base de dados.
- Identificar competências presentes nos requisitos e diferenciais.
- Contabilizar a frequência das competências encontradas.
- Gerar rankings das habilidades mais recorrentes.
- Analisar tanto **hard skills** quanto **soft skills** solicitadas nas vagas.

## 🔄 Como funciona

### Fluxo atual

**CSV → Python → Análise → Resultados**

### Fluxo planejado

**Telegram → n8n → CSV → Python → Análise → Resultados**

O fluxo com n8n ainda será desenvolvido. A ideia é utilizar o Telegram como ponto de entrada para registrar vagas de maneira prática, armazenando as informações para análise posterior.

## 🧠 Competências analisadas

As competências são organizadas em categorias para facilitar a análise.

| Categoria | Exemplos |
|---|---|
| 📊 Dados | Python, SQL, análise de dados, Pandas, ETL |
| 🤖 Inteligência Artificial | Machine Learning, Deep Learning, LLM, RAG, engenharia de prompt |
| 💻 Desenvolvimento | Python, Java, JavaScript, APIs, Backend, testes |
| ⚙️ Automação | n8n, workflows, Power Automate, webhooks |
| 🗄️ Banco de Dados | MySQL, PostgreSQL, SQL Server, MongoDB |
| 🛠️ Ferramentas | Git, GitHub, Docker, Linux, Jupyter |
| 🤝 Soft Skills | Comunicação, organização, proatividade, trabalho em equipe, pensamento crítico |

*Os exemplos representam competências previstas no dicionário utilizado pelo projeto; a frequência encontrada depende das vagas analisadas.*

## 🐍 Análise com Python

O programa utiliza um dicionário de competências organizado por categorias e verifica sua ocorrência nos requisitos e diferenciais das vagas.

O código também utiliza normalização de texto para facilitar a identificação de termos, incluindo diferenças entre letras maiúsculas, minúsculas e acentos. Além disso, considera variações de determinados termos para evitar contagens duplicadas da mesma competência.

### Resultados gerados

- Contagem de ocorrências das competências.
- Percentual de vagas em que cada competência foi identificada.
- Rankings por categoria.
- Arquivos CSV com os resultados da análise.
- Gráfico com as 10 competências mais recorrentes.

Os resultados refletem somente as vagas incluídas na base analisada, não todo o mercado de tecnologia.

## 🛠️ Tecnologias utilizadas

- **Python:** processamento e análise dos dados.
- **CSV:** armazenamento das vagas e exportação dos resultados.
- **Matplotlib:** criação de gráficos.
- **n8n:** previsto para a próxima etapa de automação.
- **Telegram:** previsto como ponto de entrada para o registro de vagas.

## 🚧 Status do projeto

- [x] Leitura dos dados de vagas em CSV.
- [x] Organização das competências por categorias.
- [x] Normalização de texto e tratamento de variações de termos.
- [x] Contagem de competências encontradas nas vagas.
- [x] Cálculo de percentuais e geração de rankings.
- [x] Exportação dos resultados para arquivos CSV.
- [x] Criação de gráfico com as 10 competências mais recorrentes.
- [ ] Criação do workflow no n8n.
- [ ] Integração com Telegram para receber novas vagas.
- [ ] Integração do fluxo automatizado com a base CSV e o processamento em Python.

## 📌 Próximos passos

1. Criar o workflow no n8n.
2. Configurar o recebimento de mensagens pelo Telegram.
3. Organizar os dados recebidos e integrá-los à base de vagas.
4. Conectar o fluxo automatizado ao processo de análise em Python.

A integração com WhatsApp poderá ser avaliada futuramente, após a validação do fluxo inicial com Telegram.
