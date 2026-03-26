---
title: PostGIS坐标转换与空间操作
type: code-snippet
tags:
  - tech/postgis
  - tech/gis
  - source/yuque
created: 2026-03-16
modified: 2026-03-16
---

# PostGIS坐标转换与空间操作

## 坐标系转换函数

完整的 PostGIS 坐标转换函数库，支持 WGS84/GCJ02/BD09/CGCS2000 互转。

### 使用方式

```sql
-- WGS84转GCJ02（火星坐标）
SELECT geoc_wgs84togcj02(geom) FROM test_table;
-- GCJ02转WGS84
SELECT geoc_gcj02towgs84(geom) FROM test_table;
-- WGS84转BD09（百度坐标）
SELECT geoc_wgs84tobd09(geom) FROM test_table;
-- BD09转WGS84
SELECT geoc_bd09towgs84(geom) FROM test_table;
-- CGCS2000转GCJ02
SELECT geoc_cgcs2000togcj02(geom) FROM test_table;
-- GCJ02转BD09
SELECT geoc_gcj02tobd09(geom) FROM test_table;
```


## 坐标迁移操作（旧架构）

Polygon 备份 → 转换 → 更新中心点的完整流程：

```sql
-- 1. 备份原表
ALTER TABLE schema.polygon RENAME TO polygon_backup;

-- 2. 创建新表并导入（转换到 4326）
CREATE TABLE schema.polygon (
  id character varying,
  geom geometry(MULTIPOLYGON, 4326),
  name character varying(80), type character varying(80),
  model character varying(80), rotation real, altitude real
);
INSERT INTO schema.polygon (id, geom, name, type, model, rotation, altitude)
SELECT uuid_generate_v4(), ST_Transform(geom, 4326), name, type, model, rotation, altitude
FROM schema.polygon_backup;

-- 3. 转换到火星坐标
UPDATE schema.polygon SET geom = ST_SetSRID(geoc_wgs84togcj02(geom), 4326);

-- 4. 更新地图中心点和边界
UPDATE public.map SET
  map_xmax=t.xmax, map_xmin=t.xmin, map_ymax=t.ymax, map_ymin=t.ymin,
  longitude=t.longitude, latitude=t.latitude
FROM (
  SELECT ST_XMax(c) xmax, ST_XMin(c) xmin, ST_YMax(c) ymax, ST_YMin(c) ymin,
         ST_X(ST_Centroid(c)) longitude, ST_Y(ST_Centroid(c)) latitude
  FROM (SELECT ST_Transform(ST_Collect(geom), 3857) c FROM schema.polygon) t
) t WHERE public.map.schema_name = 'schema';

-- 回滚
DROP TABLE IF EXISTS schema.polygon;
ALTER TABLE schema.polygon_backup RENAME TO polygon;
```

## 空间变换操作

### 移动

```sql
UPDATE schema.t_polygon SET geom = ST_Transform(
  ST_SetSRID(ST_Affine(ST_Transform(ST_SetSRID(geom,4326),3857),
    1,0,0, 0,1,0, 0,0,1, deltaX,deltaY,0), 3857), 4326)
WHERE map_id = ?;
```

### 缩放

```sql
UPDATE schema.t_polygon SET geom = ST_Affine(geom,
  scaleFactor,0,0, 0,scaleFactor,0, 0,0,1, 0,0,0)
WHERE map_id = ?;
```

### 旋转（绕中心点）

```sql
-- 先获取中心点
SELECT ST_X(ST_Centroid(geom)), ST_Y(ST_Centroid(geom)) FROM schema.t_space WHERE id=?;

-- 旋转 polygon/floor/space
UPDATE schema.t_polygon SET geom = ST_Transform(
  ST_SetSRID(ST_Rotate(ST_Transform(ST_SetSRID(geom,4326),3857),
    pi()/2, ST_Transform(ST_SetSRID(ST_MakePoint(lon,lat),4326),3857)), 3857), 4326)
WHERE map_id = ?;
```

## 空间查询

### 获取指定范围内的点

```sql
SELECT ST_Force2D(location) FROM t_position
WHERE ST_Contains(
  ST_Polygon('LINESTRING(x1 y1, x2 y2, x3 y3, x4 y4, x1 y1)'::geometry, 4326),
  location);
```

### 移动电子围栏到火星坐标

```sql
UPDATE schema.t_fence SET geom = ST_SetSRID(geoc_wgs84togcj02(geom), 4326);
```

### 偏移位置数据到火星坐标

```sql
UPDATE schema.t_position SET location = ST_SetSRID(geoc_wgs84togcj02(location), 4326);
```

### 生成 UUID

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();
```