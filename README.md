
# Fraude Zero: Arquitetura de Dados e Análise de Fraudes
Estrutura do pipeline AWS e Dashboard Power BI

## Projeto
Este projeto apresenta a construção de um pipeline de dados focado em Análise de Fraudes. O objetivo principal foi aplicar na prática os conceitos de Engenharia e Análise de Dados, construindo uma infraestrutura real e funcional na nuvem.

Além do desafio arquitetural com ferramentas de ponta, o projeto mergulha na investigação analítica do comportamento de transações ilícitas, servindo como base prática para entender como sistemas de pagamento podem ser explorados e qual a importância de controles antifraude no mercado financeiro.

## Arquitetura e Tecnologias
A esteira de dados:
*   **Medalhões (AWS S3):** Armazenamento em camadas (Bronze, Silver e Gold) simulando um ambiente real.
*   **ETL (AWS Glue & Python):** Scripts desenvolvidos em Python para limpeza, transformação e agregação dos dados.
*   **Consulta (AWS Athena):** Disponibilização dos dados da camada Gold para consumo via SQL.
*   **Conexão:** Integração do Athena com o Power BI através de drivers ODBC e Access Keys.
*   **Visualização (Power BI & DAX):** Dashboard focado em volumetria temporal, KPIs de risco e perfil de ataque.

## Dashboard

*   **Análise Temporal:** Mapeamento do "Relógio do Crime" com "picos" de ataque por dia e hora.
*   **KPIs de Risco:** Redução do volume de fraudes YoY provando a eficácia dos bloqueios.

## Como rodar o projeto

Para replicar este laboratório ou explorar a modelagem localmente, siga os passos abaixo:

### 1. Pré-requisitos
* Conta ativa na **AWS** (para configurar e rodar os serviços S3, Glue e Athena).
* Instalação do **Power BI Desktop**.
* Driver **ODBC do Amazon Athena** instalado na sua máquina (necessário apenas se quiser atualizar os dados do dashboard).

### 2. Executando o Pipeline de Dados (ETL)
* Os scripts de extração, tratamento e estruturação de dados (desenvolvidos em Python para o AWS Glue) estão localizados na pasta `scripts/`.
* Esses scripts são responsáveis por pegar os dados transacionais brutos, aplicar as regras de limpeza e enviá-los para a camada Gold no S3, deixando tudo pronto para o consumo do Athena.

### 3. Visualizando o Dashboard
* Abra o arquivo `.pbix` localizado na pasta principal do repositório.
* **Para atualizar a base:** Caso queira rodar uma nova carga de dados, será necessário configurar as suas *Access Keys* da AWS nas configurações de Fonte de Dados do Power BI, permitindo que a conexão via ODBC consulte as tabelas diretamente no Athena.
