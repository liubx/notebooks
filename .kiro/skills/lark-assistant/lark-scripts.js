#!/usr/bin/env node
/**
 * 飞书直接 HTTP 调用脚本 — lark-cli / lark-mcp 都无法处理的场景
 *
 * 当前唯一必须使用本脚本的场景：任务附件上传（multipart/form-data）
 * 其他场景说明：
 *   - 云空间文件上传/下载 → 用 lark-cli drive +upload/+download
 *   - 任务附件下载 → 可用 lark-mcp task.v2.attachment.get 获取临时 URL 后 curl 下载
 *   - 任务附件列表/删除 → 可用 lark-mcp task.v2.attachment.list/delete
 *
 * 用法：
 *   FT=.kiro/skills/lark-assistant/lark-scripts.js
 *   node $FT auth                                        # 获取/刷新 OAuth token
 *   node $FT task-attach <task_guid> <本地文件>           # 上传任务附件（唯一必须场景）
 *   node $FT task-download <attach_guid> <输出路径>       # 下载任务附件（备用，也可用 lark-mcp + curl）
 */

const https = require('https');
const http = require('http');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const APP_ID = 'cli_a7819fab58b11013';
const APP_SECRET = 'aMa8UUE3zZnCpI2HkwCdIeaRY1TdmI3F';
const TOKEN_FILE = path.join(__dirname, 'lark-token.json');
const SCOPES = 'task:attachment:write task:task';

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

// ==================== Token 管理 ====================

function getToken() {
  if (!fs.existsSync(TOKEN_FILE)) return null;
  const data = JSON.parse(fs.readFileSync(TOKEN_FILE, 'utf-8'));
  if (new Date(data.expires_at) < new Date()) {
    console.log('⚠️  Token 已过期，请运行: node ' + __filename + ' auth');
    return null;
  }
  return data.user_access_token;
}

function requireToken() {
  const token = getToken();
  if (!token) { console.error('❌ 无有效 token，请先运行: node ' + __filename + ' auth'); process.exit(1); }
  return token;
}

async function cmdAuth() {
  const REDIRECT_URI = 'http://localhost:3000/callback';
  const authUrl = `https://open.feishu.cn/open-apis/authen/v1/authorize?app_id=${APP_ID}&redirect_uri=${encodeURIComponent(REDIRECT_URI)}&response_type=code&scope=${encodeURIComponent(SCOPES)}`;

  const server = http.createServer(async (req, res) => {
    const url = new URL(req.url, 'http://localhost:3000');
    if (url.pathname === '/callback') {
      const code = url.searchParams.get('code');
      if (!code) { res.writeHead(400); res.end('无授权码'); return; }
      console.log('收到授权码:', code);
      try {
        const appRes = await httpsRequest('POST', 'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal', { app_id: APP_ID, app_secret: APP_SECRET });
        if (appRes.code !== 0) throw new Error('app_token: ' + JSON.stringify(appRes));
        const tokenRes = await httpsRequest('POST', 'https://open.feishu.cn/open-apis/authen/v1/oidc/access_token',
          { grant_type: 'authorization_code', code }, { Authorization: `Bearer ${appRes.app_access_token}` });
        if (tokenRes.code === 0 && tokenRes.data) {
          const info = {
            user_access_token: tokenRes.data.access_token, refresh_token: tokenRes.data.refresh_token,
            expires_in: tokenRes.data.expires_in, created_at: new Date().toISOString(),
            expires_at: new Date(Date.now() + tokenRes.data.expires_in * 1000).toISOString(),
          };
          fs.writeFileSync(TOKEN_FILE, JSON.stringify(info, null, 2));
          console.log('✅ Token 获取成功，过期:', info.expires_at);
          res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
          res.end('<h1>✅ 授权成功</h1><p>可关闭此页面</p>');
        } else {
          console.error('❌ 失败:', JSON.stringify(tokenRes));
          res.writeHead(500); res.end('失败');
        }
      } catch (e) { console.error('❌', e.message); res.writeHead(500); res.end(e.message); }
      setTimeout(() => { server.close(); process.exit(0); }, 1000);
    } else { res.writeHead(302, { Location: authUrl }); res.end(); }
  });
  server.listen(3000, () => { console.log('🚀 http://localhost:3000'); exec('open "' + authUrl + '"'); });
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
飞书直接 HTTP 调用脚本（lark-cli / lark-mcp 无法处理的场景）

用法：
  FT=.kiro/skills/lark-assistant/lark-scripts.js

  node $FT auth                                    获取/刷新 OAuth token
  node $FT task-attach <task_guid> <文件路径>       上传任务附件（唯一必须场景）
  node $FT task-download <attach_guid> <输出路径>   下载任务附件（备用）
`;

(async () => {
  switch (cmd) {
    case 'auth': await cmdAuth(); break;
    case 'task-attach': await cmdTaskAttach(args[0], args[1]); break;
    case 'task-download': await cmdTaskDownload(args[0], args[1]); break;
    default: console.log(HELP);
  }
})().catch(e => { console.error('❌', e.message); process.exit(1); });
