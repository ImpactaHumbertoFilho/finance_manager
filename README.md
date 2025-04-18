# 💰 Gerenciador Financeiro Pessoal

Projeto desenvolvido para fins acadêmicos, com o objetivo de aplicar os princípios de **Programação Orientada a Objetos (POO)** e práticas de organização de software, utilizando a arquitetura baseada em **Use Cases**, separando as responsabilidades em camadas distintas.

---

## 📌 Objetivo

Ajudar o usuário a organizar e acompanhar suas finanças pessoais, incluindo receitas, despesas, categorias e metas financeiras.

---

## 🧱 Arquitetura

O projeto está organizado nas seguintes camadas:

```
finance_manager/
├── application/       # Ponto de entrada (menu, interface CLI)
├── domain/            # Entidades e enums do domínio
├── usecases/          # Casos de uso que orquestram as regras
├── repository/        # Implementações de acesso a dados
├── crosscutting/      # Utilitários, exceções, logging etc.
├── tests/             # Testes automatizados
```

Essa separação permite:
- Melhor testabilidade
- Reaproveitamento e manutenção mais fáceis
- Independência de framework/banco/entrada

---

## 🧠 Funcionalidades

- [x] Cadastro de receitas e despesas
- [x] Classificação por categorias
- [x] Enumeração padronizada de formas de pagamento
- [x] Criação e acompanhamento de metas financeiras
- [x] Listagem e filtragem de transações por usuário
- [ ] Atualização e exclusão de registros
- [ ] Relatórios resumidos (em breve)

---

## 🔗 Tecnologias

- Python 3.11+
- SQLAlchemy ORM
- SQLite (persistência local)
- Enum, abc (POO avançada)
- Arquitetura com UseCases e Repositories

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/gerenciador-financeiro.git
cd gerenciador-financeiro
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode o projeto:

```bash
python application/main.py
```

---

## 🧪 Testes

```bash
pytest
```

Os testes cobrem entidades do domínio, regras de negócio e repositórios em memória.

---

## 👥 Integrantes

- Humberto Lisboa Leite Filho(RA: 2402662)
- Melissa Moura Ferreira (RA: 2403008)
- Jullya Mendonça Brandão Nigro (RA: 2402577)

---

## 📄 Licença

Projeto acadêmico — uso livre para fins educacionais.
