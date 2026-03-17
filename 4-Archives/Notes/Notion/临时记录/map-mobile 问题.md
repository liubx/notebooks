# map-mobile 问题

- [x]  1.任意角度3D切换到2D，不会回正角度，修改为2D可以旋转角度
- [x]  2.无法切换楼层
- [x]  3.指北针无法使用
- [x]  4.点击指北针后，比例尺会变成3000KM
- [ ]  5.连点两次跟随按钮会回正地图方向
- [x]  6.点位高度需适当调低一点
- [x]  7.开始导航后，3D/2D切换按钮消失
- [x]  8.小程序无语音，关闭右侧语音按钮
- [ ]  9.左侧全揽按钮无效果
- [x]  10.途径点icon图标字体未居中
- [x]  11.“起点和终点置换”按钮点击后会回到确认终点界面
- [ ]  12.跨楼层时导航，路线粗细不一致
- [x]  13.点位图标需要更改

修了 8,10,11 ///// 6是数据的问题，现在location后端返回来的值是1.6所以显示的较高. ////// 12 无法修改. ///// 在看5

[http://localhost:8001/?spaceId=1&appId=sziot_iote2023&appSecret=45f4c5cb-bbfa-445b-b2f2-75a83403c20c&trackableId=b6d70eab-41c4-48c6-be82-35115d78da2e&enableMultiFloorController=true&enableSpaceController=true&enableMultipleFloorController=true&enableFloorController=true&enableLocationController=true&enableDimensionController=true&enableCompassController=true&enableRulerController=true&enableVoiceController=true&enableRouteController=false&enableRouteDetailController=true&enableClickController=true&enableSearchController=true&locationMode=0&showPoi=true&showDarkMode=false&showSatellite=false&show3Dimension=true&showMultipleFloor=true&showTrackables=false&showAvailableTrackables=false&showFences=true&showAlarm=false&showAlert=false&showHeatmap=false&showHistory=false](http://localhost:8001/?spaceId=1&appId=sziot_iote2023&appSecret=45f4c5cb-bbfa-445b-b2f2-75a83403c20c&trackableId=b6d70eab-41c4-48c6-be82-35115d78da2e&enableMultiFloorController=true&enableSpaceController=true&enableMultipleFloorController=true&enableFloorController=true&enableLocationController=true&enableDimensionController=true&enableCompassController=true&enableRulerController=true&enableVoiceController=true&enableRouteController=false&enableRouteDetailController=true&enableClickController=true&enableSearchController=true&locationMode=0&showPoi=true&showDarkMode=false&showSatellite=false&show3Dimension=true&showMultipleFloor=true&showTrackables=false&showAvailableTrackables=false&showFences=true&showAlarm=false&showAlert=false&showHeatmap=false&showHistory=false)

[https://lbs.reliablesense.cn/map](https://lbs.reliablesense.cn/map/)[/?spaceId=1&appId=sziot_iote2023&appSecret=45f4c5cb-bbfa-445b-b2f2-75a83403c20c&trackableId=b6d70eab-41c4-48c6-be82-35115d78da2e&enableMultiFloorController=true&enableSpaceController=true&enableMultipleFloorController=true&enableFloorController=true&enableLocationController=true&enableDimensionController=true&enableCompassController=true&enableRulerController=true&enableVoiceController=true&enableRouteController=false&enableRouteDetailController=true&enableClickController=true&enableSearchController=true&locationMode=0&showPoi=true&showDarkMode=false&showSatellite=false&show3Dimension=true&showMultipleFloor=true&showTrackables=false&showAvailableTrackables=false&showFences=true&showAlarm=false&showAlert=false&showHeatmap=false&showHistory=false](http://localhost:8001/?spaceId=1&appId=sziot_iote2023&appSecret=45f4c5cb-bbfa-445b-b2f2-75a83403c20c&trackableId=b6d70eab-41c4-48c6-be82-35115d78da2e&enableMultiFloorController=true&enableSpaceController=true&enableMultipleFloorController=true&enableFloorController=true&enableLocationController=true&enableDimensionController=true&enableCompassController=true&enableRulerController=true&enableVoiceController=true&enableRouteController=false&enableRouteDetailController=true&enableClickController=true&enableSearchController=true&locationMode=0&showPoi=true&showDarkMode=false&showSatellite=false&show3Dimension=true&showMultipleFloor=true&showTrackables=false&showAvailableTrackables=false&showFences=true&showAlarm=false&showAlert=false&showHeatmap=false&showHistory=false)