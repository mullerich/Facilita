use sql10620948;

create table usuarios (
	id int not null auto_increment,
    nome varchar(64) not null,
    nascimento date not null,
    email varchar(256) not null,
    senha varchar(64) not null,
    
    tipo_conta longtext,
    cursos longtext,
    cidades longtext,
    notas longtext,
    turnos longtext,
    cotas longtext,
    grau longtext,
    pendencias longtext,
    
    primary key (id)
);