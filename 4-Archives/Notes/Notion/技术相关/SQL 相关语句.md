# SQL 相关语句

// TimescaleDB 详细教程

https://www.allbs.cn/posts/21383/index.html

```bash
DO $$ DECLARE
schemaname NAME;
BEGIN
		FOR schemaname IN (
		SELECT
			nspname 
		FROM
			pg_namespace 
		WHERE
			nspname NOT LIKE'pg_%' 
			AND nspname NOT LIKE'_timescaledb%' 
			AND nspname NOT LIKE'timescaledb%' 
			AND nspname <> 'public' 
			AND nspname <> 'information_schema' 
			AND nspname <> 'toolkit_experimental' 
			AND nspname <> 'topology' 
		)
		LOOP
			raise info '%', schemaname;
			EXECUTE format ( 'ALTER TABLE "%I".t_trackable ADD COLUMN IF NOT EXISTS state smallint NOT NULL DEFAULT 0;', schemaname );
		END LOOP;
END;
$$ LANGUAGE plpgsql;
```

```sql
ALTER TABLE csg_wmsnavigation.t_anchor DROP COLUMN IF EXISTS longitude,latitude,altitude;

// 删除 Schema

DROP SCHEMA IF EXISTS banma_factory CASCADE; 
DROP SCHEMA IF EXISTS bjgcys_gcys CASCADE; 
DROP SCHEMA IF EXISTS cnnc_qshdz CASCADE; 
DROP SCHEMA IF EXISTS csg_wmsnavigation CASCADE;
DROP SCHEMA IF EXISTS demo_platform CASCADE;
DROP SCHEMA IF EXISTS demo_tydqys CASCADE;
DROP SCHEMA IF EXISTS dfcy_dfcy CASCADE;
DROP SCHEMA IF EXISTS dwstd_wkwxwly CASCADE;
DROP SCHEMA IF EXISTS feiman_rtk CASCADE;
DROP SCHEMA IF EXISTS finsiot_cdfyst CASCADE;
DROP SCHEMA IF EXISTS hongjin_dianchang CASCADE;
DROP SCHEMA IF EXISTS kanglida_tadiao CASCADE; 
DROP SCHEMA IF EXISTS kanglida_vehicle CASCADE;  
DROP SCHEMA IF EXISTS lanbufu_lanbufu CASCADE;
DROP SCHEMA IF EXISTS madinat_sewd CASCADE;
DROP SCHEMA IF EXISTS madinat_test CASCADE;
DROP SCHEMA IF EXISTS madinat_xmc CASCADE;
DROP SCHEMA IF EXISTS panasonic_showroom CASCADE;
DROP SCHEMA IF EXISTS philips_idc CASCADE;
DROP SCHEMA IF EXISTS reliablesense_ceshi CASCADE;
DROP SCHEMA IF EXISTS reliablesense_demo CASCADE;
DROP SCHEMA IF EXISTS reliablesense_hbhospital CASCADE;
DROP SCHEMA IF EXISTS reliablesense_huatu CASCADE;
DROP SCHEMA IF EXISTS reliablesense_testlzjc CASCADE;
DROP SCHEMA IF EXISTS yitong_tracking CASCADE;
DROP SCHEMA IF EXISTS zhenhua_zhtl CASCADE;
DROP SCHEMA IF EXISTS zhonghe_zhonghe CASCADE;
 

// 删除 map.public

DROP TABLE IF EXISTS public."t_project" CASCADE; 
DROP TABLE IF EXISTS public."t_icon" CASCADE;
DROP TABLE IF EXISTS public."t_label_style" CASCADE;   
DROP TABLE IF EXISTS public."t_model" CASCADE;    
DROP TABLE IF EXISTS public."t_polygon_type" CASCADE;   
DROP TABLE IF EXISTS public."t_polygon_style" CASCADE;     

SELECT * FROM timescaledb_information.jobs;

// 删除 position.job

SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='banma_factory' AND proc_name='online_time_count'; 
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='csg_wmsnavigation' AND proc_name='online_time_count'; 
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='demo_platform' AND proc_name='online_time_count'; 
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='feiman_rtk' AND proc_name='online_time_count'; 
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='kanglida_tadiao' AND proc_name='online_time_count'; 
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='lanbufu_lanbufu' AND proc_name='online_time_count'; 
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='madinat_xmc' AND proc_name='online_time_count'; 
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='madinat_test' AND proc_name='online_time_count';  
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='madinat_sewd' AND proc_name='online_time_count'; 
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='philips_idc' AND proc_name='online_time_count'; 
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='reliablesense_ceshi0a' AND proc_name='online_time_count';  
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='reliablesense_demo' AND proc_name='online_time_count';   
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='reliablesense_hbhospital' AND proc_name='online_time_count';   
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='reliablesense_huatu' AND proc_name='online_time_count';   
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='yitong_tracking' AND proc_name='online_time_count';   
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='zhenhua_zhtl' AND proc_name='online_time_count';    
SELECT delete_job(job_id) FROM timescaledb_information.jobs WHERE proc_schema='zhonghe_zhonghe' AND proc_name='online_time_count';      
```

洗煤厂数据

```sql
INSERT INTO "public"."t_company" ("id", "uid", "name", "email", "phone", "address", "postal_code", "create_time", "update_time", "website", "description") VALUES ('5f305da1-d60e-4c0d-8799-cc5de8e2c31c', 'madinat', '北京麦钉艾特科技有限公司', 'business@madintech.com', '18612275407', '北京市东城区和平里南街3号', NULL, '2021-08-09 06:22:27.248578+00', '2021-08-09 06:22:27.248578+00', 'www.madintech.com', '北京麦钉艾特科技有限公司成立于2016年，是一家以地磁为核心的室内外一体化位置服务提供商，全国高新技术企业，国家实时定位技术标准制定工作组成员。');

INSERT INTO "public"."t_user" ("uid", "create_time", "id", "username", "name", "email", "phone", "avatar", "password", "role_id", "company_id", "replace_password", "update_time") VALUES ('0000', '2021-08-09 04:04:24.549756+00', '6adf60d4-aaa9-424d-8596-f4351859be74', 'madintech', '麦丁艾特账号', 'madinat@gmail.com', '12341243351', NULL, '$2a$12$qRi3R34z11xAUUWVyb3PnOe/yjquaFN6S20RtRiNqCsTdRAcTnlb6', 'c9e847e6-6d75-4f1c-ac76-e016413c4896', '5f305da1-d60e-4c0d-8799-cc5de8e2c31c', false, '2021-08-09 04:04:24.549756+00');
```

导出t_position

```sql
DROP TRIGGER IF EXISTS ts_insert_blocker ON "$schema".t_position;
SELECT create_hypertable(relation => '"$schema".t_position', time_column_name => 'device_time', if_not_exists => TRUE, migrate_data => TRUE);
SELECT add_retention_policy(relation => '"$schema".t_position', drop_after => INTERVAL '1 year', if_not_exists => TRUE);

SELECT * FROM _timescaledb_catalog.hypertable;

DROP TRIGGER IF EXISTS ts_insert_blocker ON t_position;
SELECT create_hypertable(relation => 't_position', time_column_name => 'device_time', if_not_exists => TRUE, migrate_data => TRUE);
SELECT add_retention_policy(relation => 't_position', drop_after => INTERVAL '1 year', if_not_exists => TRUE);
SELECT add_job('online_time_count','1d', initial_start=>'2022-06-10 24:00:00+08', config=>'{"gap":"1"}');

```

修改连接数

```bash
ALTER SYSTEM SET max_connections = 500;
show max_connections;
```

修改数据清除任务

```bash
SELECT remove_retention_policy(relation => 't_position');
SELECT add_retention_policy(relation => 't_position', drop_after => INTERVAL '3 months', if_not_exists => TRUE);
```

清理数据

```bash

// device
TRUNCATE t_anchor, t_tag, t_module, t_tag_bind_history, t_camera, r_tag_type_module_type RESTART IDENTITY;

// device.ext
TRUNCATE t_tag RESTART IDENTITY;

// position
TRUNCATE r_fence_bind, r_group_label, r_trackable_fence, r_trackable_group, r_trackable_label, r_trackable_tag, r_trackable_trackable_type, t_alarm, t_attendance, t_fence, t_fence_access_history, t_fence_access_statistic, t_fence_history, t_group, t_mileage, t_notification, t_position, t_trackable RESTART IDENTITY;

TRUNCATE t_tag RESTART IDENTITY;

// position.ext
TRUNCATE t_alarm, t_fence, t_tag, t_trackable, t_trackable_allow_record, t_trackable_record, t_trackable_trip, t_trackable_trip_data RESTART IDENTITY;

```