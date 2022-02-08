create table todolist (
id serial primary key,
task text not null,
created_at timestamp not null,
updated_at timestamp not null
);