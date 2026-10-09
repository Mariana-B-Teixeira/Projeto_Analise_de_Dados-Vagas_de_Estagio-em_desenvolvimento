import csv

vagas = []

with open("vagas_estagio.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")

    for vaga in reader:
        vagas.append(vaga)

for vaga in vagas:
    print(vaga['empresa'],": ",vaga['cargo'], sep="")


print(len(vagas))

skills = {

    "dados": [
        "python",
        "sql",
        "excel",
        "análise de dados",
        "analise de dados",
        "data analysis",
        "analytics",
        "data analytics",
        "data science",
        "ciência de dados",
        "ciencia de dados",
        "pandas",
        "numpy",
        "estatística",
        "estatistica",
        "banco de dados",
        "database",
        "modelagem de dados",
        "etl",
        "pipeline de dados",
        "engenharia de dados"
    ],

    "inteligencia_artificial": [
        "inteligência artificial",
        "inteligencia artificial",
        "artificial intelligence",
        "ia generativa",
        "generative ai",
        "machine learning",
        "aprendizado de máquina",
        "aprendizado de maquina",
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
        "programacao orientada a objetos",
        "poo",
        "crud",
        "testes",
        "testes unitários",
        "testes unitarios",
        "debug",
        "debugging",
        "clean code"
    ],

    "automacao": [
        "automação",
        "automacao",
        "automação de processos",
        "automacao de processos",
        "n8n",
        "workflow",
        "workflows",
        "power automate",
        "integração",
        "integracao",
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
        "joins",
        "consultas sql"
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
        "comunicacao",
        "trabalho em equipe",
        "trabalho em equipa",
        "teamwork",
        "colaboração",
        "colaboracao",
        "proatividade",
        "organização",
        "organizacao",
        "raciocínio lógico",
        "raciocinio logico",
        "resolução de problemas",
        "resolucao de problemas",
        "problem solving",
        "pensamento crítico",
        "pensamento critico",
        "adaptabilidade",
        "autonomia",
        "liderança",
        "lideranca"
    ]
}

# # Tira duplicata.
# todas_skills = set()
# for categoria in skills:
#     for skill in skills[categoria]:
#         todas_skills.add(skill)


print("Requisitos:")

for categoria in skills:
    print(f"\n====== {categoria.upper()} ======")
    for skill in skills[categoria]:
        contador = 0
        for vaga in vagas:
            if skill in vaga["requisitos"].lower():
                contador = contador + 1
        
        if contador > 0:
            print(skill, ":", contador, sep="")