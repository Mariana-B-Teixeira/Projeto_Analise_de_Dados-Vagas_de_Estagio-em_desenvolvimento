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
        "database"
    ],
    "modelagem de dados": [
        "modelagem de dados",
        "modelagens de dados"
    ],
    "pipeline de dados": [
        "pipeline de dados",
        "pipelines de dados"
    ],
    "engenharia de dados": [
        "engenharia de dados",
        "engenharias de dados"
    ],
    "large language model": [
        "large language model",
        "large language models"
    ],
    "agentes de ia": [
        "agente de ia",
        "agentes de ia"
    ],
    "ai agents": [
        "ai agent",
        "ai agents"
    ],
    "agentes inteligentes": [
        "agente inteligente",
        "agentes inteligentes"
    ],
    "api": [
        "api",
        "apis"
    ],
    "api rest": [
        "api rest",
        "apis rest"
    ],
    "rest api": [
        "rest api",
        "rest apis"
    ],
    "teste": [
        "teste",
        "testes"
    ],
    "teste unitário": [
        "teste unitário",
        "testes unitários"
    ],
    "automação de processo": [
        "automação de processo",
        "automação de processos"
    ],
    "workflow": [
        "workflow",
        "workflows"
    ],
    "integração": [
        "integração",
        "integrações"
    ],
    "join": [
        "join",
        "joins"
    ],
    "consulta sql": [
        "consulta sql",
        "consultas sql"
    ],
    "trabalho em equipe": [
        "trabalho em equipe",
        "trabalhos em equipe",
        "trabalho em equipa",
        "teamwork"
    ],
    "colaboração": [
        "colaboração",
        "colaborações"
    ],
    "resolução de problemas": [
        "resolução de problema",
        "resolução de problemas",
        "problem solving"
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

        for skill, dados in ranking_ordenado:
                print(f"{skill} - quantidade: {dados['quantidade']} - {dados['frequencia']:.1f}%")

    print(f"\n====== ***RANKING GERAL*** ======")

    ranking_geral_ordenado = sorted(ranking_geral.items(), key=lambda item: item[1]["frequencia"], reverse=True)

    for skill, dados in ranking_geral_ordenado:
        print(f"{skill} - quantidade: {dados['quantidade']} - {dados['frequencia']:.1f}%")

else:
    print("Não há vagas cadastradas para analisar.")