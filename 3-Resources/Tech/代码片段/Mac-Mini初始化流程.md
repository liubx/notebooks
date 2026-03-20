---
title: Mac Mini 初始化流程
type: code-snippet
tags:
  - tech/macos
  - tech/setup
created: 2026-03-19
modified: 2026-03-19
---

# Mac Mini 初始化流程

办公室 Mac Mini 重新初始化的标准流程。

## 1. 开启远程访问

### 屏幕共享

```bash
# 系统设置 > 通用 > 共享 > 屏幕共享 > 开启
sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.screensharing.plist
```

### SSH

```bash
# 系统设置 > 通用 > 共享 > 远程登录 > 开启
sudo systemsetup -setremotelogin on
```

## 2. 安装软件

### 安装 Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 安装核心应用

```bash
brew install --cask iterm2
brew install --cask microsoft-edge
brew install --cask surge
brew install --cask visual-studio-code
brew install --cask kiro
```

### 安装 mise

```bash
brew install mise
```

## 3. 初始化 iTerm2 设置

iTerm2 配置通过 iCloud 同步，无需手动配置。

### 从 iCloud 加载配置

1. 打开 iTerm2 > Settings > General > Preferences
2. 勾选 "Load preferences from a custom folder or URL"
3. 路径设置为：`~/Library/Mobile Documents/com~apple~CloudDocs/Applications/iTerm2`
4. 重启 iTerm2，Profiles 和所有设置会自动同步过来

iCloud 中的配置文件：
- `com.googlecode.iterm2.plist` — iTerm2 全局设置
- `Profiles.json` — 终端 Profiles 配置
- `iTerm2.itermexport` — 导出备份

### 安装 Oh My Zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 安装 Powerlevel10k 主题

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

### 安装自定义插件

```bash
# zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### 同步终端配置文件

从当前机器通过 scp 同步到新 Mac Mini（首次需要输入密码）：

```bash
# SSH 密钥和配置（优先传输，后续 scp 可免密）
ssh reliablesense@192.168.50.8 "mkdir -p ~/.ssh"
scp ~/.ssh/id_rsa reliablesense@192.168.50.8:~/.ssh/id_rsa
scp ~/.ssh/id_rsa.pub reliablesense@192.168.50.8:~/.ssh/id_rsa.pub
scp ~/.ssh/config reliablesense@192.168.50.8:~/.ssh/config
ssh reliablesense@192.168.50.8 "cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && chmod 700 ~/.ssh && chmod 600 ~/.ssh/id_rsa ~/.ssh/config ~/.ssh/authorized_keys && chmod 644 ~/.ssh/id_rsa.pub"
# .zshrc — oh-my-zsh 配置、主题、插件、mise 激活
scp ~/.zshrc reliablesense@192.168.50.8:~/.zshrc

# .p10k.zsh — Powerlevel10k 主题配置
scp ~/.p10k.zsh reliablesense@192.168.50.8:~/.p10k.zsh

# oh-my-zsh custom 目录（含 powerlevel10k 主题和自定义插件）
scp -r ~/.oh-my-zsh/custom/ reliablesense@192.168.50.8:~/.oh-my-zsh/custom/

# mise 配置
ssh reliablesense@192.168.50.8 "mkdir -p ~/.config/mise"
scp ~/.config/mise/config.toml reliablesense@192.168.50.8:~/.config/mise/config.toml
```

> 同步完成后在目标机器上执行 `source ~/.zshrc` 和 `mise install` 即可。

## 4. 初始化 mise 设置

mise 激活已包含在 .zshrc 中，同步后自动生效。

### 安装运行时

```bash
mise install

# 验证
mise ls
```

## 5. 完成 Surge 配置

Surge 代理配置详见 [[Surge代理配置]]

### 快速配置步骤

1. 打开 Surge，登录账号激活授权
2. 导入配置文件或手动添加代理节点
3. 配置规则：
   - 办公网络走 OFFICE-SNELL 或 OFFICE-V2RAY
   - 外网走 PROXY
4. 开启「增强模式」接管系统网络
5. 验证连通性

### iCloud 同步

如果需要从其他设备同步配置，参考 [[Surge-iCloud同步修复]]
