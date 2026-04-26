#!/usr/bin/env python3
"""生成图表图片和完整HTML文件"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import base64
import io
import json
import os

# 使用英文避免字体问题
plt.rcParams['font.family'] = 'DejaVu Sans'

def generate_base64_image(fig):
    """将matplotlib图表转换为base64"""
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=80, bbox_inches='tight', facecolor='white')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return f"data:image/png;base64,{img_base64}"

# 生成matplotlib示例图表
def create_matplotlib_examples():
    examples = {}

    # 1. plot - Line plot
    fig, ax = plt.subplots(figsize=(4, 2.5))
    x = np.linspace(0, 10, 50)
    y = np.sin(x)
    ax.plot(x, y, 'b-', linewidth=2)
    ax.set_title('plot - Line Plot', fontsize=10)
    ax.set_xlabel('x')
    ax.set_ylabel('sin(x)')
    ax.grid(True, alpha=0.3)
    examples['plot'] = generate_base64_image(fig)

    # 2. scatter - Scatter plot
    fig, ax = plt.subplots(figsize=(4, 2.5))
    x = np.random.randn(50)
    y = np.random.randn(50)
    ax.scatter(x, y, c='steelblue', s=50, alpha=0.6)
    ax.set_title('scatter - Scatter Plot', fontsize=10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, alpha=0.3)
    examples['scatter'] = generate_base64_image(fig)

    # 3. bar - Bar chart
    fig, ax = plt.subplots(figsize=(4, 2.5))
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 12, 67, 34]
    ax.bar(categories, values, color='steelblue')
    ax.set_title('bar - Bar Chart', fontsize=10)
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.grid(True, alpha=0.3, axis='y')
    examples['bar'] = generate_base64_image(fig)

    # 4. hist - Histogram
    fig, ax = plt.subplots(figsize=(4, 2.5))
    data = np.random.randn(200)
    ax.hist(data, bins=20, color='steelblue', edgecolor='white', alpha=0.7)
    ax.set_title('hist - Histogram', fontsize=10)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.grid(True, alpha=0.3, axis='y')
    examples['hist'] = generate_base64_image(fig)

    # 5. pie - Pie chart
    fig, ax = plt.subplots(figsize=(4, 2.5))
    sizes = [25, 35, 20, 20]
    labels = ['A', 'B', 'C', 'D']
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('pie - Pie Chart', fontsize=10)
    examples['pie'] = generate_base64_image(fig)

    # 6. boxplot - Box plot
    fig, ax = plt.subplots(figsize=(4, 2.5))
    data = [np.random.randn(100), np.random.randn(100) + 1, np.random.randn(100) + 2]
    ax.boxplot(data, tick_labels=['G1', 'G2', 'G3'])
    ax.set_title('boxplot - Box Plot', fontsize=10)
    ax.set_ylabel('Value')
    ax.grid(True, alpha=0.3, axis='y')
    examples['boxplot'] = generate_base64_image(fig)

    # 7. imshow - Heatmap
    fig, ax = plt.subplots(figsize=(4, 2.5))
    data = np.random.rand(10, 10)
    im = ax.imshow(data, cmap='viridis', aspect='auto')
    ax.set_title('imshow - Heatmap', fontsize=10)
    plt.colorbar(im, ax=ax, shrink=0.8)
    examples['imshow'] = generate_base64_image(fig)

    # 8. fill_between - Fill between
    fig, ax = plt.subplots(figsize=(4, 2.5))
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.sin(x) + 0.3
    ax.fill_between(x, y1, y2, alpha=0.3, color='steelblue')
    ax.plot(x, y1, 'b-', linewidth=1)
    ax.plot(x, y2, 'b-', linewidth=1)
    ax.set_title('fill_between - Fill Area', fontsize=10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, alpha=0.3)
    examples['fill_between'] = generate_base64_image(fig)

    # 9. contour - Contour
    fig, ax = plt.subplots(figsize=(4, 2.5))
    x = np.linspace(-3, 3, 50)
    y = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2 + Y**2))
    CS = ax.contour(X, Y, Z, levels=10, cmap='viridis')
    ax.set_title('contour - Contour Plot', fontsize=10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    examples['contour'] = generate_base64_image(fig)

    # 10. subplots - Multiple subplots
    fig, axes = plt.subplots(2, 2, figsize=(5, 4))
    axes[0,0].plot(x, np.sin(x))
    axes[0,0].set_title('Subplot 1')
    axes[0,1].plot(x, np.cos(x), 'r-')
    axes[0,1].set_title('Subplot 2')
    axes[1,0].scatter(x[:20], np.random.randn(20), c='green', s=20)
    axes[1,0].set_title('Subplot 3')
    axes[1,1].bar(['a','b','c'], [3,5,2])
    axes[1,1].set_title('Subplot 4')
    fig.suptitle('subplots - Multiple Subplots', fontsize=10)
    plt.tight_layout()
    examples['subplots'] = generate_base64_image(fig)

    # 11. barh - Horizontal bar
    fig, ax = plt.subplots(figsize=(4, 2.5))
    categories = ['Cat A', 'Cat B', 'Cat C', 'Cat D', 'Cat E']
    values = [23, 45, 12, 67, 34]
    ax.barh(categories, values, color='steelblue')
    ax.set_title('barh - Horizontal Bar', fontsize=10)
    ax.set_xlabel('Value')
    ax.set_ylabel('Category')
    ax.grid(True, alpha=0.3, axis='x')
    examples['barh'] = generate_base64_image(fig)

    # 12. violinplot - Violin plot
    fig, ax = plt.subplots(figsize=(4, 2.5))
    data = [np.random.randn(100) for _ in range(3)]
    parts = ax.violinplot(data, positions=[1, 2, 3], showmeans=True, showmedians=True)
    ax.set_title('violinplot - Violin Plot', fontsize=10)
    ax.set_ylabel('Value')
    ax.grid(True, alpha=0.3, axis='y')
    examples['violinplot'] = generate_base64_image(fig)

    # 13. step - Step plot
    fig, ax = plt.subplots(figsize=(4, 2.5))
    x = np.arange(10)
    y = np.array([1, 3, 2, 5, 4, 6, 5, 7, 6, 8])
    ax.step(x, y, 'b-', linewidth=2, where='mid')
    ax.set_title('step - Step Plot', fontsize=10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, alpha=0.3)
    examples['step'] = generate_base64_image(fig)

    # 14. errorbar - Error bar
    fig, ax = plt.subplots(figsize=(4, 2.5))
    x = np.arange(5)
    y = [3, 5, 4, 6, 5]
    yerr = [0.5, 0.3, 0.4, 0.5, 0.3]
    ax.errorbar(x, y, yerr=yerr, fmt='o', capsize=5, color='steelblue')
    ax.set_title('errorbar - Error Bar', fontsize=10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, alpha=0.3)
    examples['errorbar'] = generate_base64_image(fig)

    # 15. stem - Stem plot
    fig, ax = plt.subplots(figsize=(4, 2.5))
    x = np.arange(10)
    y = np.sin(x) * np.exp(-x*0.1)
    ax.stem(x, y, linefmt='b-', markerfmt='bo', basefmt='r-')
    ax.set_title('stem - Stem Plot', fontsize=10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, alpha=0.3)
    examples['stem'] = generate_base64_image(fig)

    return examples

# 生成seaborn示例图表
def create_seaborn_examples():
    examples = {}
    sns.set_style("whitegrid")

    # 设置示例数据
    tips = sns.load_dataset("tips")
    iris = sns.load_dataset("iris")

    # 1. scatterplot
    try:
        fig, ax = plt.subplots(figsize=(4, 2.5))
        sns.scatterplot(x='total_bill', y='tip', data=tips, ax=ax, color='steelblue')
        ax.set_title('scatterplot - Scatter Plot', fontsize=10)
        examples['scatterplot'] = generate_base64_image(fig)
    except:
        examples['scatterplot'] = None

    # 2. lineplot
    try:
        fig, ax = plt.subplots(figsize=(4, 2.5))
        sns.lineplot(x='size', y='total_bill', data=tips, ax=ax, color='steelblue', errorbar='sd')
        ax.set_title('lineplot - Line Plot', fontsize=10)
        examples['lineplot'] = generate_base64_image(fig)
    except:
        examples['lineplot'] = None

    # 3. barplot
    try:
        fig, ax = plt.subplots(figsize=(4, 2.5))
        sns.barplot(x='day', y='total_bill', hue='day', data=tips, ax=ax, palette='steelblue', legend=False)
        ax.set_title('barplot - Bar Chart', fontsize=10)
        ax.set_xlabel('')
        examples['barplot'] = generate_base64_image(fig)
    except:
        examples['barplot'] = None

    # 4. boxplot
    try:
        fig, ax = plt.subplots(figsize=(4, 2.5))
        sns.boxplot(x='day', y='total_bill', hue='day', data=tips, ax=ax, palette='steelblue', legend=False)
        ax.set_title('boxplot - Box Plot', fontsize=10)
        ax.set_xlabel('')
        examples['boxplot'] = generate_base64_image(fig)
    except:
        examples['boxplot'] = None

    # 5. violinplot
    try:
        fig, ax = plt.subplots(figsize=(4, 2.5))
        sns.violinplot(x='day', y='total_bill', hue='day', data=tips, ax=ax, palette='steelblue', legend=False)
        ax.set_title('violinplot - Violin Plot', fontsize=10)
        ax.set_xlabel('')
        examples['violinplot'] = generate_base64_image(fig)
    except:
        examples['violinplot'] = None

    # 6. histplot
    try:
        fig, ax = plt.subplots(figsize=(4, 2.5))
        sns.histplot(x='total_bill', data=tips, kde=True, ax=ax, color='steelblue')
        ax.set_title('histplot - Histogram', fontsize=10)
        examples['histplot'] = generate_base64_image(fig)
    except:
        examples['histplot'] = None

    # 7. heatmap
    try:
        fig, ax = plt.subplots(figsize=(4, 2.5))
        corr = tips[['total_bill', 'tip', 'size']].corr()
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', ax=ax, square=True, cbar=False)
        ax.set_title('heatmap - Heatmap', fontsize=10)
        examples['heatmap'] = generate_base64_image(fig)
    except:
        examples['heatmap'] = None

    # 8. countplot
    try:
        fig, ax = plt.subplots(figsize=(4, 2.5))
        sns.countplot(x='day', hue='day', data=tips, ax=ax, palette='steelblue', legend=False)
        ax.set_title('countplot - Count Plot', fontsize=10)
        ax.set_xlabel('')
        examples['countplot'] = generate_base64_image(fig)
    except:
        examples['countplot'] = None

    # 9. pairplot
    try:
        fig = plt.figure(figsize=(5, 5))
        sns.pairplot(iris, hue='species', palette='husl', diag_kind='kde')
        plt.close(fig)
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=60, bbox_inches='tight', facecolor='white')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        examples['pairplot'] = f"data:image/png;base64,{img_base64}"
    except:
        examples['pairplot'] = None

    # 10. kdeplot
    try:
        fig, ax = plt.subplots(figsize=(4, 2.5))
        sns.kdeplot(x='total_bill', data=tips, ax=ax, color='steelblue', fill=True)
        ax.set_title('kdeplot - KDE Plot', fontsize=10)
        examples['kdeplot'] = generate_base64_image(fig)
    except:
        examples['kdeplot'] = None

    return examples

# 生成pandas表格变化HTML
def create_pandas_table_examples():
    examples = {}

    # 创建示例DataFrame
    df_original = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'age': [25, 30, 35, 28, 22],
        'city': ['Beijing', 'Shanghai', 'Beijing', 'Shenzhen', 'Shanghai'],
        'score': [85.5, 92.3, 78.9, 88.0, 95.1]
    })

    # 1. head
    examples['head'] = {
        'before': df_original.to_html(index=False, classes='table-demo'),
        'after': df_original.head(3).to_html(index=False, classes='table-demo'),
        'desc': 'Show first 3 rows (default 5)'
    }

    # 2. dropna
    df_with_na = df_original.copy()
    df_with_na.loc[1, 'age'] = np.nan
    df_with_na.loc[3, 'city'] = np.nan
    examples['dropna'] = {
        'before': df_with_na.to_html(index=False, classes='table-demo'),
        'after': df_with_na.dropna().to_html(index=False, classes='table-demo'),
        'desc': 'Drop rows with missing values'
    }

    # 3. fillna
    examples['fillna'] = {
        'before': df_with_na.to_html(index=False, classes='table-demo'),
        'after': df_with_na.fillna(0).to_html(index=False, classes='table-demo'),
        'desc': 'Fill missing values with 0'
    }

    # 4. sort_values
    examples['sort_values'] = {
        'before': df_original.to_html(index=False, classes='table-demo'),
        'after': df_original.sort_values('age').to_html(index=False, classes='table-demo'),
        'desc': 'Sort by age column ascending'
    }

    # 5. groupby
    examples['groupby'] = {
        'before': df_original.to_html(index=False, classes='table-demo'),
        'after': df_original.groupby('city')['score'].mean().reset_index().to_html(index=False, classes='table-demo'),
        'desc': 'Group by city, calculate mean score'
    }

    # 6. merge
    df_scores = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'grade': ['A', 'B', 'A']
    })
    examples['merge'] = {
        'before': f"<b>df1:</b><br>{df_original[['name', 'age']].head(3).to_html(index=False, classes='table-demo')}<br><b>df2:</b><br>{df_scores.to_html(index=False, classes='table-demo')}",
        'after': pd.merge(df_original[['name', 'age']].head(3), df_scores, on='name').to_html(index=False, classes='table-demo'),
        'desc': 'Merge two tables on name column'
    }

    # 7. pivot_table
    df_sales = pd.DataFrame({
        'product': ['A', 'A', 'B', 'B', 'A', 'B'],
        'region': ['North', 'South', 'North', 'South', 'East', 'West'],
        'sales': [100, 150, 200, 180, 120, 220]
    })
    examples['pivot_table'] = {
        'before': df_sales.to_html(index=False, classes='table-demo'),
        'after': df_sales.pivot_table(values='sales', index='product', columns='region', aggfunc='sum').to_html(classes='table-demo'),
        'desc': 'Create pivot table: product x region sales'
    }

    # 8. loc
    examples['loc'] = {
        'before': df_original.to_html(index=False, classes='table-demo'),
        'after': df_original.loc[df_original['age'] > 25].to_html(index=False, classes='table-demo'),
        'desc': 'Filter rows where age > 25'
    }

    # 9. value_counts
    examples['value_counts'] = {
        'before': df_original.to_html(index=False, classes='table-demo'),
        'after': df_original['city'].value_counts().to_frame().to_html(classes='table-demo'),
        'desc': 'Count unique values in city column'
    }

    # 10. astype
    examples['astype'] = {
        'before': df_original[['name', 'age']].to_html(index=False, classes='table-demo'),
        'after': df_original[['name', 'age']].astype({'age': float}).to_html(index=False, classes='table-demo'),
        'desc': 'Convert age to float type'
    }

    # 11. drop_duplicates
    df_dup = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Alice', 'David'],
        'score': [85, 92, 85, 88]
    })
    examples['drop_duplicates'] = {
        'before': df_dup.to_html(index=False, classes='table-demo'),
        'after': df_dup.drop_duplicates().to_html(index=False, classes='table-demo'),
        'desc': 'Remove duplicate rows (keep first)'
    }

    # 12. rename
    examples['rename'] = {
        'before': df_original[['name', 'score']].to_html(index=False, classes='table-demo'),
        'after': df_original[['name', 'score']].rename(columns={'name': 'Name', 'score': 'Score'}).to_html(index=False, classes='table-demo'),
        'desc': 'Rename column names'
    }

    # 13. apply
    examples['apply'] = {
        'before': df_original[['name', 'age']].to_html(index=False, classes='table-demo'),
        'after': df_original[['name', 'age']].copy().assign(age_group=df_original['age'].apply(lambda x: 'Young' if x < 30 else 'Senior')).to_html(index=False, classes='table-demo'),
        'desc': 'Add age group column'
    }

    # 14. concat
    df1 = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})
    df2 = pd.DataFrame({'name': ['Charlie', 'David'], 'age': [35, 28]})
    examples['concat'] = {
        'before': f"<b>df1:</b><br>{df1.to_html(index=False, classes='table-demo')}<br><b>df2:</b><br>{df2.to_html(index=False, classes='table-demo')}",
        'after': pd.concat([df1, df2]).to_html(index=False, classes='table-demo'),
        'desc': 'Concatenate two tables vertically'
    }

    # 15. query
    examples['query'] = {
        'before': df_original.to_html(index=False, classes='table-demo'),
        'after': df_original.query('age > 25 & city == "Beijing"').to_html(index=False, classes='table-demo'),
        'desc': 'Filter: age > 25 AND city == "Beijing"'
    }

    return examples

def generate_html():
    """生成完整的HTML文件"""

    matplotlib_examples = create_matplotlib_examples()
    seaborn_examples = create_seaborn_examples()
    pandas_tables = create_pandas_table_examples()

    # 保存图表为JSON
    with open('chart_examples.json', 'w', encoding='utf-8') as f:
        json.dump({
            'matplotlib': matplotlib_examples,
            'seaborn': seaborn_examples,
            'pandas_tables': pandas_tables
        }, f, ensure_ascii=False, indent=2)

    print("Charts and tables generated!")
    print(f"matplotlib examples: {len(matplotlib_examples)}")
    print(f"seaborn examples: {len([x for x in seaborn_examples.values() if x])}")
    print(f"pandas table examples: {len(pandas_tables)}")

if __name__ == '__main__':
    generate_html()