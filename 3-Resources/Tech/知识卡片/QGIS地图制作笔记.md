---
title: QGIS地图制作笔记
type: knowledge-card
tags:
  - tech/gis
  - tech/qgis
  - source/yuque
created: 2026-03-16
modified: 2026-03-16
---

# QGIS地图制作笔记

## 基础概念

一栋楼是一个 t_space，一层是一个 t_floor，一个 t_floor 有多个 t_map。

## DWG 导入

导入 DWG 文件时坐标参照系必须与 QGIS 地图坐标系保持一致。

- 如果导入时选择 4326，导入后改为 3857，DWG 图层将不显示
- 反之亦然

## 创建多地图结构

### 步骤

1. 在数据库连接右键「编辑连接」，勾选「同时列出不包含几何图形的表格」
2. 打开插件，添加地图
3. 创建 t_space（多边形），填写相应字段
4. 创建 t_floor（多边形），填写相应字段
5. 创建多个 t_map，对应 t_scenegraph 包中的 map id

## 多边形样式配置（新数据库）

### 1. 创建多边形样式

在 t_polygon_style 表中创建样式，生成 styleID：

```json
{
  "color": "#F4CDD5",
  "height": 1,
  "line_color": "#F99EAB",
  "bese_height": 0
}
```

### 2. 创建多边形类型

在 t_polygon_type 表中创建多边形类型和文字显示。在 QGIS 画多边形时复制对应的多边形 ID。

### 3. 画多边形

QGIS 里需要先建立好样式（不然多边形不会显示），然后开始画多边形。

## 文字样式配置

### 1. 创建文字样式

在 t_label_style 表中创建样式：

```json
{
  "size": 18,
  "color": "#000000FF",
  "height": 2,
  "max_zoom": 24,
  "min_zoom": 20
}
```

### 2. 关联到多边形

把文字样式的 ID 添加到 t_polygon_type 表中对应记录。

## 3D 地图元素

### 通用元素表

- `t_polygon_type`：用于添加与生成通用元素的 id（在 QGIS 画多边形时需要）
- `t_polygon_style`：用于修改多边形颜色、高度等数值
- `t_icon`：包括洗手间、电梯、楼梯、出口、大门

### 添加通用元素

1. 在通用表单找到元素（如「门」）的 id
2. 在 QGIS 画出代表该元素的多边形
3. 把 id 复制到多边形属性中

### 添加房间名称

在多边形的 `name` 字段添加房间名字，可在地图显示。

## 3D 模型添加

### 流程

1. 在 QGIS 画好 2D 地图，定义好多边形
2. 在 SketchUp 或 Blender 准备 3D 模型，导出 GLB 格式
3. 上传模型文件，获取对象地址
4. 在 pgAdmin 打开模型表（t_model），输入 name 和 src，生成模型 id
5. 在 QGIS 的 t_scenegraph 表中画出模型摆放位置，填入模型 id

### 模型字段

- name：模型名称
- src：模型文件地址
- 高度、角度等数值可在属性中修改

### 常见问题

- 模型中心点问题：SketchUp 导出后中心点可能不在模型下方中心，需要在 Blender 重新调整
- 材质问题：导出时可能出现材质丢失
- 与地图不匹配：需要根据实际显示调整参数
- 2D 模式下如何自动隐藏模型用多边形替代

---
*来源：语雀 - 莱讯科技技术分享/设计相关文档*
