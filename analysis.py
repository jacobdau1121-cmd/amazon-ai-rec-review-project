import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# 自动创建output文件夹，解决图片保存报错
if not os.path.exists("C:\\Users\\86139\\OneDrive\\桌面\\output"):
    os.makedirs("C:\\Users\\86139\\OneDrive\\桌面\\output")

# 你的TSV文件相对路径
tsv_file_path = "C:\\Users\\86139\\OneDrive\\桌面\\amazon_reviews_us_Electronics_v1_00.tsv"

# ===================== 2. 读取TSV原始数据 =====================
df = pd.read_csv(tsv_file_path, sep="\t", on_bad_lines="skip")

print("="*50)
print("Data Basic Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())
print("\nTotal Rows:", len(df))
print("="*50)

# ===================== 3. 数据清洗 =====================
core_columns = ["customer_id", "product_id", "star_rating", "helpful_votes"]
df_clean = df.dropna(subset=core_columns).copy()
print(f"\nValid rows after dropping missing values: {len(df_clean)}")

df_clean = df_clean[df_clean["star_rating"].between(1, 5)]
print(f"Valid rows after filtering invalid ratings: {len(df_clean)}")

if len(df_clean) == 0:
    print("ERROR: No valid data left! Check your TSV file content.")
    exit()

if len(df_clean) > 50000:
    df_clean = df_clean.sample(n=50000, random_state=42)
    print(f"Randomly sampled 50000 rows for analysis")

# ===================== 4. 构造AI推荐分组标签 =====================
median_votes = df_clean["helpful_votes"].median()
df_clean["is_ai_recommend"] = np.where(
    (df_clean["star_rating"] >= 4) & (df_clean["helpful_votes"] >= median_votes),
    1,
    0
)

print("\n" + "="*50)
print("AI Recommendation Group Count:")
print(df_clean["is_ai_recommend"].value_counts())
print("="*50)

# ===================== 5. 核心统计分析 =====================
group_stats = df_clean.groupby("is_ai_recommend").agg(
    Avg_Rating=("star_rating", "mean"),
    Avg_Helpful_Votes=("helpful_votes", "mean"),
    Sample_Size=("product_id", "count")
).round(2)
print("\nCore Indicator Comparison (AI Recommended vs Non-Recommended):")
print(group_stats)

group_ai = df_clean[df_clean["is_ai_recommend"] == 1]["star_rating"]
group_normal = df_clean[df_clean["is_ai_recommend"] == 0]["star_rating"]
t_score, p_value = stats.ttest_ind(group_ai, group_normal, equal_var=False)
print(f"\nT-test for star rating difference: t={t_score:.2f}, p={p_value:.4f}")

corr_matrix = df_clean[["star_rating", "helpful_votes"]].corr().round(2)
print("\nCorrelation Matrix:")
print(corr_matrix)
print("="*50)

# ===================== 6. 可视化绘图 =====================
plt.rcParams["axes.unicode_minus"] = False

# 1. 评分对比柱状图
plt.figure(figsize=(10, 6))
sns.barplot(x="is_ai_recommend", y="star_rating", hue="is_ai_recommend", data=df_clean, palette="Set2", legend=False)
plt.title("Average Star Rating: AI Recommended vs Non-Recommended Products", fontsize=14)
plt.xlabel("AI Recommendation (0 = No, 1 = Yes)", fontsize=12)
plt.ylabel("Average Star Rating", fontsize=12)
plt.ylim(0, 5)
plt.savefig("../output/rating_compare.png", dpi=300, bbox_inches="tight")
plt.close()

# 2. 投票箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(x="is_ai_recommend", y="helpful_votes", hue="is_ai_recommend", data=df_clean, palette="Set2", legend=False)
plt.title("Helpful Votes Distribution by Recommendation Group", fontsize=14)
plt.xlabel("AI Recommendation (0 = No, 1 = Yes)", fontsize=12)
plt.ylabel("Number of Helpful Votes", fontsize=12)
plt.savefig("../output/votes_boxplot.png", dpi=300, bbox_inches="tight")
plt.close()

# 3. 热力图
plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap of Rating & Helpful Votes", fontsize=14)
plt.savefig("../output/corr_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

print("\n✅ ALL ANALYSIS FINISHED!")
print("✅ Charts saved to /output folder")
# test