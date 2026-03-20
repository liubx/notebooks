---
title: SQL常用语句（Notion迁移）
type: code-snippet
language: sql
tags:
  - tech/sql
  - tech/数据库
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

## PostGIS 3D 几何操作

```sql
-- 修改 geom 字段为 3D 类型
ALTER TABLE schema.t_polygon ALTER COLUMN geom TYPE geometry(PolygonZ) USING ST_Force3D(geom);
ALTER TABLE schema.t_anchor ALTER COLUMN geom TYPE geometry(PointZ) USING ST_Force3D(geom);
ALTER TABLE schema.t_camera ALTER COLUMN geom TYPE geometry(PointZ) USING ST_Force3D(geom);

-- 查询/更新 3D 几何
SELECT ST_AsText(geom) FROM schema.t_polygon WHERE id='xxx';
SELECT ST_GeometryType(geom) FROM schema.t_polygon WHERE id='xxx';
UPDATE schema.t_polygon SET geom=ST_SetSRID(ST_GeomFromGeoJSON('{"type":"Polygon","coordinates":[...]}'),4326) WHERE id='xxx';
```

## 设备类型初始化 SQL

```sql
-- 定位标签类型（示例：蓝牙 AOA）
INSERT INTO schema.t_module_type (id, name, technique, uid) VALUES ('uuid', '蓝牙', '蓝牙AOA定位', 'CORELOCATION_BLUETOOTH_AOA');
INSERT INTO schema.t_tag_type (uid, id, name, brand, type) VALUES ('CL-TA10', 'uuid', '佩戴型信标', '核心物联', '标签');
INSERT INTO schema.r_tag_type_module_type (id, tag_type_id, module_type_id) VALUES (1, 'tag_uuid', 'module_uuid');

-- 基站类型
INSERT INTO schema.t_anchor_type (uid, id, name, brand) VALUES ('CL-GA10-P', 'uuid', 'AOA室内定位基站', '核心物联');
```
