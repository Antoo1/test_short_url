DROP TABLE IF EXISTS tshort_urls CASCADE;


create table if not exists tshort_urls
(
    id           serial primary key,
    source_url varchar(255) not null,
    short_url varchar(30) not null default substring(md5(random()::text),1,20),
    UNIQUE(source_url)
);

CREATE UNIQUE INDEX ui_short ON tshort_urls (short_url);
