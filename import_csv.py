import re
import unicodedata
import csv

vagas = []

with open("vagas_estagio.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")

    for vaga in reader:
        vagas.append(vaga)

for vaga in vagas:
    print(vaga['empresa'],": ",vaga['cargo'], sep="")


total_vagas = len(vagas)

skills = {

    "dados": [
        "python",
        "sql",
        "excel",
        "análise de dados",
        "data analysis",
        "analytics",
        "data analytics",
        "data science",
        "ciência de dados",
        "pandas",
        "numpy",
        "estatística",
        "banco de dados",
        "database",
        "modelagem de dados",
        "etl",
        "pipeline de dados",
        "engenharia de dados"
    ],

    "inteligencia_artificial": [
        "inteligência artificial",
        "artificial intelligence",
        "ia generativa",
        "generative ai",
        "machine learning",
        "aprendizado de máquina",
        "deep learning",
        "llm",
        "large language model",
        "rag",
        "retrieval augmented generation",
        "prompt engineering",
        "engenharia de prompt",
        "agentes de ia",
        "ai agents",
        "agentes inteligentes",
        "chatgpt",
        "azure ai",
        "azure ai foundry"
    ],

    "desenvolvimento": [
        "python",
        "java",
        "php",
        "laravel",
        "javascript",
        "html",
        "css",
        "backend",
        "back-end",
        "desenvolvimento backend",
        "desenvolvimento de software",
        "api",
        "apis",
        "api rest",
        "rest api",
        "programação orientada a objetos",
        "poo",
        "crud",
        "teste",
        "teste unitário",
        "debug",
        "debugging",
        "clean code"
    ],

    "automacao": [
        "automação",
        "automação de processo",
        "n8n",
        "workflow",
        "power automate",
        "integração",
        "webhook"
    ],

    "banco_de_dados": [
        "mysql",
        "postgresql",
        "postgres",
        "oracle",
        "sql server",
        "mongodb",
        "nosql",
        "join",
        "consulta sql"
    ],

    "ferramentas": [
        "git",
        "github",
        "gitlab",
        "docker",
        "docker compose",
        "linux",
        "jupyter",
        "visual studio code",
        "vscode",
        "postman",
        "json",
        "csv"
    ],

    "soft_skills": [
        "comunicação",
        "trabalho em equipe",
        "trabalho em equipa",
        "teamwork",
        "colaboração",
        "proatividade",
        "organização",
        "raciocínio lógico",
        "resolução de problemas",
        "problem solving",
        "pensamento crítico",
        "adaptabilidade",
        "autonomia",
        "liderança"
    ]
}

variacoes_habilidades = {
    # DADOS
    "análise de dados": [
        "análise de dados",
        "análises de dados",
        "data analysis"
    ],
    "ciência de dados": [
        "ciência de dados",
        "ciências de dados",
        "data science"
    ],
    "banco de dados": [
        "banco de dados",
        "bancos de dados",
        "database",
        "databases"
    ],
    "modelagem de dados": [
        "modelagem de dados",
        "modelagens de dados",
        "data modeling",
        "data modelling"
    ],
    "pipeline de dados": [
        "pipeline de dados",
        "pipelines de dados",
        "data pipeline",
        "data pipelines"
    ],
    "engenharia de dados": [
        "engenharia de dados",
        "engenharias de dados",
        "data engineering"
    ],
    "estatística": [
        "estatística",
        "estatísticas",
        "statistics"
    ],

    # INTELIGÊNCIA ARTIFICIAL
    "inteligência artificial": [
        "inteligência artificial",
        "artificial intelligence"
    ],
    "ia generativa": [
        "ia generativa",
        "generative ai"
    ],
    "machine learning": [
        "machine learning",
        "aprendizado de máquina"
    ],
    "deep learning": [
        "deep learning",
        "aprendizagem profunda",
        "aprendizado profundo"
    ],
    "large language model": [
        "large language model",
        "large language models",
        "llm",
        "llms"
    ],
    "rag": [
        "rag",
        "retrieval augmented generation"
    ],
    "engenharia de prompt": [
        "engenharia de prompt",
        "engenharia de prompts",
        "prompt engineering"
    ],
    "agentes de ia": [
        "agente de ia",
        "agentes de ia",
        "ai agent",
        "ai agents"
    ],
    "agentes inteligentes": [
        "agente inteligente",
        "agentes inteligentes",
        "intelligent agents"
    ],

    # DESENVOLVIMENTO
    "backend": [
        "backend",
        "back-end"
    ],
    "api": [
        "api",
        "apis"
    ],
    "api rest": [
        "api rest",
        "apis rest",
        "rest api",
        "rest apis"
    ],
    "programação orientada a objetos": [
        "programação orientada a objetos",
        "poo",
        "object-oriented programming",
        "oop"
    ],
    "teste": [
        "teste",
        "testes",
        "test",
        "tests"
    ],
    "teste unitário": [
        "teste unitário",
        "testes unitários",
        "unit test",
        "unit tests",
        "unit testing"
    ],
    "debugging": [
        "debug",
        "debugging"
    ],
    "clean code": [
        "clean code"
    ],

    # AUTOMAÇÃO
    "automação": [
        "automação",
        "automation"
    ],
    "automação de processo": [
        "automação de processo",
        "automação de processos",
        "process automation"
    ],
    "workflow": [
        "workflow",
        "workflows"
    ],
    "integração": [
        "integração",
        "integrações",
        "integration",
        "integrations"
    ],
    "webhook": [
        "webhook",
        "webhooks"
    ],

    # BANCO DE DADOS
    "postgresql": [
        "postgresql",
        "postgres"
    ],
    "mongodb": [
        "mongodb",
        "mongo db"
    ],
    "nosql": [
        "nosql",
        "no sql"
    ],
    "join": [
        "join",
        "joins"
    ],
    "consulta sql": [
        "consulta sql",
        "consultas sql",
        "sql query",
        "sql queries"
    ],

    # FERRAMENTAS
    "github": [
        "github"
    ],
    "gitlab": [
        "gitlab"
    ],
    "docker compose": [
        "docker compose",
        "docker-compose"
    ],
    "visual studio code": [
        "visual studio code",
        "vscode"
    ],

    # SOFT SKILLS
    "comunicação": [
        "comunicação",
        "comunicacao",
        "communication"
    ],
    "trabalho em equipe": [
        "trabalho em equipe",
        "trabalhos em equipe",
        "trabalho em equipa",
        "teamwork",
        "team work"
    ],
    "colaboração": [
        "colaboração",
        "colaborações",
        "collaboration"
    ],
    "proatividade": [
        "proatividade",
        "proactive",
        "proactivity"
    ],
    "organização": [
        "organização",
        "organizacao",
        "organization",
        "organisation"
    ],
    "raciocínio lógico": [
        "raciocínio lógico",
        "raciocinio logico",
        "logical reasoning"
    ],
    "resolução de problemas": [
        "resolução de problema",
        "resolução de problemas",
        "problem solving"
    ],
    "pensamento crítico": [
        "pensamento crítico",
        "pensamento critico",
        "critical thinking"
    ],
    "adaptabilidade": [
        "adaptabilidade",
        "adaptability"
    ],
    "autonomia": [
        "autonomia",
        "autonomy"
    ],
    "liderança": [
        "liderança",
        "lideranca",
        "leadership"
    ]
}


# # Tira duplicata.
# todas_skills = set()
# for categoria in skills:
#     for skill in skills[categoria]:
#         todas_skills.add(skill)

def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)

    caracteres = []

    for caractere in texto:
        if unicodedata.category(caractere) != "Mn":
            caracteres.append(caractere)

    texto = "".join(caracteres)
    return texto

def encontrar_habilidade(texto, skill):
    texto = normalizar_texto(texto)
    skill = normalizar_texto(skill)

    habilidade = rf"\b{re.escape(skill)}\b"

    return re.search(habilidade, texto) is not None

def encontrar_variacao(texto, habilidade, variacoes_habilidades):
    variacoes = variacoes_habilidades.get(habilidade, [habilidade])

    for variacao in variacoes:
        if encontrar_habilidade(texto, variacao):
            return True

    return False

def obter_habilidades(categoria, skills, variacoes_habilidades):
    habilidades = []

    for skill in skills[categoria]:
        habilidade_oficial = skill

        for nome, variacoes in variacoes_habilidades.items():
            if skill in variacoes:
                habilidade_oficial = nome
                break

        if habilidade_oficial not in habilidades:
            habilidades.append(habilidade_oficial)

    return habilidades

def obter_todas_habilidades(skills, variacoes_habilidades):
    todas_habilidades = []

    for categoria in skills:
        habilidades = obter_habilidades(
            categoria,
            skills,
            variacoes_habilidades
        )

        for skill in habilidades:
            if skill not in todas_habilidades:
                todas_habilidades.append(skill)

    return todas_habilidades

if total_vagas > 0:
    print("\nRequisitos:")

    print(f"Total de vagas analisadas: {total_vagas}")

    todas_habilidades = obter_todas_habilidades(skills, variacoes_habilidades)

    ranking_geral = {}
    
    for skill in todas_habilidades:
        contador = 0

        for vaga in vagas:
            if encontrar_variacao(vaga["requisitos"] + " " + vaga["diferenciais"], skill, variacoes_habilidades):

                contador += 1

        if contador > 0:
            frequencia = (contador / total_vagas) * 100

            ranking_geral[skill] = {
                "quantidade": contador,
                "frequencia": frequencia
            }

    for categoria in skills:
        ranking_categoria = {}

        print(f"\n====== {categoria.upper()} ======")
        habilidades = obter_habilidades(categoria, skills, variacoes_habilidades)

        for skill in habilidades:

            contador = 0
            for vaga in vagas:
                if encontrar_variacao(vaga["requisitos"] + " " + vaga["diferenciais"], skill, variacoes_habilidades):
                    contador = contador + 1
            
            if contador > 0:
                frequencia = (contador / total_vagas) * 100

                ranking_categoria[skill] = {
                    "quantidade": contador,
                    "frequencia": frequencia
                }

        ranking_ordenado = sorted(ranking_categoria.items(), key=lambda item:item[1]["frequencia"], reverse=True)

        nome_arquivo = f"skill_vaga_{categoria}.csv"

        with open(nome_arquivo, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["Habilidade", "Quantidade", "Frequência"])

            for skill, dados in ranking_ordenado:
                writer.writerow([skill, dados["quantidade"], round(dados["frequencia"], 1)])


        for skill, dados in ranking_ordenado:
            print(f"{skill} - quantidade: {dados['quantidade']} - {dados['frequencia']:.1f}%")

    print(f"\n====== ***RANKING GERAL*** ======")

    ranking_geral_ordenado = sorted(ranking_geral.items(), key=lambda item: item[1]["frequencia"], reverse=True)

    for skill, dados in ranking_geral_ordenado:
        print(f"{skill} - quantidade: {dados['quantidade']} - {dados['frequencia']:.1f}%")

    with open("skill_vaga_geral.csv", "w", newline="",encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")

        writer.writerow(["Habilidade", "Quantidade", "Frequência"])

        for skill, dados in ranking_geral_ordenado:
            writer.writerow([skill, dados['quantidade'], round(dados['frequencia'], 1)])

else:
    print("Não há vagas cadastradas para analisar.")


print("\n====== TESTE DE RECONHECIMENTO ======")

print(encontrar_habilidade("Conhecimento em Python", "python"))
print(encontrar_habilidade("Conhecimento em APIs REST", "api"))
print(encontrar_habilidade("Experiência com comunicação", "comunicação"))
print(encontrar_habilidade("Conhecimento em programação", "python"))

print(encontrar_variacao("Conhecimento em APIs REST", "api", variacoes_habilidades))

texto_teste = "Conhecimento em API e experiência com APIs"

print(encontrar_variacao(texto_teste, "api", variacoes_habilidades))