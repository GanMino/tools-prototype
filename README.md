# 工具集 · 8-BIT TOOLBOX

塞尔达传说（红白机 NES）像素风的在线工具集合原型。

## 功能

| 工具 | 说明 |
| --- | --- |
| JSON 格式化 | 格式化 / 压缩 / 校验 JSON |
| URL 编解码 | URL 编码（encodeURIComponent）与解码 |
| Base64 编解码 | Base64 编码与解码，支持中文 UTF-8 |
| 时间戳转换 | Unix 时间戳（秒）与日期时间互转 |
| WebSocket | WebSocket 连接与消息收发调试 |
| MQTT | MQTT 订阅 / 发布调试（WebSocket 连接） |
| UUID 生成 | 批量生成 UUID v4 |
| 哈希计算 | MD5 / SHA-1 / SHA-256 / SHA-512 |
| 正则测试 | 正则匹配与高亮测试 |
| 颜色转换 | HEX / RGB / HSL 互转 |
| 二维码生成 | 文本 / 网址生成二维码，可下载 PNG |
| JWT 解析 | 解析 JWT 的 Header 与 Payload |
| URL 解析器 | 解析 URL 组成与查询参数 |
| HMAC 计算 | HMAC-MD5 / SHA1 / SHA256 / SHA512 |
| 进制转换 | 二进制 / 八进制 / 十进制 / 十六进制互转 |
| 字符统计 | 字符 / 单词 / 行 / 字节 / 中文字数统计 |
| 大小写转换 | 大写 / 小写 / 首字母 / 反转 |
| 随机密码 | 生成强随机密码 |
| Cron 调试 | Linux / Spring / Quartz 定时表达式解析与下次执行时间 |
| JSON ↔ YAML | JSON 与 YAML 双向转换 |
| JSON ↔ CSV | JSON 对象数组与 CSV 表格互转 |
| HTML 实体 | HTML 特殊字符编码与解码 |
| 人民币大写 | 数字金额转中文大写 |
| 图片转 Base64 | 图片与 Base64 互转（本地处理） |
| Markdown 预览 | Markdown 实时预览 |
| SQL 格式化 | SQL 语句格式化（多方言） |
| 文本 Diff 对比 | 两段文本差异对比 |
| 二维码解码 | 识别二维码图片内容 |

## 特点

- 🎮 塞尔达 NES 像素风：金色标题、对话窗、三角力量 Logo、生命心、瓦片地图背景
- 📱 PC / 手机双端自适应，输入区 / 展示区双栏全高布局（桌面左右、手机上下）
- 🔒 纯前端实现，数据全程在浏览器本地处理，不上传服务器
- 🔤 中文字体采用缝合像素字体 Fusion Pixel（MIT 开源），英文用 Press Start 2P（OFL）

## 运行

依赖任意一个静态文件服务器，推荐 Python 3 自带的：

```bash
python3 server.py
# 浏览器打开 http://127.0.0.1:4180/
```

也可以直接用 npx serve、VS Code Live Server 等托管本目录。

## 技术栈

- 原生 HTML + CSS + JavaScript（单文件 index.html，无构建步骤）
- 字体：Fusion Pixel 12px（MIT）+ Press Start 2P（Google Fonts, OFL）
- 配色：NES PPU（2C02）官方调色板

## 预览

截图见 `screenshots/` 目录。

## License

待定（如需开源可加 MIT）。
