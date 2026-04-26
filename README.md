# Python 数据处理命令速查 (Py Data Desk)

一个**离线可用的** Python 数据处理指令查询网页，无需安装任何依赖，直接双击 HTML 文件即可使用。

![Version](https://img.shields.io/badge/version-v3.1.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 功能特点

- **离线使用** - 所有数据内置在 HTML 中，双击即可打开，无网络依赖
- **多库覆盖** - 覆盖 pandas、NumPy、SciPy、seaborn、matplotlib 及 Python 标准库
- **场景导航** - 按数据处理流程场景引导，方便新手入门
- **完整参数** - 每个指令包含学习优先参数 + 官方完整参数折叠区
- **可视化预览** - 每类指令配有 SVG 图形示意
- **双语支持** - 支持中文任务名和英文函数名搜索

---

## 快速开始

```bash
# 方式一：直接双击打开
open index.html   # macOS
start index.html  # Windows

# 方式二：使用本地服务器（可选）
python -m http.server 8000
# 然后访问 http://localhost:8000
```

---

## 库覆盖范围

| 库 | 指令数 | 主要功能 |
|---|---|---|
| **pandas** | 40+ | 表格读写、数据清洗、筛选、聚合、连接、变换、透视表 |
| **NumPy** | 30+ | 数组创建、形状变换、数学运算、随机数、线性代数、文件IO |
| **SciPy** | 25+ | 统计检验、信号处理、插值优化、曲线拟合、分布函数 |
| **seaborn** | 16+ | 散点图、折线图、箱线图、热力图、分布图 |
| **matplotlib** | 20+ | 基础绑图、子图布局、样式设置、图像保存 |
| **Python** | 25+ | os, json, re, datetime, glob, pathlib 等标准库 |
| **collections** | 5+ | Counter, defaultdict, OrderedDict, namedtuple, deque |

---

## 使用技巧

| 操作 | 方法 |
|---|---|
| 快速搜索 | 直接在搜索框输入，如 `merge`、`去重`、`ttest` |
| 筛选库 | 点击左侧导航栏的库名 |
| 筛选类别 | 点击顶部分类标签（读写文件、查看数据、清洗等） |
| 查看完整参数 | 点击卡片底部的「查看完整参数」折叠区 |
| 复制示例 | 点击卡片右上角「复制」按钮 |

---

## 参数文档说明

每个指令包含两种参数展示：

1. **📌 学习优先参数**（默认展开）
   - 最常用的 3-5 个参数
   - 包含参数含义、使用场景、注意事项

2. **完整参数**（需展开查看）
   - 来自官方文档的完整参数列表
   - 包含类型、默认值、详细说明

---

## 官方文档入口

- [pandas 官方文档](https://pandas.pydata.org/docs/reference/index.html)
- [NumPy 官方文档](https://numpy.org/doc/stable/reference/index.html)
- [SciPy 官方文档](https://docs.scipy.org/doc/scipy/reference/index.html)
- [seaborn 官方文档](https://seaborn.pydata.org/api.html)
- [matplotlib 官方文档](https://matplotlib.org/stable/api/index.html)
- [Python 官方文档](https://docs.python.org/3/library/index.html)
- [collections 官方文档](https://docs.python.org/3/library/collections.html)

---

## 版本历史

| 版本 | 更新内容 |
|---|---|
| **v3.1.1** | 新增 Python 标准库（os, json, re, datetime, glob, pathlib）、collections 容器库；扩展 scipy/numpy/pandas 指令共 20+ 条 |
| **v3.0** | 增强参数文档，添加官方完整参数、类型标签、必需/可选标识、默认值显示、参数折叠区 |
| **v2.0** | 添加 SciPy 库支持、14 类 SVG 图形预览、场景导航增强 |
| **v1.0** | 初始版本，支持 pandas、NumPy、seaborn、matplotlib 基础指令 |

---

## 项目结构

```
PYDataAnalysisTools/
├── index.html      # 主文件（离线可运行）
├── README.md       # 项目说明文档
├── build_html.py   # HTML 构建脚本
├── chart_examples.json  # 图表示例数据
└── generate_charts.py   # 图表生成脚本
```

---

## 适用场景

- 📚 **学习 Python 数据处理** - 快速查询不知道怎么写的函数
- 🔧 **日常数据清洗** - 不确定参数用法时即时查看
- 📊 **制作数据报告** - 复制示例代码到 Jupyter Notebook
- 🎓 **教学演示** - 离线环境直接展示，无需配置环境

---

## License

MIT License - 可自由使用、修改和分发。