# 备份ingress-ssl-admin

```jsx
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"traefik.containo.us/v1alpha1","kind":"IngressRoute","metadata":{"annotations":{},"name":"ingress-ssl-admin","namespace":"biz"},"spec":{"entryPoints":["websecure"],"routes":[{"kind":"Ru
  creationTimestamp: "2023-11-04T13:02:43Z"
  generation: 2
  name: ingress-ssl-admin
  namespace: biz
  resourceVersion: "48643137"
  uid: fff6570b-a262-4cbb-9e25-8811c25efee6
spec:
  entryPoints:
  - websecure
  routes:
  - kind: Rule
    match: PathPrefix(`/`)
    services:
    - kind: Service
      name: admin
      passHostHeader: true
      port: 8080
  - kind: Rule
    match: PathPrefix(`/pic-local-adaptor`)
    middlewares:
    - name: mw-admin-cors
    services:
    - kind: Service
      name: admin-oneid
      passHostHeader: false
      port: 443
      serversTransport: st-admin-pic
  - kind: Rule
    match: PathPrefix(`/baggage`)
    middlewares:
    - name: mw-admin-cors
    - name: mw-admin-baggage-replace
    services:
    - kind: Service
      name: admin-baggage
      passHostHeader: false
      port: 8081
  - kind: Rule                                                                                                                                                                                               
    match: PathPrefix(`/wifi`)             
    middlewares:                           
    - name: mw-admin-cors           
    - name: mw-admin-wifi-replace   
    services:                              
    - kind: Service                        
      name: admin-wifi                     
      passHostHeader: false      
      port: 8080                    
  - kind: Rule                      
    match: PathPrefix(`/geoesb`)    
    middlewares:                    
    - name: mw-admin-cors           
    services:                    
    - kind: Service                 
      name: admin-gis            
      passHostHeader: false      
      port: 8081                    
  - kind: Rule                             
    match: PathPrefix(`/amap`)      
    middlewares:                 
    - name: mw-admin-cors        
    services:                   
    - kind: Service             
      name: admin-amap                       
      passHostHeader: false                  
      port: 8080                    
  - kind: Rule                               
    match: PathPrefix(`/wechat`) 
    middlewares:                             
    - name: mw-admin-cors       
    services:                                
    - kind: Service             
      name: admin-wechat                     
      passHostHeader: false                  
      port: 8080
  - kind: Rule                      
    match: PathPrefix(`/tmap`)   
    middlewares:                 
    - name: mw-admin-cors           
    services:                              
    - kind: Service                 
      name: admin-tmap           
      passHostHeader: false      
      port: 8080                
  - kind: Rule                  
    match: PathPrefix(`/webapp`, `/weixinh5`)
    middlewares:                             
    - name: mw-admin-cors           
    services:                                
    - kind: Service              
      name: admin-webapp                     
      passHostHeader: false     
      port: 8080                             
  - kind: Rule                  
    match: PathPrefix(`/yscloud`)            
    middlewares:                             
    - name: mw-admin-cors                    
    - name: mw-admin-yscloud-headers
    services:                       
    - kind: Service                          
      name: admin-yscloud           
      passHostHeader: false                  
      port: 8080                             
  tls:                                       
    secretName: main-tls
```