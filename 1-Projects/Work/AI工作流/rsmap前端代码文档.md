# rsmap AI 参考文档

> 本文档供 AI 快速理解项目结构、API 和修改方式。

## 1. 项目概述

rsmap 是一个基于 React (Class Component) + DeckGL + react-map-gl 的室内地图工具库。
- 技术栈: React 16+, TypeScript, DeckGL, Mapbox GL, Turf.js, lodash, umi-request
- 构建: father-build (库打包), dumi (文档)
- 坐标系: WGS84 (外部接口) ↔ GCJ02 (中国模式内部渲染)

## 2. 目录结构

```
src/
├── index.tsx          # 主入口 - RSMap 类组件 + 所有导出
├── types.ts           # 全局类型定义
├── services.ts        # API 请求层 (umi-request)
├── utils/
│   ├── index.ts       # 通用工具函数 (楼层计算/过滤/比较)
│   ├── geo.tsx        # WGS84↔GCJ02 坐标转换
│   ├── cache.ts       # LRU 缓存实现
│   ├── svg.tsx        # SVG 图标生成 (POI/定位/方向)
│   └── mobile.js      # 移动端检测
├── components/        # 底层渲染组件 (直接操作 DeckGL Layer)
│   ├── BaseMap/       # 底图瓦片 (高德/腾讯/Mapbox)
│   ├── Bitmap/        # BitmapLayer 图片叠加
│   ├── Cluster/       # 聚合点 (supercluster)
│   ├── GeojsonEditor/ # GeoJSON 编辑器 (nebula.gl)
│   ├── Heatmap/       # HeatmapLayer 热力图
│   ├── Line/          # PathLayer 线段 (含箭头/标记)
│   ├── Marker/        # IconLayer 标记点
│   ├── Mesh/          # SimpleMeshLayer 网格模型
│   ├── Model/         # ScenegraphLayer 3D 模型
│   ├── Overlay/       # HTML Overlay 浮层
│   ├── Path/          # PathLayer 路径
│   ├── Point/         # ScatterplotLayer 散点
│   ├── Polygon/       # SolidPolygonLayer 多边形
│   ├── Popup/         # HTML Popup 弹窗
│   ├── Selection/     # 框选组件
│   ├── StaticMap/     # 静态地图样式
│   ├── Text/          # TextLayer 文字标注
│   ├── Tile3D/        # Tile3DLayer 3D 瓦片
│   ├── MapPolygon/    # Mapbox GL 原生多边形
│   ├── MapboxText/    # Mapbox GL 原生文字
│   ├── MapboxBitmap/  # Mapbox GL 原生图片
│   ├── Controller/    # 控制器容器
│   └── RSIcon/        # 图标组件
├── modules/           # 业务模块 (带楼层/空间感知)
│   ├── Wrapper/       # DeckGL 容器 (核心)
│   ├── Spaces/        # 空间列表管理
│   ├── Floor/         # 楼层渲染
│   ├── Map/           # 地图数据加载 (Polygon/Poi/Text/Scenegraph/Bitmap/StaticMap)
│   ├── Point/         # 带楼层的散点
│   ├── Line/          # 带楼层的线段
│   ├── Polygon/       # 带楼层的多边形
│   ├── Marker/        # 带楼层的标记
│   ├── Text/          # 带楼层的文字
│   ├── Overlay/       # 带楼层的浮层
│   ├── Heatmap/       # 带楼层的热力图
│   ├── Bitmap/        # 带楼层的图片叠加
│   ├── BitmapEditor/  # 图片编辑器 (含测距)
│   ├── Cluster/       # 带楼层的聚合
│   ├── Mesh/          # 带楼层的网格模型
│   ├── Model/         # 带楼层的3D模型
│   ├── Tile3D/        # 带楼层的3D瓦片
│   ├── Selection/     # 带楼层的框选
│   ├── Shelf/         # 货架渲染
│   ├── Popup/         # 带楼层的弹窗
│   ├── Location/      # 定位点渲染 (含方向/跟随)
│   ├── History/       # 历史轨迹回放
│   ├── MultiFloorLine/# 跨楼层线段
│   ├── GeojsonEditor/ # 带楼层的GeoJSON编辑
│   ├── NearbyEvent/   # 附近事件检测
│   ├── Layers/        # 自定义图层管理
│   ├── MapPolygon/    # 带楼层的Mapbox多边形
│   ├── MapBitmap/     # 带楼层的Mapbox图片
│   ├── Space/         # 单空间管理
│   ├── Toolbar/       # 工具栏
│   ├── Controller/    # 控制器集合
│   ├── Platform/      # 平台业务组件集合
│   └── Navigation/    # 导航引擎
```

## 3. 核心入口 - RSMap (src/index.tsx)

React Class Component，是整个库的主组件。

### RSMapProps (关键属性)

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| server | string | '' | API 服务器地址 |
| appId | string | - | 应用 ID (鉴权) |
| appSecret | string | - | 应用密钥 (鉴权) |
| spaceState | SpaceStateData | undefined | 当前空间/楼层状态 (受控) |
| defaultViewport | ViewportData | undefined | 初始视角 |
| location | LocationData | undefined | 当前定位数据 |
| locationMode | number | 0 | 定位模式 |
| showChinaMode | boolean | true | 启用 GCJ02 偏移 |
| showDarkMode | boolean | false | 暗色模式 |
| show3Dimension | boolean | true | 3D 视角 |
| showMultipleFloor | boolean | false | 多楼层同时显示 |
| showMixEnvironment | boolean | false | 混合环境 (室内外同显) |
| showSatellite | boolean | false | 卫星图 |
| showBaseMap | boolean | true | 显示底图 |
| showFloor/showPolygon/showText/showPoi/showScenegraph/showBitmap/showStaticMap | boolean | true | 各图层开关 |
| enableXxxController | boolean | 各异 | 各控制器开关 |
| backgroundColor | string | - | 背景色 |
| mapFilter | object | - | 空间/楼层/地图过滤器 |
| locale | string | 'zh-CN' | 语言 |

### RSMapProps (回调)

| 回调 | 参数 | 说明 |
|------|------|------|
| onViewportChange | (viewport: ViewportData) | 视角变化 |
| onSpaceStateChange | (spaceState: SpaceStateData \| undefined) | 空间状态变化 |
| onSpaceClick | (space: SpaceData \| undefined) | 空间点击 |
| onFloorClick | (feature) | 楼层点击 |
| onPolygonClick | (feature) | 多边形点击 |
| onPoiClick | (feature) | POI 点击 |
| onSingleClick / onDoubleClick / onRightClick / onLongClick | (e) | 通用点击事件 |
| onInitSuccess / onInitFail | () | 初始化回调 |

### RSMap 实例方法

| 方法 | 参数 | 返回 | 说明 |
|------|------|------|------|
| onViewportChange | (viewport: ViewportData) | void | 编程式视角切换 (支持 spaceId/floor/mapId) |
| recenter | () | void | 回到默认视角 |
| getBounds | () | [[lng,lat],[lng,lat]] \| null | 获取当前可视范围 |
| fitBounds | (bounds, options?) | {lng,lat,zoom} \| null | 计算适配视角 |
| pickObject | ({longitude, latitude}) | object | 拾取指定坐标的对象 |
| resize | () | void | 触发地图重绘 |

### ViewportData 切换逻辑

`onViewportChange` 支持以下特殊字段:
- `spaceId`: 切换到指定空间 (自动加载楼层、调整视角)
- `floor`: 切换楼层
- `mapId`: 通过地图 ID 切换 (自动解析 spaceId + floor)
- `instance: true`: 立即执行 (否则缓存等初始化完成后执行)
- `gcj02: true`: 坐标已是 GCJ02，不再转换
- `skipable: true`: 过渡动画中可跳过

## 4. 类型系统 (src/types.ts)

### 核心数据类型

```typescript
SpaceData        // 空间: {id, name, latitude, longitude, properties, geometry, visibility}
FloorData        // 楼层: {id, floor, spaceId, name, maps, geom, height, current, visibility}
MapData          // 地图: {id, spaceId, floor, name, image, imageBounds, mapStyle, visibility}
CoordinateData   // 坐标: {longitude, latitude, altitude?, timestamp?, animation?}
PositionData     // 位置: CoordinateData + {spaceId?, mapId?, floor?, level?, x?, y?, z?}
LocationData     // 定位: PositionData + {direction?}
ViewportData     // 视角: {spaceId?, floor?, mapId?, zoom?, longitude?, latitude?, pitch?, bearing?, ...}
SpaceStateData   // 空间状态: {space?: SpaceData, floors?: FloorData[]}
FeatureData      // GeoJSON Feature
PoiData          // POI: PositionData + {id, name, icon, properties, type}
ScenegraphData   // 3D模型: PositionData + {id, name, model, properties}
TextData         // 文字: PositionData + {id, name, properties: {size, height, color}}
ShelfData        // 货架: {id, position, direction, length, width, height, color, levels}
```

## 5. API 服务层 (src/services.ts)

使用 umi-request，带 LRU 缓存 (localStorage via xijs store)。

| 函数 | 端点 | 缓存 | 说明 |
|------|------|------|------|
| initService(server, appId, appSecret) | - | - | 初始化请求实例 + 拦截器 |
| getSpaces() | GET /api/spaces | 否 | 获取所有空间 |
| getSpace(spaceId) | GET /api/spaces/:id | 否 | 获取单个空间 |
| getFloors(spaceId, cache?) | GET /api/spaces/:id/floors | 10分钟 | 获取楼层列表 |
| getFloor(spaceId, floor) | GET /api/spaces/:id/floors/:floor | 否 | 获取单个楼层 |
| getMap(mapId) | GET /api/maps/:id | 否 | 获取地图 |
| getPolygons(mapId, cache?) | GET /api/maps/:id/polygons | 30分钟 | 获取多边形 |
| getPois(mapId, cache?) | GET /api/maps/:id/pois | 30分钟 | 获取 POI |
| getTexts(mapId, cache?) | GET /api/maps/:id/texts | 30分钟 | 获取文字 |
| getScenegraphs(mapId, cache?) | GET /api/maps/:id/scenegraphs | 30分钟 | 获取3D模型 |

请求头: `{apiKey: appId, apiSecret: appSecret}`
响应格式: `{success, code, data, errorMessage}` → 自动解包返回 data

## 6. 工具函数 (src/utils/)

### geo.tsx - 坐标转换
```typescript
wgs84toGcj02(coordinate, showChinaMode?) // WGS84→GCJ02，支持数组和对象格式
gcj02toWgs84(coordinate, showChinaMode?) // GCJ02→WGS84，迭代逼近法
initGeoCache(server)                      // 初始化坐标偏移缓存
downloadGeoCache(longitude, latitude)     // 下载区域偏移数据
```

### index.ts - 通用工具
```typescript
excludeProps(props, excludeFunction?)  // 排除内部属性
includeProps(props, excludeFunction?)  // 只保留内部属性
compareProps(props1, props2)           // 比较属性 (排除内部属性)
compareSpaceState(s1, s2)              // 比较空间状态 (space.id + floor)
renderChildren(children, props, nested) // 递归注入 props 到子组件
compareFloor(floor1, floor2)           // 比较楼层 (含子楼层)
compareMainFloor(floor1, floor2)       // 比较主楼层
getMainFloor(floor)                    // 获取主楼层号
getSubFloor(floor)                     // 获取子楼层号
checkMainFloor(floor)                  // 是否为主楼层
sortFloors(floor1, floor2)             // 楼层排序
calFloorHeight(floor, current, floors) // 计算楼层3D高度偏移
getFloors(floors)                      // 展开楼层列表 (含子楼层)
hexToRgb(hex) / rgbToHex(rgb)         // 颜色转换
filterSpace/filterFloor/filterMap      // 按 mapFilter 过滤
isEmpty(value)                         // 增强的空值检查
```

### 楼层编号规则
- 简单楼层: floor=1 表示1楼, floor=-1 表示B1
- 复合楼层: floor=100 表示1楼主层, floor=110 表示1楼子层+1, floor=101 表示1楼子层-1
- getMainFloor(150) → 1, getSubFloor(150) → 5

## 7. 模块通用模式

所有 modules/ 下的组件遵循相同模式:

```typescript
class ModuleName extends Component<ModuleProps> {
  // 1. 坐标转换
  getPosition = (feature) => {
    const pos = this.props.getPosition(feature);
    return wgs84toGcj02({longitude: pos[0], latitude: pos[1]}, showChinaMode);
    // 3D模式: altitude = (pos[2] || 0) + floor.height
    // 2D模式: altitude = (pos[2] || 0) / 1000
  }

  // 2. 楼层感知的位置
  getFloorPosition = (floor) => (feature) => {
    // 同 getPosition，但使用指定楼层的 height
  }

  // 3. defaultFollow - 自动跟随视角
  defaultFollow = () => {
    // 计算数据边界 → fitBounds → onViewportChange
  }

  render() {
    // 渲染逻辑:
    // a. 无 spaceId/floor 时: 渲染为室外图层
    // b. showMixEnvironment 时: 渲染其他空间的数据 (半透明)
    // c. 当前空间楼层: 遍历 floors，过滤 current 或 showMultipleFloor
    // d. 每个楼层渲染对应的 Component
  }
}
```

### 模块 Props 通用字段

| 字段 | 说明 |
|------|------|
| mapId / floor / spaceId | 指定数据所属的地图/楼层/空间 |
| defaultFollow | 自动调整视角到数据范围 |
| data | 数据数组 |
| getPosition | 从数据项提取坐标 `(d) => [lng, lat, alt?]` |
| 其余 | 透传给底层 Component |

## 8. 各模块详细说明

### Point (散点图层)
- 底层: ScatterplotLayer
- Props: `{data, getPosition, getRadius, getFillColor, getLineColor, radiusUnits, ...}`
- 默认: `getPosition = (d) => d.position`, `radiusUnits = 'pixels'`

### Line (线段图层)
- 底层: PathLayer
- Props: `{data, getPath, getColor, getWidth, widthUnits, ...}`
- 默认: `getPath = (d) => d.path`
- 特殊: 支持 `showArrow` 箭头, `markers` 标记点

### Polygon (多边形图层)
- 底层: SolidPolygonLayer
- Props: `{data, getPolygon, getFillColor, getLineColor, getElevation, extruded, ...}`
- 默认: `getPolygon = (d) => d.polygon`

### Marker (标记图层)
- 底层: IconLayer
- Props: `{data, getPosition, getIcon, getSize, getAngle, ...}`
- 默认: `getPosition = (d) => d.position`

### Text (文字图层)
- 底层: TextLayer
- Props: `{data, getPosition, getText, getSize, getColor, ...}`
- 默认: `getPosition = (d) => d.position`

### Overlay (HTML浮层)
- 底层: 自定义 HTML Overlay
- Props: `{data, getPosition, children (render prop), ...}`
- 默认: `getPosition = (d) => d.position`

### Heatmap (热力图)
- 底层: HeatmapLayer
- Props: `{data, getPosition, getWeight, radiusPixels, intensity, ...}`
- 默认: `getPosition = (d) => d.position`

### Bitmap (图片叠加)
- 底层: BitmapLayer
- Props: `{image, bounds, ...}`
- bounds 格式: `[minLng, minLat, maxLng, maxLat]` 或 `[[lng,lat],[lng,lat],[lng,lat],[lng,lat]]`

### Cluster (聚合)
- 底层: supercluster
- Props: `{data, getPosition, getId, options: {maxZoom, radius}, exceptionIds, children (render prop)}`
- children 接收: `{count, position, data, clusterId, index}`

### Mesh (网格模型)
- 底层: SimpleMeshLayer
- Props: `{data, mesh, getPosition, getColor, getOrientation, getScale, ...}`

### Model (3D模型)
- 底层: ScenegraphLayer
- Props: `{data, scenegraph, getPosition, getOrientation, getScale, ...}`

### GeojsonEditor (GeoJSON编辑器)
- 底层: nebula.gl EditableGeoJsonLayer
- Props: `{data, mode, onEdit, selectedFeatureIndexes, ...}`
- Mode: DrawPointMode, DrawLineStringMode, DrawPolygonMode, ModifyMode, TranslateMode, ...

### BitmapEditor (图片编辑器)
- 组合: Bitmap + GeojsonEditor + Overlay
- Props: `{image, data, ...GeojsonEditorProps}`
- 静态属性: `BitmapEditor.Mode` 包含所有编辑模式 + MeasureDistanceMode

### Selection (框选)
- Props: `{data, getPosition, onSelect, ...}`

### Shelf (货架)
- 底层: SimpleMeshLayer (3D) / Polygon (2D)
- Props: `{data, getPosition, getDirection, getLength, getWidth, getHeight, getColor, ...}`

### Tile3D (3D瓦片)
- 底层: Tile3DLayer
- Props: `{data (tileset URL), ...}`

### Popup (弹窗)
- 底层: HTML Overlay
- Props: `{data, getPosition, children, ...}`

### MultiFloorLine (跨楼层线段)
- 渲染跨越多个楼层的路径线段
- Props: `{data, getPath, ...LineProps}`

### History (历史轨迹)
- 轨迹回放组件
- Props: `{data, playing, speed, onProgress, ...}`

### Location (定位)
- 渲染定位点 + 方向 + 精度圈
- 自动从 props.location 获取位置

### NearbyEvent (附近事件)
- 检测定位点附近的 POI 事件
- 触发 onNearbyEvent 回调

## 9. Controller 控制器

| 控制器 | 功能 |
|--------|------|
| FloorController | 楼层切换 |
| ReturnController | 返回室外 |
| ZoomController | 缩放 +/- |
| RecenterController | 回到中心 |
| FullscreenController | 全屏切换 |
| DimensionController | 2D/3D 切换 |
| MultipleFloorController | 多楼层显示开关 |
| CompassController | 指南针 (旋转复位) |
| LocationController | 定位模式切换 |
| SatelliteController | 卫星图切换 |
| RulerController | 比例尺显示 |

## 10. Platform 平台业务组件

Platform 是面向业务的高级组件集合:

```typescript
Platform.Markers<T>     // 标记点管理 (聚合+方向+点击)
Platform.Marker<T>      // 单个标记 (头像/图标/闪烁/弹窗)
Platform.ClusterMarker  // 聚合标记 (展开列表)
Platform.Cluster        // 聚合容器
Platform.FencePolygon   // 围栏多边形 (颜色/3D/提示)
Platform.ZonePolygon    // 区域多边形
Platform.Shelves        // 货架集合 (距离过滤/层级弹窗)
Platform.Shelf          // 单个货架
Platform.Points         // 分组散点
Platform.GatherPoint    // 聚集事件点 (告警颜色)
Platform.Directions     // 方向箭头
```

## 11. Navigation 导航引擎

纯逻辑类 (非 React 组件)，实现路径导航。

```typescript
const nav = new Navigation();

// 初始化
nav.init(routeData, {
  distTolerance: 3,        // 偏离容忍距离(米)
  autoReroute: true,       // 自动重新规划
  locationUpdateTime: 120, // 更新间隔(ms)
  locationObjectType: 'walk' // 'walk' | 'drive'
});

// 事件监听
nav.on(NavigationEvent.locationUpdate, (pos: AdjustPositionData) => {});
nav.on(NavigationEvent.guideStateUpdate, (state: GuideStateData) => {});
nav.on(NavigationEvent.showManeuver, (maneuver, segmentIndex, batchIndex) => {});
nav.on(NavigationEvent.playTTS, (type: ManeuverType, distance: number) => {});
nav.on(NavigationEvent.reroute, (location, batchIndex) => {});
nav.on(NavigationEvent.stop, () => {});

// 控制
nav.start(GuideStateType.EMULATE); // 模拟导航
nav.start(GuideStateType.REAL);    // 实时导航
nav.setCurrentLocation(rawLocation, toMars?); // 更新定位 (实时模式)
nav.pause();
nav.resume();
nav.stop();
nav.destroy();
```

### ManeuverType 转向类型
`straight, left, right, slight_left, slight_right, sharp_left, sharp_right, uturn, stair_enter, stair_exit, destination, midpoint, begin`

### RouteData 结构
```typescript
{
  distance: number,
  duration: number,
  segments: [{
    name, distance, duration, batchIndex,
    maneuver: {type: ManeuverType, location, floor?},
    coordinates: [{longitude, latitude, altitude, spaceId, floor, sublevel}],
    floors: {[floorNum]: true}
  }],
  destinations: [RoutePositionData]
}
```

## 12. 导出清单

### 默认导出
- `RSMap` - 主组件

### 带楼层模块
Popup, GeojsonEditor, BitmapEditor, Selection, Heatmap, History, Overlay, Point, Marker, Line, MultiFloorLine, Polygon, Model, Mesh, Cluster, Bitmap, Text, Tile3D, StaticMap, Shelf, NearbyEvnet, Location

### 原生组件 (不带楼层)
PolygonComponent, HeatmapComponent, ModelComponent, MeshComponent, PointComponent, MarkerComponent, PathComponent, GeojsonEditorComponent, SelectionComponent, BitmapComponent, LineComponent, OverlayComponent, TextComponent, Tile3DComponent

### Platform
Platform (含 Markers, Marker, ClusterMarker, Cluster, FencePolygon, ZonePolygon, GatherPoint, Shelf, Shelves, Directions, Points)

### Navigation
Navigation, PathRoute, parseCustomRouteData, calcDistance, NavigationEvent, ManeuverType, GuideStateType

### 工具
wgs84toGcj02, gcj02toWgs84, WebMercatorViewport, FlyToInterpolator, LinearInterpolator, TRANSITION_EVENTS, ToolItem

## 13. 修改指南

### 添加新图层模块
1. 在 `src/components/` 创建底层组件 (封装 DeckGL Layer)
2. 在 `src/modules/` 创建业务模块 (添加楼层/空间感知)
3. 在 `src/index.tsx` 导入并导出

### 修改坐标转换
- 文件: `src/utils/geo.tsx`
- 所有模块的 `getPosition` 方法都调用 `wgs84toGcj02`

### 修改 API
- 文件: `src/services.ts`
- 请求拦截器在 `initService` 中配置

### 修改控制器
- 目录: `src/modules/Controller/XxxController/`
- 在 `src/modules/Controller/index.tsx` 导出
- 在 `src/index.tsx` 的 render 中条件渲染

### 修改楼层逻辑
- 楼层计算: `src/utils/index.ts` 的 `calFloorHeight`, `sortFloors`, `getFloors`
- 楼层切换: `src/index.tsx` 的 `onFloorChange`, `onViewportChangeInstance`
- 楼层加载: `src/index.tsx` 的 `loadFloors`
