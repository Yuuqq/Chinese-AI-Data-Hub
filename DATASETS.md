# CLUEDatasetSearch - Datasets Overview

> **Auto-generated overview** of all datasets. Use `Ctrl+F` to search.

This file is **automatically updated** via GitHub Actions when datasets change.

---

## 📍a Quick Reference

- **HF Dataset ID** links are preferred for downloading.
- See individual JSON files in `data/` for full metadata.
- Last generated: 2026-07-09 04:26 UTC

---

## 🔥 Pretraining & Foundation Corpora

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| Chinese Books Corpus 2025 (High-Quality) | - | ~500GB | llm-pretraining, long-context-pretraining | 2026-07-08 | active | 2025年高质量中文书籍语料，适合大模型预训练 |
| Chinese Wikipedia 2023 Filtered | [pleisto/wikipedia-cn-20230720-filtered](https://huggingface.co/datasets/pleisto/wikipedia-cn-20230720-filtered) | 230,000 examples | llm-pretraining, continued-pretraining, rag | 2026-07-08 | active | Strongly recommended for Chinese LLM pretraining |
| Large Chinese Web Corpus 2024 (Filtered) | - | 数百GB级别 | llm-pretraining, domain-adaptation | 2026-07-08 | active | Recent large-scale Chinese web data (community filtered versions available on HF |

## 📝 Instruction Tuning / SFT

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| BELLE 3.5M Chinese Instruction Data | [BelleGroup/train_3.5M_CN](https://huggingface.co/datasets/BelleGroup/train_3.5M_CN) | 3,500,000 examples | sft, llm-finetuning | 2026-07-08 | active | Classic large-scale Chinese SFT dataset |
| Magpie Chinese Instruction Dataset (2025) | - | 大规模高质量指令数据 | sft, llm-finetuning | 2026-07-08 | active | Recent high-quality synthetic Chinese instruction data |
| Qwen Instruct 2025 (High-Quality Chinese) | [Qwen/Qwen-Instruct-2025-CN](https://huggingface.co/datasets/Qwen/Qwen-Instruct-2025-CN) | 2,000,000 examples | sft, reasoning-llm, agent | 2026-07-08 | active | 2025年Qwen团队发布的高质量中文指令数据 |
| WizardLM Evol-Instruct Chinese | [WizardLM/WizardLM_evol_instruct_V2_196k](https://huggingface.co/datasets/WizardLM/WizardLM_evol_instruct_V2_196k) | 196,000 examples | sft, reasoning-llm | 2026-07-08 | active | Good for improving reasoning ability |

## ❤️ Preference & Alignment (RLHF / DPO)

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| Chinese Preference Dataset 2025 (High-Quality) | - | 大规模偏好数据 | rlhf, dpo, alignment | 2026-07-08 | active | 2025最新高质量中文偏好数据，推荐用于对齐训练 |
| DPO Chinese Preference 2026 | [OpenChineseLLM/DPO-Chinese-2026](https://huggingface.co/datasets/OpenChineseLLM/DPO-Chinese-2026) | 150,000 examples | dpo, alignment | 2026-07-08 | active | 2026年最新DPO专用中文偏好数据 |
| UltraFeedback Chinese Preference Data | [HuggingFaceH4/ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized) | 60,000 examples | rlhf, dpo, alignment | 2026-07-08 | active | High quality preference data for alignment |

## 📏 Long-Context Data

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| InfiniteBench Chinese | - | 超长上下文数据 | long-context-llm | 2026-07-08 | active | 适合测试超长上下文能力 |
| Long-Context SFT Chinese 2026 | [ChineseLLM/Long-SFT-2026](https://huggingface.co/datasets/ChineseLLM/Long-SFT-2026) | 500,000 examples | long-context-llm, rag-long-context | 2026-07-08 | active | 2026年长上下文SFT专用高质量数据 |
| LongBench Chinese 2025 | - | 多任务长上下文数据 | long-context-llm, rag-long-context | 2026-07-08 | active | 2025更新版中文长上下文 benchmark 和训练数据 |

## 📊 Evaluation & Benchmarks

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| AgentBench Chinese 2026 | [AgentEval/AgentBench-Chinese-2026](https://huggingface.co/datasets/AgentEval/AgentBench-Chinese-2026) | Multiple agent tasks | agent, tool-use-evaluation | 2026-07-08 | active | 2026年中文Agent能力评测 benchmark |
| C-Eval Chinese Evaluation Benchmark | [ceval/ceval-exam](https://huggingface.co/datasets/ceval/ceval-exam) | Multiple subjects | evaluation, chinese-llm | 2026-07-08 | active | Widely used Chinese evaluation benchmark |
| SuperCLUE 2025 Chinese LLM Evaluation | - | Multiple tasks | evaluation, model-comparison | 2026-07-08 | active | Latest SuperCLUE benchmark |

## 🧩 Traditional NLP Tasks

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| CLUE Fine-Grain NER (CLUENER2020) | - | 12,091 examples | ner-evaluation, fine-grained-ner | 2026-07-08 | active | CLUE classic fine-grained NER dataset |
| MSRA NER Dataset | - | 46,365 examples | ner-evaluation, baseline | 2026-07-08 | active | Classic Chinese NER benchmark |

## 🏥 Domain-Specific

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| CJRC Chinese Legal Reading Comprehension | - | 50,000 examples | legal-llm, rag-legal | 2026-07-08 | active | Classic Chinese legal domain dataset |
| Chinese Financial Domain Dataset 2025 | [FinancialAI/Finance-Chinese-2025](https://huggingface.co/datasets/FinancialAI/Finance-Chinese-2025) | 300,000 examples | finance-llm, rag-finance | 2026-07-08 | active | 2025年高质量中文金融领域数据集 |
| cMedQA Chinese Medical QA | - | 200,000 examples | medical-llm, rag-medical | 2026-07-08 | active | Widely used Chinese medical QA dataset |

---

## Notes

- This table is generated from `data/**/*.json` files.
- To add a new dataset, add a JSON entry in the appropriate folder and the table will update automatically.
- For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

> **Last updated**: 2026-07-09