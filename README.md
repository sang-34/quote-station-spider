# 名言爬虫实战项目
一个基于 Python + Requests + BeautifulSoup4 开发的静态网页爬虫项目，专为练习网页解析、翻页爬取与数据存储设计，可爬取 `quotes.toscrape.com` 全站名言数据并导出为 CSV 文件。

---

## 项目结构
```
quote-station-spider/
├── quote_spider.py   # 爬虫主程序
├── README.md         # 项目说明文档
├── .gitignore        # Git忽略文件配置
└── 名言.csv          # 爬取生成的数据文件（运行后自动生成）
```

---

## 技术栈
| 技术/工具 | 用途 |
| :--- | :--- |
| Python 3 | 开发语言 |
| `requests` | 发送HTTP请求，模拟浏览器访问 |
| `BeautifulSoup4` | 解析HTML文档，提取目标数据 |
| `lxml` | 高效HTML解析器 |
| `csv` | 将爬取的数据写入CSV文件 |

---

## 功能说明
1.  **模拟浏览器请求**：通过设置完整请求头（含User-Agent等字段），伪装正常用户访问，避免被服务器拦截。
2.  **多页数据爬取**：通过循环遍历 `page/1/` 至 `page/10/`，实现全站数据的批量爬取。
3.  **数据精准提取**：
    -   使用 `find_all()` 定位所有名言区块
    -   使用 `find()` 提取名言文本与作者信息
    -   使用 `select()` CSS选择器批量提取标签
4.  **数据格式化处理**：将多标签列表通过 `-` 拼接为字符串，兼容单标签、多标签、无标签场景。
5.  **数据持久化存储**：以 `utf-8-sig` 编码写入CSV文件，解决Excel打开中文乱码问题，同时通过 `newline=""` 去除多余空行。

---

## 安装依赖
```bash
pip install requests beautifulsoup4 lxml
```

---

## 运行方式
```bash
# 执行爬虫主程序
python quote_spider.py
```
运行完成后，项目根目录将自动生成 `名言.csv` 文件，包含爬取的所有数据。

---

## 核心代码逻辑
```python
# 翻页爬取核心逻辑
for page in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    # 提取每一页的所有名言数据
    quote_data = soup.find_all('div', class_='quote')
    for item in quote_data:
        quote = item.find("span", class_="text").get_text(strip=True)
        author = item.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in item.select('a.tag')]
        results.append([quote, author, "-".join(tags)])

# 写入CSV文件
with open("./名言.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)
```

---

## 注意事项
1.  **项目用途**：本项目仅用于爬虫学习与技术练习，请勿将其用于商业用途或对目标网站进行高频恶意请求。
2.  **目标网站**：`quotes.toscrape.com` 是专门用于爬虫练习的网站，无反爬限制，适合新手学习。
3.  **爬取频率**：建议添加请求延时（如 `time.sleep(1)`），模拟真人访问节奏，避免给服务器造成压力。
4.  **数据文件**：`名言.csv` 已在 `.gitignore` 中配置忽略，不会被提交到GitHub仓库。

---

## 后续拓展方向
-   增加异常捕获与请求超时处理，提升爬虫稳定性
-   实现自动检测最大页码，无需手动设置10页上限
-   新增数据导出为Excel（`.xlsx`）或JSON格式的功能
-   添加简单的数据可视化，对名言标签、作者分布进行统计分析

---

