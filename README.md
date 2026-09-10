# Projecto Demo — Sessão Práctica de SonarQube

Pequeno projecto em Python, partilhado pelo Grupo 3 com toda a turma, para a sessão
prática de análise de qualidade de código com o SonarQube. Usar o **mesmo código**
em todos os grupos garante que os resultados (bugs, vulnerabilidades, duplicação,
cobertura) são directamente comparáveis na fase de discussão.

## Estrutura

```
src/
  calculadora.py    # somas e médias sobre listas de preços/quantidades
  utilizadores.py   # autenticação simples de utilizadores
  inventario.py     # cálculo do valor total de um inventário
tests/
  test_calculadora.py
```

## Preparar o ambiente

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Correr os testes com cobertura

```bash
pytest --cov=src --cov-report=xml
```

Isto gera o `coverage.xml` que o SonarQube Scanner lê para calcular a cobertura.

## Configurar e correr a análise

1. Editar `sonar-project.properties`:
   - `sonar.projectKey` — substituir `grupoX` pelo número do vosso grupo (evita
     colisões entre grupos no mesmo servidor).
   - `sonar.host.url` — endereço da instância do SonarQube da aula.
   - `sonar.token` — token gerado em *My Account → Security*.
2. Correr a análise a partir da raiz do projecto:

```bash
sonar-scanner
```

3. Abrir o projecto no dashboard do SonarQube e explorar Bugs, Vulnerabilidades,
   Code Smells, Duplicação e Cobertura.
