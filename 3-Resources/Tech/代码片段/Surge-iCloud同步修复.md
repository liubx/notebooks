---
title: Surge iCloud 同步修复
type: code-snippet
tags:
  - tech/macos
  - tech/surge
created: 2025-01-01
modified: 2025-01-01
---

# Surge iCloud 同步目录修复

```bash
sudo mkdir -pv iCloud~com~nssurge~inc/Documents
sudo chown -R liubx:staff iCloud~com~nssurge~inc/Documents
sudo chown -R liubx:staff iCloud~com~nssurge~inc
chmod 700 iCloud~com~nssurge~inc

vi ~/Library/Application\ Support/com.nssurge.surge-mac/KDDefaults.plist
```
