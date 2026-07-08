# CLUEDatasetSearch · AI Data Hub

> **为 AI / LLM 开发者打造的中文数据枢纽**  
> 发现、获取、贡献高质量数据集 —— 助力大模型预训练、指令微调、评估与应用

[![Stars](https://img.shields.io/github/stars/Yuuqq/CLUEDatasetSearch?style=social)](https://github.com/Yuuqq/CLUEDatasetSearch)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Yuuqq/CLUEDatasetSearch/pulls)
[![Issues](https://img.shields.io/github/issues/Yuuqq/CLUEDatasetSearch)](https://github.com/Yuuqq/CLUEDatasetSearch/issues)

---

## 🎯 这个 Data Hub 适合谁？

- **大模型开发者**：寻找预训练语料、SFT/指令数据、偏好数据
- **RAG / Agent 开发者**：领域知识数据、长文本、工具使用数据
- **研究人员**：高质量评测 benchmark 和消融实验数据
- **企业落地团队**：垂直领域（法律、医疗、金融、代码、教育）数据

---

## 🚀 快速开始（面向 AI 开发者）

### 1. 在线搜索（最快）
https://www.cluebenchmarks.com/dataSet_search.html

### 2. 本地克隆 + 结构化数据
```bash
git clone https://github.com/Yuuqq/CLUEDatasetSearch.git
cd CLUEDatasetSearch
```

推荐优先查看 `data/` 目录下的 JSON 文件（机器可读 + 丰富元数据）。

---

## 📍a AI 场景推荐数据集分类

我们按照**现代 AI 开发流程**重新组织数据：

### 🔥 预训练 / 基础语料 (Pretraining & Corpus)
- 大规模中文网页、书籍、代码、百科数据
- 推荐用于继续预训练或领域适配
- 示例：高质量中文维基百科过滤版、新闻语料、书籍语料

### 📝 指令微调 / SFT (Instruction Tuning)
- 高质量问答、对话、任务指令数据
- 推荐用于 Supervised Fine-Tuning
- 优先带 `hf_dataset_id` 的数据集

### ❤️ 偏好对齐 / RLHF (Preference & Alignment)
- 人类偏好数据、奖励模型训练数据
- 用于 DPO、PPO、ORPO 等对齐方法

### 📊 评测与 Benchmark (Evaluation)
- 中文综合能力评测（SuperCLUE、CLUE 等）
- 特定能力评测（推理、长文本、代码、数学等）

### 🏥 垂直领域 (Domain-Specific)
- 法律、医疗、金融、代码、教育、政务等
- 适合垂直大模型或 RAG 应用

### 🧩 其他高价值
- 多模态、工具调用、Agent trajectory、合成数据等

---

## 📂 仓库结构（AI 友好版）

```
CLUEDatasetSearch/
├── README.md                    # 本文件（AI Data Hub 总览）
├── CONTRIBUTING.md
├── data/
│   ├── pretraining/             # 预训练语料
│   ├── instruction/             # 指令/SFT 数据
│   ├── preference/              # 偏好/RLHF 数据
│   ├── evaluation/              # 评测 benchmark
│   ├── domain/                  # 垂直领域
│   └── general/                 # 通用/其他
├── scripts/
│   └── validate_datasets.py
└── .github/ISSUE_TEMPLATE/
```

每个子目录下包含：
- `README.md`（人类可读 + 下载指南）
- `*.json`（结构化元数据，含 HF ID、license、size、last_verified 等）

---

## ✨ 精选推荐（部分示例，已结构化）

**预训练推荐**
- `pleisto/wikipedia-cn-20230720-filtered`（高质量中文维基百科）

**指令数据推荐**
- Belle / WizardLM / ShareGPT 中文增强版（持续补充中）

**评测推荐**
- SuperCLUE 系列、CLUE 经典任务

更多数据集正在快速补充中（欢迎 PR）。

---

## 📥 如何下载数据集？

大多数数据集推荐通过以下平台获取（优先级排序）：

1. **Hugging Face Datasets**（最推荐）
   - 直接 `datasets.load_dataset("username/dataset-name")`
   - 自动处理、版本管理、流式下载

2. **ModelScope**（阿里）
   - 国内访问更快，常有中文优化版本

3. **OpenDataLab / WiseModel / 其他**
   - 部分国内独占或更大规模数据

4. **原始来源**（论文附录或官网）
   - 仅在 HF/ModelScope 没有时使用

每个数据集的 JSON 中都会尽量提供 `hf_dataset_id` 和 `download_url`。

---

## 🤝 贡献指南（AI 开发者友好）

我们欢迎以下贡献：
- 添加带 **HF Dataset ID** 的新数据集
- 补充 **license、规模、质量标签**
- 提供 **使用示例 / 推荐场景**
- 报告失效链接或过时信息

详细请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📜 声明

本仓库仅做数据集信息整理与索引，所有数据版权归原作者所有。请遵守各数据集的 License 进行使用。

---

## 🔗 相关资源

- **CLUE 官方**：https://www.cluebenchmarks.com/
- **Hugging Face 中文数据集**：https://huggingface.co/datasets?language=zh
- **ModelScope 数据集**：https://modelscope.cn/datasets

---

**一起把这个仓库打造成中文 AI 开发者最爱用的 Data Hub！**

有任何建议或想添加的数据集，欢迎直接开 Issue 或提交 PR。  
Star ⭐ 支持我们持续维护！