create table exchange_organizations
(
    id                    serial not null
        constraint exchange_organizations_pkey
            primary key,
    original_organization text,
    clean_organization    text,
    reviewed              boolean
);