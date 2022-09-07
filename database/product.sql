show databases;
-- CRIAÇÃO DA TABELA E DO BANCO
create database products;

use products;

create table users(
	id_users bigint not null unique auto_increment,
	name varchar(100) not null,
    email varchar(100) not null,
    password varchar(300) not null,
    cpf varchar(12) not null unique,
    data_add datetime not null default now(),
    primary key(id_users)
);


describe users;

-- CONSULTAS
select * from users;


-- isercoes

insert into users(name, email, password, cpf)
values('admin', 'admin@email.com','admin',12345678910);