CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    tipo_usuario INTEGER NOT NULL DEFAULT 0,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_evento TEXT NOT NULL,
    local_evento TEXT NOT NULL,
    horario DATE NOT NULL, 
    organizadora TEXT NOT NULL,
    preco INTEGER,
    id_usuario INTEGER NOT NULL,
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS locais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rua TEXT NOT NULL,
    bairro TEXT NOT NULL,
    cep TEXT NOT NULL,
    proximo_evento TEXT NOT NULL,
    max_pessoas  INTEGER
);


INSERT INTO eventos (nome_evento, local_evento, horario, organizadora,preco, id_usuario) VALUES
('Festival de Música de BH', 'Praça da Estação','19:00' , 'Cultura BH',100, 1),
('Feira de Tecnologia 2025', 'Expominas','20:00', 'TechWorld',100, 2),
('BH Gastrô', 'Parque Municipal', '20:25','Sabores do Brasil',50, 3),
('Mostra de Cinema Mineiro', 'Cine Belas Artes','20:00' , 'Cine BH',0, 1),
('Encontro de Startups', 'WeWork Savassi', '20:25','Inova BH', 15,2),
('Corrida da Liberdade', 'Avenida Afonso Pena','21:00', 'Run BH',16, 4),
('Congresso de Arquitetura', 'Palácio das Artes','23:00', 'Construir Ideias',17, 3),
('Festival Literário BH', 'Biblioteca Pública Estadual','11:00', 'Palavra Viva',18, 2),
('ExpoAnime BH', 'Serraria Souza Pinto', '13:00', 'OtakuMG', 19,1),
('Simpósio de Saúde Mental', 'UFMG - Campus Pampulha','20:25', 'Saúde Plena',20, 4);