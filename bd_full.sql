-- MODELO COMPLETO DE DADOS

create table vagas (
	ID INT NOT NULL AUTO_INCREMENT,
	NU_ANO SMALLINT, 
    NU_EDICAO tinyint,
    CO_IES int,
    NO_IES varchar(120),
    SG_IES varchar(25),
    DS_ORGANIZACAO_ACADEMICA varchar(60),
    DS_CATEGORIA_ADM varchar(25),
    NO_CAMPUS varchar(100),
    NO_MUNICIPIO_CAMPUS varchar(40),
    SG_UF_CAMPUS varchar(2),
    DS_REGIAO varchar(15),
    CO_IES_CURSO varchar(10),
    NO_CURSO varchar(120),
    DS_GRAU varchar(30),
    DS_TURNO varchar(10),
    DS_PERIODICIDADE varchar(10),
    QT_SEMESTRE tinyint,
    QT_VAGAS_OFERTADAS tinyint,
    NU_PERCENTUAL_BONUS SMALLINT,
    TP_MODALIDADE varchar(70),
    DS_MOD_CONCORRENCIA tinytext,
    PESO_REDACAO tinyint,
    NOTA_MINIMA smallint,
    PESO_LINGUAGENS tinyint,
	NOTA_MINIMA_LINGUAGENS smallint,
	PESO_MATEMATICA tinyint,
	NOTA_MINIMA_MATEMATICA smallint, 
	PESO_CIENCIAS_HUMANAS tinyint,
	NOTA_MINIMA_CIENCIAS_HUMANAS smallint,
	PESO_CIENCIAS_NATUREZA tinyint,
	NOTA_MINIMA_CIENCIAS_NATUREZA smallint,
	NU_MEDIA_MINIMA_ENEM smallint,
	NU_NOTACORTE smallint,
    QT_INSCRICAO smallint,
    primary key (ID)
) default charset = utf8;

select * from vagas;
drop table vagas;
# truncate vagas;

select count(id) from vagas;