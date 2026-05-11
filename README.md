# 名言爬虫实战项目 README.md
## 项目简介
基于 `requests + BeautifulSoup4` 开发的静态网页爬虫，练习 BeautifulSoup 常用解析方法：`find` / `find_all` / `select` CSS选择器，爬取 Quotes to Scrape 网站名言、作者、标签数据，并自动保存为 UTF-8 编码 CSV 文件，适合爬虫入门练手。

## 技术栈
- 编程语言：Python 3
- 网络请求：`requests`
- 网页解析：`BeautifulSoup4`
- 数据存储：内置 `csv` 模块

## 项目文件结构
```
quote-station-spider/
├── quote_spider.py        # 爬虫主程序
├── 名言.csv       # 爬取生成的数据文件
└── README.md      # 项目说明文档
```

## 安装依赖
```bash
pip install requests beautifulsoup4 lxml
```

## 功能说明
1. 模拟浏览器请求，携带请求头伪装正常访问
2. 使用 `find_all` 定位所有名言区块
3. 通过 `find` 提取名言、作者文本
4. 通过 `select` CSS 选择器批量提取标签
5. 将多标签用 `-` 拼接为字符串，兼容单个/多个/无标签场景
6. 自动生成 CSV 文件，采用 `utf-8-sig` 编码，Excel 打开不乱码

## 运行方式
直接执行主程序即可：
```bash
python main.py
```
运行完成后，项目根目录自动生成 `名言.csv` 数据文件。

## 核心知识点总结
1. **BeautifulSoup 解析**
   - `find()`：获取第一个匹配标签
   - `find_all()`：获取所有匹配标签
   - `select()` / `select_one()`：CSS 选择器定位
2. **文本提取**
   - 推荐 `get_text(strip=True)` 替代 `string`，避免空值报错
3. **列表处理**
   - `str.join()` 可将标签列表转为拼接字符串，兼容任意数量标签
4. **CSV 存储**
   - `utf-8-sig` 解决中文乱码
   - `newline=""` 去除 CSV 多余空行

## 注意事项
1. 本项目仅用于**爬虫学习练习**，请勿用于商业用途
2. 目标网站为专业爬虫练习站点，无反爬限制
3. 爬取建议保持合理频率，禁止高频恶意请求

## 后续拓展方向
- 增加分页循环，爬取全站 10 页所有名言
- 增加异常捕获、请求超时处理
- 新增保存为 Excel / JSON 格式
- 增加随机请求延时，模拟真人访问节奏

