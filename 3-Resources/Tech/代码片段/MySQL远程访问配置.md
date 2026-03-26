---
title: MySQL 远程访问配置
type: code-snippet
tags:
  - tech/mysql
  - tech/数据库
created: 2022-01-01
modified: 2022-01-01
---

# MySQL 远程访问配置

## MySQL 远程访问配置

```sql
SHOW databases;
SELECT user, host FROM mysql.user WHERE user='root';
SELECT user, host FROM mysql.user WHERE user='root' AND host='127.0.0.1';
UPDATE mysql.user SET Host='%' WHERE user='root' AND host='127.0.0.1';
```

## PostgreSQL max_connections

```sql
ALTER SYSTEM SET max_connections = 500;
show max_connections;
```
