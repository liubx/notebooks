#!/usr/bin/env node
/**
 * 飞书直接 HTTP 调用脚本 — lark-cli 无法处理的场景（multipart 上传）
 *
 * Token 来源：直接读取 lark-cli 的加密存储（macOS Keychain + AES-256-GCM）
 * 前提：已通过 lark-cli auth login 完成授权
 *
 * 用法：
 *   FT=.kiro/skills/lark-assistant/lark-scripts.js
 *   node $FT task-attach <task_guid> <本地文件>           # 上传任务附件
 *   node $FT task-download <attach_guid> <输出路径>       # 下载任务附件
 */

const https = require('https');
const http = require('http');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const crypto = require('crypto');
const os = require('os');

const LARK_CLI_SERVICE = 'lark-cli';
const LARK_CLI_CONFIG = path.join(os.homedir(), '.lark-cli', 'config.json');

// ==================== 通用工具 ====================

function httpsRequest(method, urlStr, body, headers = {}) {
  return new Promise((resolve, reject) => {
    const u = new URL(urlStr);
    const isBuffer = Buffer.isBuffer(body);
    const data = isBuffer ? body : (body ? JSON.stringify(body) : null);
    const req = https.request({
      hostname: u.hostname, path: u.pathname + u.search, method,
      headers: {
        ...(isBuffer ? {} : { 'Content-Type': 'application/json; charset=utf-8' }),
        ...(data ? { 'Content-Length': Buffer.byteLength(data) } : {}),
        ...headers,
      },
    }, (res) => {
      let raw = ''; res.on('data', c => raw += c);
      res.on('end', () => { try { resolve(JSON.parse(raw)); } catch { resolve({ _raw: raw, _status: res.statusCode }); } });
    });
    req.on('error', reject);
    if (data) req.write(data);
    req.end();
  });
}

function downloadUrl(url, outPath) {
  return new Promise((resolve, reject) => {
    function follow(u, depth) {
      if (depth > 5) { reject(new Error('重定向过多')); return; }
      const mod = u.startsWith('https') ? https : http;
      mod.get(u, (res) => {
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          follow(res.headers.location, depth + 1); return;
        }
        if (res.statusCode !== 200) {
          let raw = ''; res.on('data', c => raw += c);
          res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${raw.substring(0, 200)}`)));
          return;
        }
        const out = fs.createWriteStream(outPath);
        res.pipe(out);
        out.on('finish', () => resolve(fs.statSync(outPath).size));
      });
    }
    follow(url, 0);
  });
}

function multipartUpload(urlPath, token, fields, fileName, fileData, fileField = 'file') {
  return new Promise((resolve, reject) => {
    const boundary = '----Boundary' + Date.now().toString(16);
    const parts = [];
    for (const [k, v] of Object.entries(fields)) {
      parts.push(`--${boundary}\r\nContent-Disposition: form-data; name="${k}"\r\n\r\n${v}\r\n`);
    }
    const ext = path.extname(fileName).toLowerCase();
    const mimeMap = { '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.pdf': 'application/pdf' };
    const mime = mimeMap[ext] || 'application/octet-stream';
    parts.push(`--${boundary}\r\nContent-Disposition: form-data; name="${fileField}"; filename="${fileName}"\r\nContent-Type: ${mime}\r\n\r\n`);
    const ending = `\r\n--${boundary}--\r\n`;
    const body = Buffer.concat([Buffer.from(parts.join('')), fileData, Buffer.from(ending)]);
    const req = https.request({
      hostname: 'open.feishu.cn', path: urlPath, method: 'POST',
      headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': `multipart/form-data; boundary=${boundary}`, 'Content-Length': body.length },
    }, (res) => {
      let raw = ''; res.on('data', c => raw += c);
      res.on('end', () => { try { resolve(JSON.parse(raw)); } catch { reject(new Error(raw)); } });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

// ==================== Token 管理（读取 lark-cli 加密存储） ====================

// 从 lark-cli 配置读取 appId 和 userOpenId
function getLarkCliConfig() {
  try {
    const config = JSON.parse(fs.readFileSync(LARK_CLI_CONFIG, 'utf-8'));
    const app = config.apps && config.apps[0];
    if (!app) return null;
    const user = app.users && app.users[0];
    return { appId: app.appId, userOpenId: user ? user.userOpenId : null };
  } catch { return null; }
}

// 从 macOS Keychain 读取 lark-cli 的 master key（AES-256 密钥）
// lark-cli 通过 go-keyring 存储，格式为 "go-keyring-base64:<base64(base64(key))>"
function getMasterKey() {
  try {
    const raw = execSync(
      `security find-generic-password -s "${LARK_CLI_SERVICE}" -a "master.key" -w`,
      { encoding: 'utf-8', stdio: ['pipe', 'pipe', 'pipe'] }
    ).trim();
    const prefix = 'go-keyring-base64:';
    const b64 = raw.startsWith(prefix) ? raw.slice(prefix.length) : raw;
    // 双重 base64：外层是 go-keyring 的编码，内层是 lark-cli 存储的 base64 key
    const innerB64 = Buffer.from(b64, 'base64').toString();
    return Buffer.from(innerB64, 'base64');
  } catch { return null; }
}

// AES-256-GCM 解密（与 lark-cli keychain_darwin.go 一致）
// 格式：[12 字节 IV] [密文] [16 字节 GCM Tag]
function decryptData(data, key) {
  const IV_BYTES = 12, TAG_BYTES = 16;
  if (data.length < IV_BYTES + TAG_BYTES) return null;
  const iv = data.slice(0, IV_BYTES);
  const ciphertext = data.slice(IV_BYTES, data.length - TAG_BYTES);
  const tag = data.slice(data.length - TAG_BYTES);
  const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
  decipher.setAuthTag(tag);
  try {
    return Buffer.concat([decipher.update(ciphertext), decipher.final()]).toString('utf-8');
  } catch { return null; }
}

// 从 lark-cli 的加密存储中读取 user_access_token
function requireToken() {
  const config = getLarkCliConfig();
  if (!config || !config.appId || !config.userOpenId) {
    console.error('❌ 未找到 lark-cli 配置，请先运行: lark-cli config init');
    process.exit(1);
  }
  const masterKey = getMasterKey();
  if (!masterKey) {
    console.error('❌ 无法从 Keychain 读取 master key');
    process.exit(1);
  }

  // 加密文件路径：~/Library/Application Support/lark-cli/<appId>_<userOpenId>.enc
  const accountKey = `${config.appId}:${config.userOpenId}`;
  const safeFileName = accountKey.replace(/[^a-zA-Z0-9._-]/g, '_') + '.enc';
  const encFile = path.join(os.homedir(), 'Library', 'Application Support', LARK_CLI_SERVICE, safeFileName);

  try {
    const encData = fs.readFileSync(encFile);
    const jsonStr = decryptData(encData, masterKey);
    if (!jsonStr) throw new Error('解密失败');
    const stored = JSON.parse(jsonStr);
    const now = Date.now();

    // token 有效（提前 5 分钟判断）
    if (now < stored.expiresAt - 5 * 60 * 1000) {
      console.log('🔑 使用 lark-cli 的 user_access_token');
      return stored.accessToken;
    }

    // token 过期但 refresh token 有效，触发 lark-cli 刷新
    if (now < stored.refreshExpiresAt) {
      console.log('⚠️  token 即将过期，触发 lark-cli 刷新...');
      try {
        execSync('lark-cli auth status --verify', { stdio: 'pipe' });
        const newJson = decryptData(fs.readFileSync(encFile), masterKey);
        if (newJson) {
          const newStored = JSON.parse(newJson);
          if (Date.now() < newStored.expiresAt - 5 * 60 * 1000) {
            console.log('🔑 刷新成功');
            return newStored.accessToken;
          }
        }
      } catch { /* 刷新失败 */ }
    }

    console.error('❌ lark-cli token 已过期，请运行: lark-cli auth login --recommend');
    process.exit(1);
  } catch (e) {
    console.error('❌ 读取 lark-cli token 失败:', e.message);
    console.error('   请确认已运行: lark-cli auth login --recommend');
    process.exit(1);
  }
}

// ==================== 任务附件操作 ====================

async function cmdTaskAttach(taskGuid, filePath) {
  const token = requireToken();
  const fileName = path.basename(filePath);
  const fileData = fs.readFileSync(filePath);
  console.log(`上传任务附件: ${fileName} (${(fileData.length / 1024).toFixed(1)} KB) -> 任务 ${taskGuid}`);

  const res = await multipartUpload('/open-apis/task/v2/attachments/upload', token, {
    resource_type: 'task', resource_id: taskGuid,
  }, fileName, fileData);

  if (res.code === 0) {
    const item = res.data.items[0];
    console.log('✅ 成功 guid:', item.guid, 'file_token:', item.file_token);
    return item;
  } else {
    console.error('❌ 失败:', res.msg); process.exit(1);
  }
}

async function cmdTaskDownload(attachGuid, outPath) {
  const token = requireToken();
  console.log(`下载任务附件: ${attachGuid} -> ${outPath}`);

  const detail = await httpsRequest('GET', `https://open.feishu.cn/open-apis/task/v2/attachments/${attachGuid}`, null, { 'Authorization': 'Bearer ' + token });
  if (detail.code !== 0) { console.error('❌ 获取附件详情失败:', detail.msg); process.exit(1); }

  const url = detail.data.attachment.url;
  const size = await downloadUrl(url, outPath);
  console.log(`✅ 成功: ${(size / 1024).toFixed(1)} KB`);
  return size;
}

// ==================== CLI 入口 ====================

const [,, cmd, ...args] = process.argv;
const HELP = `
飞书直接 HTTP 调用脚本 — 复用 lark-cli 凭据（macOS Keychain）

前提：已通过 lark-cli auth login 完成授权

用法：
  FT=.kiro/skills/lark-assistant/lark-scripts.js

  node $FT task-attach <task_guid> <文件路径>       上传任务附件
  node $FT task-download <attach_guid> <输出路径>   下载任务附件
`;

(async () => {
  switch (cmd) {
    case 'task-attach': await cmdTaskAttach(args[0], args[1]); break;
    case 'task-download': await cmdTaskDownload(args[0], args[1]); break;
    default: console.log(HELP);
  }
})().catch(e => { console.error('❌', e.message); process.exit(1); });
