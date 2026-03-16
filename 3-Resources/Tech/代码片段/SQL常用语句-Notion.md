---
title: SQL常用语句（Notion迁移）
type: code-snippet
language: sql
tags:
  - code-snippet
  - 技术/数据库/SQL
source: "[[4-Archives/Notion/技术相关/SQL 相关语句 35c696dbd3344c0887636f409c4f9ffe]]"
created: 2026-03-16
---

> 从 Notion 迁移，包含 TimescaleDB、PostgreSQL 常用操作。

## TimescaleDB

```sql
-- 创建 hypertable
DROP TRIGGER IF EXISTS ts_insert_blocker ON "$schema".t_position;
SELECT create_hypertable(
  relation => '"$schema".t_position',
  time_column_name => 'device_time',
  if_not_exists => TRUE,
  migrate_data => TRUE
);

-- 数据保留策略
SELECT add_retention_policy(relation => '"$schema".t_position', drop_after => INTERVAL '1 year', if_not_exists => TRUE);
SELECT remove_retention_policy(relation => 't_position');
SELECT add_retention_policy(relation => 't_position', drop_after => INTERVAL '3 months', if_not_exists => TRUE);

-- 定时任务
SELECT add_job('online_time_count','1d', initial_start=>'2022-06-10 24:00:00+08', config=>'{"gap":"1"}');
SELECT * FROM timescaledb_information.jobs;
```

## PostgreSQL

```sql
-- 修改连接数
ALTER SYSTEM SET max_connections = 500;
show max_connections;

-- 批量 Schema 操作（遍历所有业务 Schema）
DO $ DECLARE schemaname NAME;
BEGIN
  FOR schemaname IN (
    SELECT nspname FROM pg_namespace
    WHERE nspname NOT LIKE 'pg_%'
    AND nspname NOT LIKE '_timescaledb%'
    AND nspname <> 'public'
    AND nspname <> 'information_schema'
  ) LOOP
    EXECUTE format('ALTER TABLE "%I".t_trackable ADD COLUMN IF NOT EXISTS state smallint NOT NULL DEFAULT 0;', schemaname);
  END LOOP;
END; $ LANGUAGE plpgsql;
```

## MySQL

```sql
-- 远程访问
SELECT user, host FROM mysql.user WHERE user='root';
UPDATE mysql.user SET Host='%' WHERE user='root' AND host='127.0.0.1';
FLUSH PRIVILEGES;

-- 创建用户
CREATE USER 'user'@'%' IDENTIFIED BY '[password]';
GRANT ALL PRIVILEGES ON *.* TO 'user'@'%' IDENTIFIED BY '[password]';
```

## 数据清理

```sql
-- Device 服务
TRUNCATE t_anchor, t_tag, t_module, t_tag_bind_history, t_camera, r_tag_type_module_type RESTART IDENTITY;

-- Position 服务
TRUNCATE r_fence_bind, r_group_label, r_trackable_fence, r_trackable_group, r_trackable_label, r_trackable_tag, r_trackable_trackable_type, t_alarm, t_attendance, t_fence, t_fence_access_history, t_fence_access_statistic, t_fence_history, t_group, t_mileage, t_notification, t_position, t_trackable RESTART IDENTITY;
```
