CREATE DATABASE IF NOT EXISTS nome_database;

CREATE EXTERNAL TABLE IF NOT EXISTS nome_tabela_ouro (
    data_hora TIMESTAMP,
    data_transacao DATE,
    hora_transacao INT,
    dia_semana_numero INT,
    id_transacao STRING,
    nome_cliente STRING,
    mcc_codigo INT,
    estabelecimento STRING,
    final_cartao STRING,
    historico_transacoes STRING,
    localizacao STRING,
    origem_transacao STRING,
    dispositivo STRING,
    bandeira STRING,
    moeda STRING,
    valor_transacao DOUBLE,
    codigo_resposta INT,
    is_fraude INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ';' 
STORED AS TEXTFILE
LOCATION 'url-do-s3'
TBLPROPERTIES ('skip.header.line.count'='1');