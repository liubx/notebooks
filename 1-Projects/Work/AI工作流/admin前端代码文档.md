# AI Codebase Guide - 室内外定位平台 Admin

## 项目概览
- 框架: Ant Design Pro + UmiJS 3 + DVA + React 17 + TypeScript
- UI: Ant Design 4 + ProComponents (ProTable/ProForm/ProLayout)
- 地图: rsmap (自研室内地图SDK)
- 状态管理: UmiJS plugin-model (hooks-based)
- 实时通信: STOMP over WebSocket
- 国际化: zh-CN(默认), zh-TW, en-US, ja-JP, fa-IR
- 样式: Less modules
- 请求: umi-request, 统一前缀 `/api`
- 路由: 约定式 + 配置式, 路径含 `/:project` 动态段

## 核心业务域
室内外定位系统管理后台，管理: 定位对象(Trackable)、标签(Tag)、基站(Anchor)、摄像头(Camera)、电子围栏(Fence)、统计区域(Zone)、告警(Alarm)、聚集事件(Gather)、地图空间(Space/Floor/Map)、项目(Project)、用户(User)、公司(Company)

---

## 目录结构

```
config/           # UmiJS配置
  config.ts       # 主配置: 路由/主题/代理/国际化/define全局常量
  routes.ts       # 路由表(含access权限控制)
  proxy.ts        # 代理配置(local/dev/test/oem/prod 5个环境)
  defaultSettings.ts  # ProLayout默认设置(暗色侧边栏, 主色#13C2C2)

src/
  app.tsx         # 运行时配置(核心入口)
  global.less     # 全局样式
  typings.d.ts    # 全局类型声明(rsmap类型re-export + 全局常量)
  types/          # 业务类型定义
  models/         # 全局状态(useModel hooks)
  services/       # API请求层
  hooks/          # 自定义hooks
  utils/          # 工具函数
  pages/          # 页面组件
  components/     # 通用组件
  locales/        # 国际化文件
```

---

## config/ 配置层

### config/config.ts
UmiJS主配置。关键define全局常量:
- `APP_ENV`: 环境标识(dev/test/oem/prod/local)
- `MAX_NUMBER`: 9999 (分页最大值)
- `RS_TRACKABLE` / `RS_TRACKABLE_MAPPER`: 定位对象多语言映射
- `ZH_CN/ZH_TW/EN_US/JA_JP/FA_IR`: locale常量

### config/routes.ts
路由表。所有项目内页面路径格式: `/:project/xxx`。权限通过 `access` 字段控制。
主要路由:
- `/login`, `/register` - 无layout
- `/:project/position` - 实时定位页
- `/:project/overview` - 总览仪表盘
- `/:project/trackable` - 定位对象(list/detail/group/label)
- `/:project/area` - 区域(fence/zone/gather)
- `/:project/alarm` - 告警
- `/:project/notification` - 通知
- `/:project/device` - 设备(tag/anchor/camera/configuration)
- `/:project/statistic` - 统计(多tab)
- `/:project/space` - 地图空间管理(list/detail/editor)
- `/:project/simulation` - 模拟回放
- `/:project/log` - 日志
- `/:project/showroom` - 展厅(无layout)
- `/project` - 项目管理
- `/user` - 用户管理
- `/company` - 公司管理

### config/proxy.ts
5个环境代理配置，代理路径: `/api`, `/websocket`, `/resources`, `/stream`, `/amap`
- local: localhost:8080
- dev/test/oem: lbs.reliablesense.net
- prod: lbs.reliablesense.com

---

## src/app.tsx - 运行时配置(最核心文件)

### getInitialState()
应用初始化，返回 `{ appId, appSecret, settings, currentUser, currentCompany, currentProject }`
流程:
1. 处理URL query参数(lang/token/username+password/appId+appSecret)
2. 通过 `getSession()` 获取当前用户
3. 通过 `getProjects()` 获取项目列表，匹配当前路径确定 currentProject
4. 设置 appId/appSecret 到 localStorage

### layout 配置
- `menuDataRender`: 根据是否有currentProject返回不同菜单(公司菜单/项目菜单)
- `headerContentRender`: 渲染RightContent + HistoryTabs
- `links`: 侧边栏底部链接(公司信息/返回项目管理)

### request 配置
- 请求拦截器: 注入 `X-AUTH-TOKEN`, `X-Schema`, `apiKey`, `apiSecret`, `Accept-Language`
- 响应拦截器: 处理CSV下载、success/data格式解包
- 错误处理: 按HTTP状态码显示国际化错误消息
- 统一前缀: `/api`

---

## src/types/ 类型定义

### pagination.d.ts
`PaginationData<T>` - 分页响应 { list, total, pageSize, current }
`PaginationParams` - 分页请求 { sort, order, pageSize, current, pageNum, offset, limit }

### project.ts
`ProjectData` - { id, uid, name, logo, config, companyId, appId, appSecret, role, permission }
`ProjectPermission` - 细粒度权限(canReadXxx/canWriteXxx 约40+个布尔字段)
`ProjectRole` - { id, uid, name, permission }

### user.d.ts
`UserData` - { id, username, password, name, email, phone, companyId, company, projects, role }
`UserRole` - { id, uid, name } (uid: ROLE_ADMIN / ROLE_COMPANY_ADMIN / ROLE_COMPANY_USER)

### trackable.d.ts
`TrackableData` - 定位对象 { id, uid, name, position, labels, groups, dynamicFence, tag, config, anticollision }
`LabelData` - 标签分类 { id, name, icon, color }
`AnticollisionConfig` - 防碰撞 { role: 'announcer'|'monitor', distance, exceptionIds }

### tag.d.ts
`TagData` - 标签设备 { id, uid, typeId, type, battery, modules, trackable, position, status }
`ModuleData` - 模组 { typeId, type, address }
`TagType` - 标签型号 { uid, name, brand, type, moduleTypeIds }

### fence.d.ts
`FenceData` - 电子围栏 { id, name, position, category(NORMAL/DYNAMIC/INSPECTION), feature, type, activeMode(ALWAYS/SCHEDULE), enable, exceptionIds, config }
`FenceType` - 围栏类型 { uid(KEEP_IN/KEEP_OUT/ACCESS_LIMIT/STATISTIC/OVERTIME_STAY_ALARM/OVERTIME_LEAVE_ALARM), name, color }

### zone.d.ts
`ZoneData` - 统计区域(结构同FenceData，通过types='STATISTIC'区分)
`ZoneAccessData` - 进出记录 { trackableId, fenceId, enterTime, leaveTime }

### alarm.d.ts
`AlarmData` - 告警 { id, name, active, typeId, type, trackableId, tag, relatedId, startTime, endTime, position }
`AlarmType` - 告警类型 { id, name, enable }

### camera.d.ts
`CameraData` - 摄像头 { id, uid, name, brand, ipaddress, username, password, online, fenceId, position }

### gather.d.ts
`GatherData` - 聚集事件 { uid, timestamp, endTimestamp, level, radius, trackables, position }

### position.d.ts
`PositionParams` - 位置查询 { spaceId, floor, mapId, latest, trackableIds, labelIds, startTime, endTime }
`HeatmapParams` - 热力图查询

### map.d.ts
`MapState` - 地图显示状态(40+个控制字段: enable*Controller, show*等)

### config.d.ts
`ConfigState` - 配置状态(showTrackables/showTags/showAnchors/showCameras/showFences/showZones等显示控制)

### access.d.ts
`AccessData` - 权限数据(canRead*/canWrite* 约40+个布尔字段)

### place.d.ts
`PlaceData` - 地点搜索(支持amap/mapbox)

---

## src/models/ 全局状态

使用UmiJS plugin-model，通过 `useModel('modelName')` 访问。

### global.ts
全局基础数据，1小时轮询刷新:
- `labels: LabelData[]` - 标签分类列表
- `alarmTypes: AlarmType[]` - 告警类型
- `fenceTypes: FenceType[]` - 围栏类型
- `zoneTypes: ZoneType[]` - 区域类型
- `spaces: SpaceStateData[]` - 空间列表
提供 refresh* 方法手动刷新

### config.ts
地图配置状态管理(多实例)。支持URL参数同步。
- 通过 `key` 区分不同实例(默认'global')
- `states[key]` 存储各实例的ConfigState
- `initStates[key]` 存储初始值
- `setState(key, k, value)` 更新配置并同步URL
- 配置项: showTrackables/showTags/showAnchors/showCameras/showFences/showZones等

### map.ts
地图视图状态管理(多实例)。支持URL参数同步。
- `refs[key]` 存储RSMap组件ref
- `states[key]` 存储各实例的MapState
- `selectIds[key]` / `followIds[key]` 选中/跟随的对象ID
- 配置项: enable*Controller, show*等40+个字段

### trackable.ts
定位对象实时数据。WebSocket订阅 `/topic/position/`，30分钟轮询刷新。
- `data: TrackableData[]`
- `update(trackable)` / `remove(trackable)`
- 支持labelIds权限过滤

### tag.ts
标签实时数据。WebSocket订阅 `/topic/position/tag/`。
- `data: TagData[]`
- `update(tag)` / `remove(tag)`

### alarm.ts
告警实时数据。WebSocket订阅 `/topic/alarm/`，5分钟轮询。
- `data: AlarmData[]` (按startTime降序)

### gather.ts
聚集事件实时数据。WebSocket订阅 `/topic/event/gathering/`，5分钟轮询。
- `data: GatherData[]` (只保留active的)

### fence.ts / zone.ts / camera.ts / anchor.ts / shelf.ts / user.ts
CRUD模型，30分钟轮询。提供 `data/add/update/remove/refresh`。

### showroom.ts
展厅页面统计数据: alarmCount, trackableCount, tagCount

---

## src/services/ API请求层

所有请求通过 `umi-request`，自动加 `/api` 前缀。

### session.ts
- `getSession()` → GET /sessions (获取当前用户)
- `createSession(params)` → POST /sessions (登录)
- `deleteSession()` → DELETE /sessions (登出)
- `getVerCode()` → GET /sessions/verCode

### project.ts
- `getProjects(params)` / `getProjectPages(params)` → GET /projects
- `createProject(data)` → POST /projects
- `updateProject(id, data)` → PUT /projects/:id
- `deleteProject(id)` → DELETE /projects/:id
- `getProjectByAppIdAndAppSecret()` → GET /projects/app

### user.ts
- `getUsers(params)` / `getUserPages(params)` → GET /users
- `createUser(data)` → POST /users
- `updateUser(id, data)` → PUT /users/:id
- `deleteUser(id)` → DELETE /users/:id

### trackable.ts
- `getTrackables(params)` / `getTrackablePages(params)` → GET /trackables
- `createTrackable(data)` → POST /trackables
- `updateTrackable(id, data)` → PUT /trackables/:id
- `deleteTrackable(id)` → DELETE /trackables/:id
- `importTrackables(file)` → POST /trackables/import
- `exportTrackables(params)` → GET /trackables/export
- 内置 `appendLabelFilter` 自动注入权限labelIds

### tag.ts
- `getTags(params)` / `getTagPages(params)` → GET /tags
- `getTagTypes(params)` / `getTagModuleTypes(params)` → GET /tags/types
- `createTag(data)` → POST /tags
- `updateTag(id, data)` → PUT /tags/:id
- `deleteTag(id)` → DELETE /tags/:id
- `bindTag(id, trackableId)` / `unbindTag(id)` → PUT /tags/:id/bindTrackable

### fence.ts
- `getFences(params)` / `getFencePages(params)` → GET /fences
- `getFenceTypes(params)` → GET /fences/types
- `createFence(data)` → POST /fences
- `updateFence(id, data)` → PUT /fences/:id
- `deleteFence(id)` → DELETE /fences/:id
- `getFenceAccesses(params)` → GET /fences/accesses
- `getFenceStatistic(params)` → GET /fences/statistic

### zone.ts
- 同fence.ts结构，但查询时 `types='STATISTIC'`
- `getZones(params)` → GET /fences (types=STATISTIC)

### alarm.ts
- `getAlarms(params)` / `getAlarmPages(params)` → GET /alarms
- `getLatestAlarms()` → GET /alarms (active=true)
- `getAlarmTypes(params)` → GET /alarms/types
- `getAlarmStatistic(params)` → GET /alarms/statistic

### position.ts
- `getLatestPositions(params)` → GET /positions/latest
- `getPositions(params)` → GET /positions
- `getHeatmap(params)` → GET /positions/heatmap
- `updateTrackablePositions(data, entries)` - WebSocket数据合并逻辑

### camera.ts
- `getCameras(params)` / `getCameraPages(params)` → GET /cameras
- `createCamera(data)` → POST /cameras
- `updateCamera(id, data)` → PUT /cameras/:id
- `deleteCamera(id)` → DELETE /cameras/:id

### notification.ts
- `getNotifications(params)` → GET /notifications
- `createNotification(data)` → POST /notifications
- `updateNotification(id, data)` → PUT /notifications/:id
- `deleteNotification(id)` → DELETE /notifications/:id

### group.ts
- `getGroups(params)` → GET /groups
- `createGroup(data)` → POST /groups
- `updateGroup(id, data)` → PUT /groups/:id
- `deleteGroup(id)` → DELETE /groups/:id

### label.ts
- `getLabels(params)` → GET /labels

### floor.ts
- `getFloors(params)` → GET /floors
- `createFloor(data)` → POST /floors
- `updateFloor(id, data)` → PUT /floors/:id
- `deleteFloor(id)` → DELETE /floors/:id

### route.ts
- `getRoutes(params)` → GET /routes (导航路线)

### inspection.ts
- `getInspections(params)` → GET /inspections (巡检)

### keep-alive.tsx
- `KeepAliveProvider` - react-activation的AliveScope包装

### utils.ts
- `joinParams(params)` - 数组参数join为逗号分隔
- `joinData(object, key)` - 提取id并join
- `orderBy/paginate` - 前端排序分页
- `orderParamTransform` - ascend→ASC
- `sortParamTransform` - camelCase→snake_case
- `detectCharset(file)` - 检测文件编码

---

## src/hooks/ 自定义Hooks

### index.ts (统一导出)
re-export React hooks + ahooks + umi hooks + 自定义hooks

### useWebsocket.ts
核心WebSocket hook。使用STOMP协议。
- 支持初始API请求 + WebSocket实时更新
- 支持轮询刷新、可见性刷新、缓存间隔
- 支持labelIds过滤、自定义filter/sorter
- 自动重连、网络恢复重连

### useRequest.ts
封装ahooks useRequest，统一请求配置

### useParam.ts
URL参数管理hook，支持参数与URL双向同步

### useWindowState.ts
跨组件共享状态(基于window对象)

### useInterval.ts
定时器hook

### useMap.ts / useInitMap.ts
地图model的便捷访问hook

### useConfig.ts / useInitConfig.ts
配置model的便捷访问hook

### useNavigation.ts
导航面板hook

### useGlobal.ts
全局model便捷访问

### 实体hooks (useTrackable/useTrackables/useTag/useTags/useAnchor/useAnchors/useFence/useFences/useZone/useZones/useCamera/useCameras/useAlarms/useGathers/useShelves/useUsers)
各实体model的便捷访问hook

---

## src/utils/ 工具函数

### utils.ts
通用工具: getDateTime, getDelay, isEmpty, uuid, getWebSocketUrl, isUrl, setGlobal/getGlobal等

### access.ts
`getAccess(currentUser, currentProject)` - 根据用户角色和项目权限计算完整AccessData
角色层级: ROLE_ADMIN > ROLE_COMPANY_ADMIN > ROLE_COMPANY_USER

### query.ts
URL参数转换: transformParamToValue, transformValueToParam, transformDefaultViewportParamToValue等

### menu.tsx
`getCompanyMenu(access)` / `getProjectMenu(project, access)` - 根据权限生成菜单

### trackable.tsx / tag.tsx / fence.tsx / zone.tsx / alarm.tsx / anchor.tsx / camera.tsx
各实体的ProTable columns定义和渲染工具

### viewport.ts
视口计算工具

### vercode.ts
验证码工具

### token.ts (推断)
getToken/setToken/clearToken/getAppId/setAppId/getAppSecret/setAppSecret

---

## src/pages/ 页面

### User/Login - 登录页
支持账号密码登录、验证码

### User/Register - 注册页

### Position - 实时定位页
核心页面，集成RSMap地图组件，显示实时定位对象、标签、基站、摄像头、围栏、区域、告警

### Overview - 总览仪表盘
统计卡片(告警数/定位对象数/标签数)

### Trackable/List - 定位对象列表
ProTable，支持搜索/筛选/导入/导出/CRUD

### Trackable/Detail - 定位对象详情
详情页，含历史轨迹、标签绑定等

### Trackable/Group - 分组管理
### Trackable/Label - 标签分类管理

### Area/Fence/List - 围栏列表
### Area/Fence/Detail - 围栏详情(含地图编辑)
### Area/Zone/List - 统计区域列表
### Area/Zone/Detail - 统计区域详情
### Area/Gather - 聚集事件

### Alarm - 告警列表
### Notification - 通知管理

### Device/Tag/List - 标签设备列表
### Device/Tag/Detail - 标签详情
### Device/Anchor/List - 基站列表
### Device/Anchor/Detail - 基站详情
### Device/Camera/List - 摄像头列表
### Device/Camera/Detail - 摄像头详情
### Device/Configuration - 设备配置

### Statistic - 统计页(多tab)
子组件: TrackableStatistic, FenceStatistic, ZoneStatistic, AlarmStatistic, History, Heatmap, Replay, Gather

### Map/List - 空间列表
### Map/Detail - 空间详情(含楼层管理)
### Map/Editor - 地图编辑器(无layout)

### Simulation - 模拟回放
### Log - 操作日志
### Showroom - 展厅(无layout，大屏展示)

### Project/List - 项目列表
### Project/Privilege - 项目权限管理
### User/List - 用户管理
### Company/List - 公司管理

---

## src/components/ 通用组件

### RSMap - 核心地图组件
封装rsmap SDK，集成所有地图图层(定位对象/标签/基站/摄像头/围栏/区域/告警/聚集等)
子目录: components/(地图子组件), modules/(功能模块)

### RSMap3 - 3D地图组件

### MapFilter - 地图筛选面板
控制地图上各图层的显示/隐藏

### Trackable/ - 定位对象组件集
FormTrackable, FormTrackableBind, FormTrackableUnbind, PopupTrackable, PanelTrackable, TableTrackable, TableSpaceTrackable, TableLabelTrackable, TableGroupTrackable, ModalTrackable, TrackableGroups

### Tag/ - 标签组件集
FormTag, FormTagBind, FormTagUnbind, FormTagType, FormModule, FormModuleSelect, TableTag, PanelTag, PopupTag, TagEnable

### Anchor/ - 基站组件集
FormAnchor, FormAnchorLocator, FormAnchorType, TableAnchor, PanelAnchor, PopupAnchor, ModalAnchor, AnchorEnable

### Camera/ - 摄像头组件集
FormCamera, FormCameraLocator, TableCamera, PanelCamera, PopupCamera, ModalCamera, VideoCamera, CardVideoCamera, CarouselVideoCamera

### Fence/ - 围栏组件集
FormFence, FenceFields, FenceExceptions, FenceEnable, TableFence, TableFenceAccess, PanelFence, ModalFence, ModalFenceAccess

### Zone/ - 区域组件集
FormZone, ZoneFields, ZoneExceptions, ZoneEnable, TableZone, TableZoneAccess, PanelZone, ModalZone, ModalZoneAccess

### Alarm/ - 告警组件集
TableAlarm, PanelAlarm, PopupAlarm, ModalAlarm

### Group/ - 分组组件集
FormGroup, FormGroupTrackables, TrackablesTransfer

### Notification/ - 通知组件集
FormNotification, ModalNotification

### User/ - 用户组件集
FormUser, FormPassword, FormProjectUsers, FormProjectRole

### Project/ - 项目组件集
CardProject, FormProject

### Company/ - 公司组件集
FormCompany

### Space/ - 空间组件集
FormSpace, FormSpaceEditor, CardSpace

### Floor/ - 楼层组件集
FormFloor, FormFloorEditor

### Map/ - 地图组件集
FormMap

### Poi/ - POI组件集
FormIcon, FormIconUpload, FormPoiType, ModalPoiType

### Anticollision/ - 防碰撞组件集
AnticollisionFields, AnticollisionExceptions

### 通用UI组件
- RightContent - 顶部右侧(用户头像/通知/语言切换)
- NoticeIcon - 通知图标(告警badge)
- HistoryTabs - 历史标签页导航
- HeaderSearch - 头部搜索
- HeaderDropdown - 头部下拉菜单
- Footer - 页脚
- CardBar - 卡片条
- CardOverview - 总览卡片
- DateTimeFromNow - 相对时间显示
- Decriptions - 描述列表
- FormDelete - 删除确认
- FormExport - 导出表单
- FormImport - 导入表单
- FormFile - 文件上传
- FormRangePicker - 日期范围选择
- FormTimePicker - 时间选择
- FormSelect - 选择器
- FormElink - 外链表单
- Labels - 标签展示
- Label - 单标签
- Link - 链接
- Modal - 模态框
- RSIcon - 自定义图标(iconfont)
- Svg/ - SVG图标集(TrackableSvg, AnchorSvg, CameraSvg, FenceSvg等)

---

## WebSocket通信

### 连接
STOMP over WebSocket，URL: `/websocket/xxx/api/ws`

### 订阅主题
- `/topic/position/` - 定位对象位置更新
- `/topic/position/tag/` - 标签位置更新
- `/topic/alarm/` - 告警更新
- `/topic/event/gathering/` - 聚集事件更新

### 数据流
1. 初始通过API请求获取全量数据
2. WebSocket推送增量更新
3. useWebsocket hook合并数据(updateData回调)
4. 支持cacheInterval节流

---

## 认证与权限

### 认证
- Token存储在localStorage，请求头 `X-AUTH-TOKEN: Bearer {token}`
- 项目标识: `X-Schema: {appId}`, `schema: {appId}`
- API认证: `apiKey: {appId}`, `apiSecret: {appSecret}`

### 角色体系
公司级: ROLE_ADMIN > ROLE_COMPANY_ADMIN > ROLE_COMPANY_USER
项目级: PROJECT_ADMIN > PROJECT_USER (通过ProjectPermission细粒度控制)

### 权限控制
- 路由级: routes.ts中access字段
- 菜单级: menuDataRender根据access过滤
- 页面级: useAccess() hook
- 数据级: labelIds过滤(appendLabelFilter)

---

## 环境与部署

### 启动命令
- `npm start` / `npm run dev` → APP_ENV=dev
- `npm run start:local` → APP_ENV=local (localhost:8080)
- `npm run start:test` → APP_ENV=test
- `npm run start:prod` → APP_ENV=prod
- `npm run build` → 生产构建

### 环境差异
- local: API→localhost:8080, WS→ws://localhost:8080
- dev/test/oem: API→https://lbs.reliablesense.net
- prod: API→https://lbs.reliablesense.com

---

## 常用修改指南

### 新增页面
1. `config/routes.ts` 添加路由(含access)
2. `src/pages/XxxPage/index.tsx` 创建页面
3. `src/utils/access.ts` 添加权限(如需)
4. `src/utils/menu.tsx` 添加菜单项(如需)

### 新增API
1. `src/services/xxx.ts` 添加请求函数
2. `src/types/xxx.d.ts` 添加类型定义

### 新增全局状态
1. `src/models/xxx.ts` 创建model
2. 页面中 `useModel('xxx')` 使用

### 新增组件
1. `src/components/Xxx/index.tsx` 创建组件
2. 组件命名规范: Form*(表单), Table*(表格), Panel*(面板), Popup*(弹出), Modal*(模态框), Card*(卡片)

### 修改地图显示
- 图层控制: `src/models/config.ts` 的 defaultState
- 地图控件: `src/models/map.ts` 的 defaultState
- 地图渲染: `src/components/RSMap/` 下的modules
