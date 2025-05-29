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

Nosso banco de dados:
![{DCC82FCB-6E46-475F-B8CA-98BD499C543A}](https://github.com/user-attachments/assets/776fefc7-0ffc-4005-90ea-4701f80c65f4)

---

## 🧠 Funcionalidades

- [x] Cadastro de usuario
- [x] Criação e acompanhamento de metas financeiras
- [x] Criação de transações
- [x] Listagem e filtragem de transações por usuário
- [x] Detalhamento de transação com suas parcelas
- [x] Atualização e exclusão de registros
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
git clone https://github.com/ImpactaHumbertoFilho/finance_manager.git
cd finance_manager
cd src
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Rode o projeto:
```bash
#Certifique que esta na pasta "src"
python -m application/main.py
```
---

## 👥 Integrantes

- Humberto Lisboa Leite Filho(RA: 2402662)
- Melissa Moura Ferreira (RA: 2403008)
- Jullya Mendonça Brandão Nigro (RA: 2402577)

---

## 📄 Licença

Projeto acadêmico — uso livre para fins educacionais.
