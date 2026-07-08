# CLUEDatasetSearch · AI Data Hub

> **A Chinese Data Hub built for AI / LLM developers**  
> Discover, access, and contribute high-quality datasets for LLM pretraining, instruction tuning, evaluation, and real-world applications.

[![Stars](https://img.shields.io/github/stars/Yuuqq/CLUEDatasetSearch?style=social)](https://github.com/Yuuqq/CLUEDatasetSearch)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Yuuqq/CLUEDatasetSearch/pulls)
[![Issues](https://img.shields.io/github/issues/Yuuqq/CLUEDatasetSearch)](https://github.com/Yuuqq/CLUEDatasetSearch/issues)

---

## 🎯 Who is this Data Hub for?

- **LLM Developers**: Looking for pretraining corpora, SFT/instruction data, and preference data
- **RAG / Agent Developers**: Domain knowledge, long-context, and tool-use datasets
- **Researchers**: High-quality evaluation benchmarks and ablation datasets
- **Industry Teams**: Vertical domain data (legal, medical, finance, code, education)

---

## 🚀 Quick Start (for AI Developers)

### 1. Online Search (Fastest)
https://www.cluebenchmarks.com/dataSet_search.html

### 2. Local Clone + Structured Data
```bash
git clone https://github.com/Yuuqq/CLUEDatasetSearch.git
cd CLUEDatasetSearch
```

We recommend starting with the structured JSON files in the `data/` directory.

---

## 📍a Recommended Categories for AI Workflows

We organize datasets according to the modern AI development pipeline:

### 🔥 Pretraining & Foundation Corpora
- Large-scale Chinese web, books, code, and encyclopedia data
- Ideal for continued pretraining or domain adaptation

### 📝 Instruction Tuning / SFT
- High-quality QA, conversation, and task instruction data
- Recommended for Supervised Fine-Tuning

### ❤️ Preference & Alignment (RLHF / DPO)
- Human preference data and reward model training data
- For DPO, PPO, ORPO, and other alignment methods

### 📊 Evaluation & Benchmarks
- Chinese comprehensive capability benchmarks (SuperCLUE, CLUE, etc.)
- Specific capability evaluation (reasoning, long-context, code, math)

### 🏥 Domain-Specific
- Legal, medical, finance, code, education, government, etc.
- Perfect for vertical LLMs or RAG applications

---

## 📂 Repository Structure (AI-Friendly)

```
CLUEDatasetSearch/
├── README.md
├── README_EN.md
├── CONTRIBUTING.md
├── data/
│   ├── pretraining/
│   ├── instruction/
│   ├── preference/
│   ├── evaluation/
│   └── domain/
├── scripts/
└── .github/ISSUE_TEMPLATE/
```

---

## ✨ Featured Recommendations

- **Pretraining**: `pleisto/wikipedia-cn-20230720-filtered` (High-quality Chinese Wikipedia)
- **Instruction Data**: Belle / WizardLM Chinese enhanced versions (continuously updated)
- **Evaluation**: SuperCLUE series, classic CLUE tasks

More high-quality datasets are being added rapidly.

---

## 📥 How to Download Datasets?

Recommended sources (in order of preference):

1. **Hugging Face Datasets** (Strongly Recommended)
2. **ModelScope** (Often faster in China)
3. Original sources

Most dataset entries include `hf_dataset_id` in their JSON metadata.

---

## 🤝 Contribution Guide

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📜 Disclaimer

This repository only indexes publicly available dataset information. All copyrights belong to the original authors.

---

## 🔗 Related Resources

- **CLUE Official**: https://www.cluebenchmarks.com/
- **Hugging Face Chinese Datasets**: https://huggingface.co/datasets?language=zh

---

## 🔄 Relationship with the Original Repository

This repository is a **community-maintained and modernized fork** of [CLUEbenchmark/CLUEDatasetSearch](https://github.com/CLUEbenchmark/CLUEDatasetSearch).

### Key Differences:

| Aspect              | Original (CLUEbenchmark)          | This Repo (Yuuqq maintained)                  |
|---------------------|-----------------------------------|-----------------------------------------------|
| **Maintenance**     | Largely inactive since 2022       | Actively maintained (2026 updates ongoing)    |
| **Goal**            | Static dataset list               | **Dynamic AI-oriented Data Hub**              |
| **Data Format**     | Markdown tables only              | **Structured JSON** + Markdown (dual-track)   |
| **Dataset Freshness**| Mostly 2017–2020 data             | Prioritizes 2023–2026 high-quality AI data    |
| **AI Focus**        | General NLP listing               | Categorized for Pretraining / SFT / RLHF / Eval / Domain |
| **Contribution**    | Traditional issues                | Standardized templates + JSON-first           |
| **Download**        | Few HF links                      | **HF-first** + ModelScope                     |
| **Documentation**   | Chinese only                      | **Bilingual** (README + README_EN)            |

**Our mission**: Preserve the spirit of the original project while transforming it into a **long-term maintainable, AI-developer-friendly** Chinese NLP / LLM Data Hub.

---

**Making Chinese AI dataset discovery and sharing simple and efficient!**

Suggestions and new dataset submissions via Issues or PRs are highly welcome.  
Star ⭐ to support ongoing maintenance!