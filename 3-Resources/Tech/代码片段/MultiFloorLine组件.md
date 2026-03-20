---
title: MultiFloorLine 组件
type: code-snippet
language: TypeScript
tags:
  - tech/react
  - tech/前端
  - project/麦钉项目
created: 2026-03-15
---

# MultiFloorLine 组件

语言: TypeScript (React Class Component)

## 使用场景

rsmap 地图库中的多楼层轨迹线组件，支持跨楼层线段渲染、3D 楼层切换动画、自动跟随视角。

## 代码

```tsx
import React, { Component } from 'react';  
import { MapContext } from 'react-map-gl';  
import { isEqual } from 'lodash';  
import bbox from '@turf/bbox';  
import { lineString, point } from '@turf/helpers';  
import { getFloors, getMainFloor, getSubFloor, isEmpty } from '@/utils';  
import { LineProps as LineComponentProps } from '@/components/Line';  
import Line from '@/modules/Line';  
  
export type MultiFloorLineProps = LineComponentProps & {  
  defaultFollow?: boolean | string;  
};  
  
class MultiFloorLine extends Component<MultiFloorLineProps> {  
  context: any = undefined;  
  
  static defaultProps = {  
    getPath: (*d*) => d.coordinates,  
    getSpace: (*d*) => d.spaceId,  
    getFloor: (*d*) => d.floor,  
    getMap: (*d*) => d.mapId,  
  };  
  
  componentDidMount() {  
    const { defaultFollow } = this.props;  
    if (defaultFollow) {  
      this.defaultFollow();  
    }  
  }  
  
  componentDidUpdate(*prevProps*: MultiFloorLineProps) {  
    const { defaultFollow } = this.props;  
    if (!isEqual(prevProps.defaultFollow, defaultFollow) && defaultFollow) {  
      this.defaultFollow();  
    }  
  }  
  
  defaultFollow = () => {  
    const { location, data, getPath, getSpace, getFloor, getMap } = this.props;  
    const { showMultipleFloor, defaultFollow } = this.props;  
    const { onViewportChange, enableInteractionController } = this.props;  
    if (!enableInteractionController) {  
      return;  
    }  
    const lines = data  
      .filter((*item*) => defaultFollow == ++[item.id](http://item.id/)++ || defaultFollow == true)  
      .map((*item*) => {  
        return {  
          coordinates: getPath!(item),  
          spaceId: getSpace(item),  
          floor: getFloor(item),  
          mapId: getMap(item),  
        };  
      });  
    if (lines.length) {  
      const { spaceId, floor } = location || lines[0];  
      const points = lines  
        .filter((*item*) => showMultipleFloor || (item.spaceId === spaceId && item.floor === floor))  
        .map((*item*) => item.coordinates)  
        .flat();  
      if (points.length) {  
        const feature = points.length > 1 ? lineString(points) : point(points[0]);  
        try {  
          const bounds = bbox(feature);  
          const result: any = this.context.viewport.fitBounds([  
            [bounds[0], bounds[1]],  
            [bounds[2], bounds[3]],  
          ]);  
          onViewportChange?.({  
            spaceId,  
            floor,  
            longitude: result.longitude,  
            latitude: result.latitude,  
            zoom: result.zoom - 1,  
            gcj02: false,  
            transitionDuration: 500,  
          });  
        } catch (error) { }  
      }  
    }  
  };  
  
  getLines = (*space*, *floors*) => {  
    const { data, getPath, getSpace, getFloor, show3Dimension, spaces } = this.props;  
  
    const resolveFloorHeight = (*item*) => {  
      const targetFloors =  
        (spaces || []).find((*sp*) => sp?.id === getSpace(item))?.floors || floors || [];  
      const floorHeighs = getFloors(targetFloors);  
      return floorHeighs.find((*fl*) => fl.floor === getFloor(item));  
    };  
  
    const lines: any = [];  
  
    data.forEach((*item*, *index*) => {  
      lines.push({  
        coordinates: getPath!(item),  
        spaceId: getSpace(item),  
        floor: getFloor(item),  
      });  
      if (index < data.length - 1) {  
        const item1 = item;  
        const item2 = data[index + 1];  
        const coord1 = getPath!(item1);  
        const coord2 = getPath!(item2);  
        const item1MainFloor = getMainFloor(getFloor(item1));  
        const item1SubFloor = getSubFloor(getFloor(item1));  
        const item2MainFloor = getMainFloor(getFloor(item2));  
        const item2SubFloor = getSubFloor(getFloor(item2));  
  
        const item1Floor = resolveFloorHeight(item1);  
        const item2Floor = resolveFloorHeight(item2);  
  
        let direction = 'flat';  
        if (item1MainFloor !== item2MainFloor) {  
          direction = item1MainFloor > item2MainFloor ? 'down' : 'up';  
        } else if (item1SubFloor !== item2SubFloor) {  
          direction = item1SubFloor > item2SubFloor ? 'down' : 'up';  
        }  
  
        if (item1.floor === 0 || item2.floor === 0) {  
          direction = 'flat';  
        }  
  
        if (direction === 'up' && show3Dimension) {  
          lines.push(  
            {  
              coordinates: [  
                coord1[coord1.length - 1],  
                [  
                  coord1[coord1.length - 1][0],  
                  coord1[coord1.length - 1][1],  
                  item1Floor?.originHeight || 0,  
                ],  
              ],  
              spaceId: getSpace(item1),  
              floor: getFloor(item1),  
              arrow: false,  
            },  
            {  
              coordinates: [  
                [coord1[coord1.length - 1][0], coord1[coord1.length - 1][1], 0],  
                coord2[0],  
              ],  
              spaceId: getSpace(item2),  
              floor: getFloor(item2),  
              arrow: false,  
            },  
          );  
        } else if (direction === 'down' && show3Dimension) {  
          lines.push(  
            {  
              coordinates: [  
                coord1[coord1.length - 1],  
                [coord1[coord1.length - 1][0], coord1[coord1.length - 1][1], 0],  
              ],  
              spaceId: getSpace(item1),  
              floor: getFloor(item1),  
              arrow: false,  
            },  
            {  
              coordinates: [  
                [  
                  coord1[coord1.length - 1][0],  
                  coord1[coord1.length - 1][1],  
                  item2Floor?.originHeight || 0,  
                ],  
                coord2[0],  
              ],  
              spaceId: getSpace(item2),  
              floor: getFloor(item2),  
              arrow: false,  
            },  
          );  
        } else {  
          if (item1.floor === 0) {  
            const baseZ = coord1[coord1.length - 1][2] ?? 0;  
            lines.push({  
              coordinates: [  
                [coord1[coord1.length - 1][0], coord1[coord1.length - 1][1], baseZ],  
                [coord2[0][0], coord2[0][1], coord2[0][2] ?? baseZ],  
              ],  
              spaceId: getSpace(item2),  
              floor: getFloor(item2),  
              arrow: false,  
            });  
          } else if (item2.floor === 0) {  
            const baseZ = coord1[coord1.length - 1][2] ?? 0;  
            lines.push({  
              coordinates: [  
                [coord1[coord1.length - 1][0], coord1[coord1.length - 1][1], baseZ],  
                [coord2[0][0], coord2[0][1], coord2[0][2] ?? baseZ],  
              ],  
              spaceId: getSpace(item1),  
              floor: getFloor(item1),  
              arrow: false,  
            });  
          }  
        }  
      }  
    });  
    return lines.filter((*item*) => (item.spaceId || 0) === (space?.id || 0));  
  };  
  
  render() {  
    const {  
      spaces,  
      spaceState,  
      showArrow,  
      showMixEnvironment,  
      data,  
      getPath,  
      getSpace,  
      getFloor,  
      getMap,  
    } = this.props;  
  
    let components: any = [];  
  
    if (!(spaceState && spaceState.space && spaceState.floors)) {  
      components = data  
        .map((*item*) => ({  
          coordinates: getPath!(item),  
          spaceId: getSpace(item),  
          floor: getFloor(item),  
          mapId: getMap(item),  
        }))  
        .filter((*item*) => !item.spaceId || !item.floor)  
        .map((*item*, *index*) => (  
          <Line  
            key={index}  
            {...this.props}  
            defaultFollow={false}  
            data={[item]}  
            getPath={(*d*) => d.coordinates}  
            spaceId={item.spaceId}  
            floor={item.floor}  
            mapId={item.mapId}  
          />  
        ));  
    } else if (showMixEnvironment) {  
      components = data  
        .map((*item*) => ({  
          coordinates: getPath!(item),  
          spaceId: getSpace(item),  
          floor: getFloor(item),  
          mapId: getMap(item),  
        }))  
        .filter((*item*) => !item.spaceId || !item.floor)  
        .map((*item*, *index*) => (  
          <Line  
            key={index}  
            {...this.props}  
            defaultFollow={false}  
            data={[item]}  
            getPath={(*d*) => d.coordinates}  
            spaceId={item.spaceId}  
            floor={item.floor}  
            mapId={item.mapId}  
          />  
        ));  
    }  
  
    const { space, floors } = spaceState || {};  
  
    if (showMixEnvironment) {  
  
      components = [  
        ...components,  
        ...(spaces || [])  
          .filter((*sp*: SpaceData) => sp?.id && space?.id !== sp?.id && !isEmpty(sp.floors))  
          .map((*sp*: SpaceData) => {  
            const lines = this.getLines(sp, sp.floors);  
            return lines  
              .filter((*item*) => (item.spaceId || 0) === (sp?.id || 0))  
              .map((*item*, *index*) => (  
                <Line  
                  lineJointRounded={true}  
                  lineCapRounded={true}  
                  key={`${item.spaceId}-${item.floor}-${index}`}  
                  {...this.props}  
                  getPath={(*d*) => d.coordinates}  
                  defaultFollow={false}  
                  data={[item]}  
                  showArrow={item.arrow === false ? false : showArrow}  
                  spaceId={item.spaceId}  
                  floor={item.floor}  
                  mapId={item.mapId}  
                />  
              ));  
          }),  
      ];  
    }  
    const lines = this.getLines(space, floors);  
    return [  
      ...components,  
      ...lines  
        .filter((*item*) => (item.spaceId || 0) === (space?.id || 0))  
        .map((*item*, *index*) => (  
          <Line  
            lineJointRounded={true}  
            lineCapRounded={true}  
            key={`${item.spaceId}-${item.floor}-${index}`}  
            {...this.props}  
            getPath={(*d*) => d.coordinates}  
            defaultFollow={false}  
            data={[item]}  
            showArrow={item.arrow === false ? false : showArrow}  
            spaceId={item.spaceId}  
            floor={item.floor}  
            mapId={item.mapId}  
          />  
        )),  
    ];  
  }  
}  
  
MultiFloorLine.contextType = MapContext;  
export default MultiFloorLine;  
