# 备份ingress-admin (1)

```jsx
# Please edit the object below. Lines beginning with a '#' will be ignored,                                                                                                                                  
# and an empty file will abort the edit. If an error occurs while saving this file will be                                                                                                                   
# reopened with the relevant failures.                                                                                                                                                                       
#                                                                                                                                                                                                            
apiVersion: traefik.containo.us/v1alpha1                                                                                                                                                                     
kind: IngressRoute                                                                                                                                                                                           
metadata:                                                                                                                                                                                                    
  annotations:                                                                                                                                                                                               
    app/sha: a36d2133935c2ac813565db54cb676b48140d78e                                                                                                                                                        
    config/sha: 38761d7b1c4d00d3d965b9310a9b98c5db16963b                                                                                                                                                     
    image/tag: v2.3.12-whjc_whjc-OEM                                                                                                                                                                         
    kubectl.kubernetes.io/last-applied-configuration: |                                                                                                                                                      
      {"apiVersion":"traefik.containo.us/v1alpha1","kind":"IngressRoute","metadata":{"annotations":{"app/sha":"a36d2133935c2ac813565db54cb676b48140d78e","config/sha":"38761d7b1c4d00d3d965b9310a9b98c5db1696
    kubernetes.io/change-cause: v2.3.12-whjc_whjc-OEM-a36d2133935c2ac813565db54cb676b48140d78e-38761d7b1c4d00d3d965b9310a9b98c5db16963b
  creationTimestamp: "2023-07-13T14:55:29Z"
  generation: 30                             
  labels:                                  
    app: admin                               
  name: ingress-admin                        
  namespace: biz                             
  resourceVersion: "61004264"              
  uid: a65bc87a-701a-4d67-b916-3c03387d1132  
spec:                                        
  entryPoints:                               
  - webpublic                              
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
    - name: mw-admin-yscloud-replace
    services:              
    - kind: Service              
      name: admin-yscloud           
      passHostHeader: false     
      port: 8080                    
  - kind: Rule                   
    match: PathPrefix(`/webrtc`)
    middlewares:                    
    - name: mw-admin-cors  
    services:              
    - kind: Service        
      name: admin-tmap        
      passHostHeader: true      
      port: 8080
```