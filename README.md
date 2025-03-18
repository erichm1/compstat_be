# 🚀 CompStat (compstat_be/backend)

Este repositório contém o backend do projeto CompStat, uma aplicação desenvolvida para análise e estatísticas geoespaciais. 🗺️📊

## 🛠️ Tecnologias Utilizadas

- **🐍 Django** - Framework web para desenvolvimento robusto e escalável.
- **🔗 Django Rest Framework (DRF)** - Ferramenta para construção de APIs RESTful.
- **🐘 PostgreSQL** - Banco de dados relacional.
- **🌍 PostGIS** - Extensão para suporte a dados geoespaciais no PostgreSQL.

## ⚙️ Instalação e Configuração

### 📌 Requisitos
Antes de iniciar, certifique-se de ter instalado:
- 🐍 Python 3.9+
- 🐘 PostgreSQL com PostGIS ativado
- 📦 Virtualenv ou Docker (opcional)

### 📥 Passos para Configuração
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/compstat_be.git
   cd compstat_be
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure o banco de dados no `.env`:
   ```env
   DATABASE_URL=postgres://usuario:senha@localhost:5432/compstat
   ```

5. Aplique as migrações:
   ```sh
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:
   ```sh
   python manage.py runserver
   ```

## 📂 Estrutura do Projeto
```
compstat_be/
│── core/              # ⚙️ Configurações do projeto
│── api/               # 🌐 Endpoints e lógica de negócio
│── models/            # 🗄️ Modelos do banco de dados
│── serializers/       # 🔄 Serialização de dados
│── tests/             # ✅ Testes automatizados
│── Dockerfile         # 🐳 Configuração para contêiner Docker (se aplicável)
│── requirements.txt   # 📜 Dependências do projeto
│── manage.py          # 🚀 Gerenciador do Django
```

## 🧪 Executando os Testes
Para rodar os testes automatizados:
```sh
pytest
```

## 🔗 Endpoints Principais
- `GET /api/data/` - 📊 Retorna os dados processados.
- `POST /api/upload/` - 📤 Faz upload de arquivos para análise.
- `GET /api/statistics/` - 📈 Retorna estatísticas geoespaciais.

## 🤝 Contribuição
Contribuições são bem-vindas! Para contribuir:
1. Fork o repositório.
2. Crie uma branch (`feature-minha-mudanca`).
3. Commit suas alterações (`git commit -m "Minha contribuição"`).
4. Push para a branch (`git push origin feature-minha-mudanca`).
5. Abra um Pull Request.

## 📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.