# 工具集 · 8-BIT TOOLBOX

塞尔达传说（红白机 NES）像素风的在线工具集合原型。

## 功能

| 工具 | 说明 |
| --- | --- |
| JSON 格式化 | 格式化 / 压缩 / 校验 JSON |
| URL 编解码 | URL 编码（encodeURIComponent）与解码 |
| Base64 编解码 | Base64 编码与解码，支持中文 UTF-8 |
| 时间戳转换 | Unix 时间戳（秒）与日期时间互转 |

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
