# MySQL

```sql
mysql -u root -p
4wwgloYnJKbOx9aRiZD5

SHOW databases;
```

```sql
SELECT user, host FROM mysql.user WHERE user='root';
```

```sql
SELECT user, host FROM mysql.user WHERE user='root' AND host='127.0.0.1';
```

```sql
UPDATE mysql.user SET Host='%' WHERE user='root' AND host='127.0.0.1';
```

```sql
UPDATE mysql.user SET Host='127.0.0.1' WHERE user='root' AND host='%';
```

```sql
flush privileges;
```

```sql
CREATE USER 'zentao'@'%' IDENTIFIED BY '4wwgloYnJKbOx9aRiZD5';
```

```sql
GRANT ALL PRIVILEGES ON *.* TO 'zentao'@'%' IDENTIFIED BY '4wwgloYnJKbOx9aRiZD5';
```