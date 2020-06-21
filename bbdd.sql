CREATE DATABASE IF NOT EXISTS notes_py;
USE notes_py;

CREATE TABlE users(
    id          int(25) auto_increment not null,
    name        varchar (100),
    lastname    varchar(255),
    email       varchar(255) not null,
    password    varchar(255) not null,
    created_at        date not null,
    CONSTRAINT pk_users PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABlE notes(
    id              int(25) auto_increment not null,
    user_id         int(25) not null,
    title           varchar(255) not null,
    description     MEDIUMTEXT,
    created_at      date not null,
    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_note_user FOREIGN KEY(user_id) REFERENCES users(id)
)ENGINE=InnoDb;