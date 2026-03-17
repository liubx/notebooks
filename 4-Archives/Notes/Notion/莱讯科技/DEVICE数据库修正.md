# DEVICE数据库修正

```sql
-- 定位标签类型

TRUNCATE "$schema".t_module_type;
TRUNCATE "$schema".t_tag_type;
TRUNCATE "$schema".r_tag_type_module_type;

-- 莱讯科技
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('5232cc91-ccb1-4bfc-9b41-571ab1a778d7', 'GPS', 'GPS定位', 'RS_GPS');
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('055fb429-5f8b-43f4-8f04-0bd927b29a7b', '蓝牙', 'iBeacon定位', 'RS_BLUETOOTH');
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('f70b6bbf-a973-48e5-adf7-5b687142745f', 'GPS', '手机GPS定位', 'RS_MOBILE_GPS');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('RS-M100', '71ff0740-fef3-4fd7-a73b-c0ea594d9241', '室内外高精度标签', '莱讯科技', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (1, '71ff0740-fef3-4fd7-a73b-c0ea594d9241', '5232cc91-ccb1-4bfc-9b41-571ab1a778d7');  -- RS_GPS
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (2, '71ff0740-fef3-4fd7-a73b-c0ea594d9241', '379b0440-a1ec-4d96-adcd-971e59806db2'); -- REDPOINT_UWB
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('RS-B100', 'a8733207-0abe-413f-869a-fc08a9067e66', '蓝牙标签', '莱讯科技', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (3, 'a8733207-0abe-413f-869a-fc08a9067e66', 'ba69a30d-dd49-4072-ad6d-8d768117818c'); -- RADIOLAND_BLUETOOTH
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('RS-M110', '8822e343-115c-4f10-9cea-e1d50bcaf3d1', '室内外工牌', '莱讯科技', '工牌');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (4, '8822e343-115c-4f10-9cea-e1d50bcaf3d1', '5232cc91-ccb1-4bfc-9b41-571ab1a778d7'); -- RS_GPS
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (5, '8822e343-115c-4f10-9cea-e1d50bcaf3d1', 'b0739ade-bf32-4055-af2c-67b78ad66f92'); -- CORELOCATION_BLUETOOTH_AOA
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('RS-M120', '9ce70f5b-91e7-4035-b2bc-8619823a65f9', '通用高精度标签', '莱讯科技', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (6, '9ce70f5b-91e7-4035-b2bc-8619823a65f9', 'b0739ade-bf32-4055-af2c-67b78ad66f92'); -- CORELOCATION_BLUETOOTH_AOA
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (7, '9ce70f5b-91e7-4035-b2bc-8619823a65f9', '379b0440-a1ec-4d96-adcd-971e59806db2'); -- REDPOINT_UWB
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('RS-M130', '7176f656-8ebc-43fc-b4d0-97da94126f4c', '通用定位标签', '莱讯科技', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (8, '7176f656-8ebc-43fc-b4d0-97da94126f4c', '5232cc91-ccb1-4bfc-9b41-571ab1a778d7'); -- RS_GPS
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (9, '7176f656-8ebc-43fc-b4d0-97da94126f4c', 'ba69a30d-dd49-4072-ad6d-8d768117818c'); -- RADIOLAND_BLUETOOTH
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('RS-MOBILE', 'c1414739-3aa4-46da-8b3f-7e61261feacd', '定位手机', '莱讯科技', '手机');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (10, 'c1414739-3aa4-46da-8b3f-7e61261feacd', 'b0739ade-bf32-4055-af2c-67b78ad66f92'); -- CORELOCATION_BLUETOOTH_AOA
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('RS-MOBILE-GPS', 'aa6b70c0-bf68-49fa-ac58-4875794ed617', '定位手机', '莱讯科技', '手机');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (11, 'aa6b70c0-bf68-49fa-ac58-4875794ed617', 'f70b6bbf-a973-48e5-adf7-5b687142745f'); -- RS_MOBILE_GPS

-- 核心互联
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('b0739ade-bf32-4055-af2c-67b78ad66f92', '蓝牙', '蓝牙AOA定位', 'CORELOCATION_BLUETOOTH_AOA');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('CL-TA10', '5de98972-1ec1-4816-90ae-265c04e74e8c', '佩戴型信标', '核心物联', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (12, '5de98972-1ec1-4816-90ae-265c04e74e8c', 'b0739ade-bf32-4055-af2c-67b78ad66f92');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('CL-TA20', 'aa46e1b6-daa6-47c1-b0c3-2ce4c69061cb', '腕带型信标', '核心物联', '手环');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (13, 'aa46e1b6-daa6-47c1-b0c3-2ce4c69061cb', 'b0739ade-bf32-4055-af2c-67b78ad66f92');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('CL-TA30', 'cd98ab08-0dfd-4e98-85ad-a990e14387aa', '工牌型信标', '核心物联', '工牌');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (14, 'cd98ab08-0dfd-4e98-85ad-a990e14387aa', 'b0739ade-bf32-4055-af2c-67b78ad66f92');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('CL-TA40', '4fbc21d2-92d5-4b09-add5-f7a48020a986', '资产型信标', '核心物联', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (15, '4fbc21d2-92d5-4b09-add5-f7a48020a986', 'b0739ade-bf32-4055-af2c-67b78ad66f92');

-- 红点科技
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('379b0440-a1ec-4d96-adcd-971e59806db2', 'UWB', 'UWB定位', 'REDPOINT_UWB');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('GPL-V7', 'b0739ade-bf32-4055-af2c-67b78ad66f91', '通用标签', 'Redpoint', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (16, 'b0739ade-bf32-4055-af2c-67b78ad66f91', '379b0440-a1ec-4d96-adcd-971e59806db2');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('PBG-V7', '59806ad1-2d4a-4ce4-b92f-15257cd6de8d', '智能工牌标签', 'Redpoint', '工牌');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (17, '59806ad1-2d4a-4ce4-b92f-15257cd6de8d', '379b0440-a1ec-4d96-adcd-971e59806db2');

-- Radioland
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('ba69a30d-dd49-4072-ad6d-8d768117818c', '蓝牙', 'iBeacon定位', 'RADIOLAND_BLUETOOTH');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('nRF52832', 'dc66ead9-410e-4fdb-a064-816733be2149', 'T8手环', 'Radioland', '手环');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (18, 'dc66ead9-410e-4fdb-a064-816733be2149', 'ba69a30d-dd49-4072-ad6d-8d768117818c');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('nRF52810', '5a1cdc88-5c6b-4361-b3c9-53ea8bb2d8b5', 'X5标签', 'Radioland', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (19, '5a1cdc88-5c6b-4361-b3c9-53ea8bb2d8b5', 'ba69a30d-dd49-4072-ad6d-8d768117818c');

-- 长兴视通
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('f0599ed9-d37c-4aac-a94f-2482cb91c2df', '蓝牙', '蓝牙定位', 'AMWHERE_BLUETOOTH');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('AMW-B100', '23d4e91e-4db9-4047-8186-fc2d0a9b43d3', '蓝牙资产定位标签', '长兴视通', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (20, '23d4e91e-4db9-4047-8186-fc2d0a9b43d3', 'f0599ed9-d37c-4aac-a94f-2482cb91c2df');
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('3f3a84d7-dfab-4f41-801b-871a752bc11b', 'GPS', 'GPS定位', 'AMWHERE_GPS');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('AMW-G100', 'c8228472-5338-49e3-8ffc-5d8d33cbf39a', 'GPS定位标签', '长兴视通', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (21, 'c8228472-5338-49e3-8ffc-5d8d33cbf39a', '3f3a84d7-dfab-4f41-801b-871a752bc11b');
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('4dd8dc63-4d2d-49ed-aa8a-d30f2e91c036', 'GPS', 'GPS定位', 'AMWHERE_GPS_MQ');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('AMW-G110', 'b0acea21-09ca-412d-b180-18f93d6270e8', 'GPS定位标签', '长兴视通', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (22, 'b0acea21-09ca-412d-b180-18f93d6270e8', '4dd8dc63-4d2d-49ed-aa8a-d30f2e91c036');
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('4f1e3cc9-2cb1-4cc4-a5a2-76ad359747d7', 'RTK', 'RTK定位', 'AMWHERE_RTK');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('AMW-G200', '246ab1de-be38-4f97-82ec-7ce91573745f', 'RTK定位标签', '长兴视通', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (23, '246ab1de-be38-4f97-82ec-7ce91573745f', '4f1e3cc9-2cb1-4cc4-a5a2-76ad359747d7');

-- Quuppa
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('47a2ec0f-9476-403b-b291-4e887af222d8', '蓝牙', '蓝牙AOA定位', 'QUUPPA_BLUETOOTH_AOA');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('JW-T1901A', 'fcd0481f-4b2e-4a5f-9265-d27d8f923680', '资产标签', 'Quuppa', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (24, 'fcd0481f-4b2e-4a5f-9265-d27d8f923680', '47a2ec0f-9476-403b-b291-4e887af222d8');

-- 嘉兴太和
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('8129e71d-9f17-422e-8fea-07eb2d606813', '蓝牙', '蓝牙AOA定位', 'TAIHE_BLUETOOTH_AOA');
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('6e50f246-ef9f-43a6-bb4b-03b96f84988c', 'UWB', 'UWB定位', 'TAIHE_UWB');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('TH-TAGC-D', 'cc84f037-69d0-4c88-9e7f-fe272a082b94', '双模卡片式标签', '嘉兴太和', '标签');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('TH-MINIAPP', 'a90bbc3d-93bd-488e-b1ce-e89c840f9a8a', '小程序定位', '嘉兴太和', '小程序');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (25, 'cc84f037-69d0-4c88-9e7f-fe272a082b94', '8129e71d-9f17-422e-8fea-07eb2d606813');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (26, 'cc84f037-69d0-4c88-9e7f-fe272a082b94', '6e50f246-ef9f-43a6-bb4b-03b96f84988c');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (27, 'a90bbc3d-93bd-488e-b1ce-e89c840f9a8a', '8129e71d-9f17-422e-8fea-07eb2d606813');

-- 华云时空
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('0315ed7f-0053-4680-a466-53ba733acfb6', 'UWB', 'UWB定位', 'HUAYUEN_UWB');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('HY-100', 'd6dd2d31-ff59-4034-a9a6-a937798dcea2', 'UWB标签', '华云时空', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (28, 'd6dd2d31-ff59-4034-a9a6-a937798dcea2', '0315ed7f-0053-4680-a466-53ba733acfb6');

-- 凡星位航
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('0a8ba25b-88dc-4bd0-9e51-44a8ad45eed6', 'UWB-AOA', 'UWB-AOA定位', 'ORDISTAR_UWB_AOA');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('ORDISTART-001', '1f403815-7f87-4f0f-872d-4a88d6c90d68', '定位标签', '凡星位航', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (29, '1f403815-7f87-4f0f-872d-4a88d6c90d68', '0a8ba25b-88dc-4bd0-9e51-44a8ad45eed6');

-- 梦芯科技
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('5e687dca-1da5-472d-9f8d-52bd35cb16ae', 'RTK', 'RTK定位', 'MENGXIN_RTK');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('S105L', '5fab1558-1220-4cc1-90fa-ad91213749be', '车载定位器', '梦芯科技', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (30, '5fab1558-1220-4cc1-90fa-ad91213749be', '5e687dca-1da5-472d-9f8d-52bd35cb16ae');

-- 麦钉科技
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('e95652d9-5f78-428d-914f-5d16ab8e8939', '地磁', '地磁定位', 'MADINAT_DICI');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('MADINAT-MOBILE', '79df8151-7f51-4159-8d23-fa86d27b1205', '定位手机', '麦钉科技', '手机');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (31, '79df8151-7f51-4159-8d23-fa86d27b1205', 'e95652d9-5f78-428d-914f-5d16ab8e8939');

-- 费曼科技
INSERT INTO "$schema".t_module_type ("id", "name", "technique", "uid") VALUES ('b6c41add-1ba3-4dc7-9b57-0b8c8f8640ef', 'RTK', 'RTK定位', 'FEIMAN_RTK');
INSERT INTO "$schema".t_tag_type ("uid", "id", "name", "brand", "type") VALUES ('FM-100', '13e36a45-bc68-41b8-960f-b3fe23764b9f', 'RTK定位标签', '费曼科技', '标签');
INSERT INTO "$schema".r_tag_type_module_type ("id", "tag_type_id", "module_type_id") VALUES (32, '13e36a45-bc68-41b8-960f-b3fe23764b9f', 'b6c41add-1ba3-4dc7-9b57-0b8c8f8640ef');

-- 定位基站类型

TRUNCATE "$schema".t_anchor_type;

-- 核心物联
INSERT INTO "$schema".t_anchor_type ("uid", "id", "name", "brand") VALUES ('CL-GA10-P', '27d10e58-fc2f-4c10-8ce7-03b83992dd56', 'AOA室内定位基站', '核心物联');
INSERT INTO "$schema".t_anchor_type ("uid", "id", "name", "brand") VALUES ('CL-GB20-P', 'd92b8d4e-6075-4f31-916b-1258dc33e462', 'AOA室内定位从基站', '核心物联');

-- 红点科技
INSERT INTO "$schema".t_anchor_type ("uid", "id", "name", "brand") VALUES ('CMA-V7', '379b0440-a1ec-4d96-adcd-971e59806dbe', '吸顶式基站', 'Redpoint');
INSERT INTO "$schema".t_anchor_type ("uid", "id", "name", "brand") VALUES ('PoEA-V7IS', 'b0739ade-bf32-4055-af2c-67b78ad66f9a', '防爆基站WMAV7', 'Redpoint');
INSERT INTO "$schema".t_anchor_type ("uid", "id", "name", "brand") VALUES ('PoEA-V4-2', '50f38705-6af0-448c-831e-b12a1e15a5b4', '壁挂式基站', 'Redpoint');

DROP TRIGGER IF EXISTS set_tag_module_type_update_timestamp ON "$schema".r_tag_type_module_type;

ALTER TABLE "$schema".r_tag_type_module_type DROP CONSTRAINT IF EXISTS r_tag_type_module_type_pkey;
ALTER TABLE "$schema".r_tag_type_module_type ADD CONSTRAINT r_tag_type_module_type_pkey PRIMARY KEY (id);

ALTER TABLE "$schema".t_tag_bind_history DROP CONSTRAINT IF EXISTS t_tag_bind_history_pkey;
ALTER TABLE "$schema".t_tag_bind_history ADD CONSTRAINT t_tag_bind_history_pkey PRIMARY KEY (id);

ALTER TABLE "$schema".t_anchor ALTER COLUMN geom TYPE geometry(PointZ) USING ST_Force3D(geom);
ALTER TABLE "$schema".t_camera ALTER COLUMN geom TYPE geometry(PointZ) USING ST_Force3D(geom);
```