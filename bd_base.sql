create database adesao_sisu
default character set utf8
default collate utf8_general_ci;

use inscricoes_sisu;

create table dados_base (
	-- INFORMAÇÕES SOBRE FACULDADES, CAMPUS, REGIÕES, etc.
    NU_ANO smallint,
    NU_EDICAO tinyint,
    CO_IES int,
    NO_IES varchar(120),
    SG_IES varchar(12),
    DS_ORGANIZACAO_ACADEMICA varchar(60),
    DS_CATEGORIA_ADM varchar(25),
    NO_CAMPUS varchar(100),
    NO_MUNICIPIO_CAMPUS varchar(40),
    SG_UF_CAMPUS varchar(2),
    DS_REGIAO_CAMPUS varchar(15),
    CO_IES_CURSO varchar(10),
    NO_CURSO varchar(80),
    DS_GRAU varchar(15),
    DS_TURNO varchar(10)
) default charset = utf8;

alter table dados_base
modify column CO_IES_CURSO varchar(10) unique;

select count(NU_ANO) from dados_base;

select * from dados_base group by CO_IES_CURSO order by CO_IES_CURSO;

select * from dados_base where NO_CURSO = 'TURISMO' order by CO_IES_CURSO;

truncate dados_base;
