# RSEngine Minapp SDK

使用该 SDK 可以接入定位平台的定位和地图服务系统，可以使用改 SDK 进行定位和位置的监听，同时可以对部署在地图服务器的室内地图进行浏览、移动、缩放、查询地图信息、路线规划等操作。

1. 导入SDK，把 "rsengine" 文件夹放入小程序 src/ 目录下, 

   **引用RSEngine**

   ```typescript
   import RSEngine from "./rsengine";
   ```

2. 初始化方法，该方法用于初始化SDK

    **RSEngine.init**
    
   ```typescript
   RSEngine.init({
      name: "演示项目",
      url: "https://lbs.reliablesense.cn",  // 服务端接口地址
      wsUrl: "wss://lbs.reliablesense.cn",  // 服务端webSocket接口地址
    · appId: "reliablesense_demo", // 当前项目ID
      appSecret: "f420b238-fb6b-4c3c-8a8a-f965765731a9", // 当前项目秘钥
      unqieueId: "xxxxx", // 用户唯一ID，可以传入微信小程序openId
      username: "xxxx", // 可以填写微信用户名称
      debug: false, // 是否启用 debug
      config: {
         defaultMapState: {
            defaultViewport: { spaceId: 1 }
         },
         location: {
            enableCorelocation: true
         },
      }
   })
   ```
3. 返回地图导航页面地址

   **RSEngine.getMap**

   ```typescript
   <WebView src={RSEngine.getMap()}/>
   ```


4. 开始定位方, 可传入回调函数接收位置更新响应

   **RSEngine.startLocation**

   ```typescript
   RSEngine.startLocation({enableGps:true, enableBluetooth:false, enableCorelocation:true });
   ```

5. 结束定位方法

   **RSEngine.stopLocation**

   ```typescript
   RSEngine.stopLocation();
   ```

6. 订阅实时位置

    **RSEngine.subscribeLocation**

   ```typescript
   RSEngine.subscribeLocation(({ longitude: 114.20511603782204, latitude: 30.771040593041484, spaceId: 1, floor:1 }) => {})
   ```

   **RSEngine.unsubscribeLocation**

   ```typescript
   RSEngine.unsubscribeLocation()
   ```
