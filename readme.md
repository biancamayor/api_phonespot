# 📱 **PhoneSpot API**

Bem-vindo ao repositório do **PhoneSpot API**, um projeto completo que combina web scraping, APIs e interface visual para oferecer uma solução robusta de comparação de preços de celulares.

---

## 🚀 **Descrição do Projeto**

A **PhoneSpot API** é uma aplicação que:
1. **Coleta dados de celulares**: Preços, nomes, marcas, códigos Anatel e links dos produtos são extraídos de grandes marketplaces como **Mercado Livre** e **Americanas** usando um projeto de **web scraping**.
2. **Armazena e trata dados**: Esses dados são salvos em um banco de dados relacional após tratamento, prontos para serem consumidos.
3. **Oferece uma API poderosa**: Diversos endpoints permitem consultar e filtrar celulares, como:
   - 🔍 **Busca por palavra-chave**.
   - 🏷️ **Filtros de preço** (mínimo e máximo).
   - 📑 **Busca por marcas específicas**.
   - 📊 **Ordenação de preços** (crescente ou decrescente).
   - 🔍 **Exibição de quais as marcas de celulares disponíveis na aplicação.**
4. **Interface visual com Streamlit**: Um **Data App** que fornece interação visual intuitiva para os usuários explorarem as funcionalidades da API.
5. **Containerização com Docker**: A aplicação pode ser executada em containers, tornando sua implantação simples e escalável.

---

## 🛠️ **Tecnologias Utilizadas**

- **Python**: Linguagem principal do projeto.
- **FastAPI**: Framework para desenvolvimento da API.
- **Streamlit**: Para criar a interface visual do usuário.
- **Docker**: Para containerização da aplicação.
- **BeautifulSoup e Requests**: Utilizados no projeto de web scraping.
- **Banco de dados relacional**: Para armazenar os dados coletados e tratados.
- **Threads em Python**: Utilizadas para paralelizar o web scraping, tornando o processo mais rápido e eficiente.

---

## ⚙️ **Como Configurar e Executar**

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/biancamayor/api_phonespot.git
   cd api_phonespot

2. **Configuração do ambiente**:
   Crie um arquivo .env com as variáveis de ambiente necessárias:
   - **CONNECTIONS_PATH** - Onde será armazenado o caminho para o arquivo json responsável por salvar o token de conexão com o banco de dados. Será nesse caminho que os endpoints terão acesso ao token gerado na conexão do endpoint get_db_connection.
   
   - **SECRET_KEY** - Chave única e secreta para gerar uma chave de criptografia resultante da combinação da SECRET_KEY e do IP de acesso do cliente. Utilizei para restringir quem pode utilizar a API, visto que a única forma de ela permitir acesso é com a combinação do meu ip permitido e a minha SECRET_KEY.

   - **allowed_ip** - IP permitido para acessar a API.

   Crie um arquivo db_credentials/credentials.json contendo suas credenciais de acesso ao banco de dados no seguinte formato:

   {
    "host": "host",
    "database": "database",
    "user": "user",
    "password": "password"
   }

   Crie um arquivo db_connections/connections.json para armazenar a conexão com o banco de dados gerada pelo endpoint get_db_connections. Nesse arquivo teremos o token gerado pela conexão e suas credenciais do banco. Dessa forma, todos os endpoints acessarão esse arquivo para utilizar a conexão criada.

   {
    "token_de_conexão_do_banco_de_dados": {
        "host": "host",
        "database": "database",
        "user": "user",
        "password": "password"
      }
   }





Insira os arquivos de credenciais no local indicado.
Build e execução com Docker:

Gere a imagem Docker:
bash
Copiar código
docker build -t phoneprice-api .  
Execute o container:
bash
Copiar código
docker run -d -p 8000:8000 --env-file .env -v /caminho/para/credenciais:/app/credenciais phoneprice-api  
Acesse a aplicação:

API: http://localhost:8000/docs
Data App: Será exibido no endereço configurado pelo Streamlit.
🌟 Funcionalidades Principais
Endpoints flexíveis para busca e filtragem de celulares.
Interface visual interativa para explorar a API.
Implementação em container para fácil escalabilidade.
🔒 Notas de Segurança
As credenciais de acesso e variáveis de ambiente não são expostas no repositório. É necessário fornecer seus próprios arquivos para rodar o container.
🖥️ Demonstração
Uma demonstração do Data App e da API está disponível aqui (adicione link para demonstração, caso exista).

🤝 Contribuições
Contribuições, sugestões e melhorias são bem-vindas! Sinta-se à vontade para abrir issues ou enviar PRs.

📞 Contato
Para mais informações ou dúvidas, entre em contato:

LinkedIn (adicione o link para o seu perfil).
E-mail.
📝 Licença
Este projeto é licenciado sob a MIT License.




