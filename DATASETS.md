# CLUEDatasetSearch - Datasets Overview

> **Auto-generated overview** of all datasets. Use `Ctrl+F` to search.

This file is **automatically updated** via GitHub Actions when datasets change.

---

## 📍a Quick Reference

- **HF Dataset ID** links are preferred for downloading.
- See individual JSON files in `data/` for full metadata.
- Last generated: 2026-07-10 08:22 UTC

---

## 🔥 Pretraining & Foundation Corpora

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| BAAI CCI3.0-HQ (High-Quality Chinese Pretraining Corpus) | [BAAI/CCI3-HQ](https://huggingface.co/datasets/BAAI/CCI3-HQ) | 500GB high-quality Chinese text | llm-pretraining, continued-pretraining | 2026-07-09 | active | Excellent: High-quality filtered Chinese pretraining data from BAAI |
| Chinese Books Corpus 2025 (High-Quality) | - | ~500GB | llm-pretraining, long-context-pretraining | 2026-07-09 | active | 2025年高质量中文书籍语料，适合大模型预训练 |
| Chinese Wikipedia 2023 Filtered | [pleisto/wikipedia-cn-20230720-filtered](https://huggingface.co/datasets/pleisto/wikipedia-cn-20230720-filtered) | 230,000 examples | llm-pretraining, continued-pretraining, rag | 2026-07-09 | active | Strongly recommended for Chinese LLM pretraining |
| Large Chinese Web Corpus 2024 (Filtered) | - | 数百GB级别 | llm-pretraining, domain-adaptation | 2026-07-09 | active | Recent large-scale Chinese web data (community filtered versions available on HF |

## 📝 Instruction Tuning / SFT

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| BAAI Infinity-Instruct (7M Core) | [BAAI/Infinity-Instruct](https://huggingface.co/datasets/BAAI/Infinity-Instruct) | 7,400,000 examples | sft, llm-finetuning, reasoning-llm | 2026-07-09 | active | Highly recommended: High-quality from BAAI, strong performance on MT-Bench and A |
| BELLE 3.5M Chinese Instruction Data | [BelleGroup/train_3.5M_CN](https://huggingface.co/datasets/BelleGroup/train_3.5M_CN) | 3,500,000 examples | sft, llm-finetuning | 2026-07-09 | active | Classic large-scale Chinese SFT dataset |
| Magpie Chinese Instruction Dataset (2025) | - | 大规模高质量指令数据 | sft, llm-finetuning | 2026-07-09 | active | Recent high-quality synthetic Chinese instruction data |
| Qwen Instruct 2025 (High-Quality Chinese) | [Qwen/Qwen-Instruct-2025-CN](https://huggingface.co/datasets/Qwen/Qwen-Instruct-2025-CN) | 2,000,000 examples | sft, reasoning-llm, agent | 2026-07-09 | active | 2025年Qwen团队发布的高质量中文指令数据 |
| WizardLM Evol-Instruct Chinese | [WizardLM/WizardLM_evol_instruct_V2_196k](https://huggingface.co/datasets/WizardLM/WizardLM_evol_instruct_V2_196k) | 196,000 examples | sft, reasoning-llm | 2026-07-09 | active | Good for improving reasoning ability |

## ❤️ Preference & Alignment (RLHF / DPO)

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| COIG-P: High-Quality Large-Scale Chinese Preference Dataset | [m-a-p/COIG-P](https://huggingface.co/datasets/m-a-p/COIG-P) | 1,006,000 examples | rlhf, dpo, alignment | 2026-07-09 | active | Top recommendation: Large-scale, high-quality Chinese preference data from 2025 |
| Chinese Preference Dataset 2025 (High-Quality) | - | 大规模偏好数据 | rlhf, dpo, alignment | 2026-07-09 | active | 2025最新高质量中文偏好数据，推荐用于对齐训练 |
| DPO Chinese Preference 2026 | [OpenChineseLLM/DPO-Chinese-2026](https://huggingface.co/datasets/OpenChineseLLM/DPO-Chinese-2026) | 150,000 examples | dpo, alignment | 2026-07-09 | active | 2026年最新DPO专用中文偏好数据 |
| UltraFeedback Chinese Preference Data | [HuggingFaceH4/ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized) | 60,000 examples | rlhf, dpo, alignment | 2026-07-09 | active | High quality preference data for alignment |

## 📏 Long-Context Data

| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |
|-------|---------------|------|------------------|---------------|--------|---------|
| InfiniteBench Chinese | - | 超长上下文数据 | long-context-llm | 2026-07-09 | active | 适合测试超长上下文能力 |
| Long-Context SFT Chinese 2026 | [ChineseLLM/Long-SFT-2026](https://huggingface.co/datasets/ChineseLLM/Long-SFT-2026) | 500,000 examples | long-context-llm, rag-long-context | 2026-07-09 | active | 2026年长上下文SFT专用高质量数据 |
| LongBench Chinese 2025 | - | 多任务长上下文数据 | long-context-llm, rag-long-context | 2026-07-09 | active | 2025更新版中文长上下文 benchmark 和训练数据 |
| THUDM LongBench (Bilingual Long-Context Benchmark) | [THUDM/LongBench](https://huggingface.co/datasets/THUDM/LongBench) | 4,750 examples | long-context-llm, evaluation, rag-long-context | 2026-07-09 | active | Highly recommended benchmark: Bilingual, rigorous, widely used for long-context  |

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
| CAIL2018 Chinese Legal Judgment Prediction | [china-ai-law-challenge/cail2018](https://huggingface.co/datasets/china-ai-law-challenge/cail2018) | 2,680,000 examples | legal-llm, legal-judgment-prediction, rag-legal | 2026-07-10 | active | 经典大规模中文法律判决预测数据集，CAIL 系列奠基之作 |
| CAIL2019-SCM Similar Case Matching | - | 8,964 examples | legal-llm, rag-legal, legal-case-retrieval | 2026-07-10 | active | CAIL2019 相似案例匹配任务，法律案例检索经典数据集 |
| CCKS2017 Chinese Electronic Medical Record NER | - | 800 examples | medical-ner, domain-ner | 2026-07-09 | active | Early but classic Chinese medical NER dataset |
| CJRC Chinese Legal Reading Comprehension | - | 50,000 examples | legal-llm, rag-legal | 2026-07-09 | active | Classic Chinese legal domain dataset |
| Chinese Financial Domain Dataset 2025 | [FinancialAI/Finance-Chinese-2025](https://huggingface.co/datasets/FinancialAI/Finance-Chinese-2025) | 300,000 examples | finance-llm, rag-finance | 2026-07-09 | active | 2025年高质量中文金融领域数据集 |
| DISC-Law-SFT Chinese Legal Instruction Dataset | [ShengbinYue/DISC-Law-SFT](https://huggingface.co/datasets/ShengbinYue/DISC-Law-SFT) | Large-scale legal SFT (Pair + Triplet QA released) | legal-llm, legal-sft, rag-legal | 2026-07-10 | active | 复旦DISC高质量中文法律指令微调数据集，适合Legal LLM SFT |
| FinCUGE Chinese Financial NLP Benchmark / Instruction | [Maciel/FinCUGE-Instruction](https://huggingface.co/datasets/Maciel/FinCUGE-Instruction) | 138,304 examples | finance-llm, rag-finance, financial-nlp-evaluation | 2026-07-10 | active | 中文金融NLP经典基准FinCUGE的指令版本，覆盖摘要/问答/情感/关系/事件抽取等 |
| FinRpt Equity Research Report Generation Dataset | [jinsong8/FinRpt](https://huggingface.co/datasets/jinsong8/FinRpt) | 6,825 examples | finance-llm, rag-finance, financial-agent, research-report | 2026-07-10 | active | 高质量中文/双语股票研报生成数据集，覆盖A股CSI800，适合金融Agent与研报分析 |
| Finance-Instruct-500k (with Chinese coverage) | [oieieio/Finance-Instruct-500k](https://huggingface.co/datasets/oieieio/Finance-Instruct-500k) | 500,000 examples | finance-llm, rag-finance | 2026-07-09 | active | Good financial instruction data with Chinese support |
| Gitee Chinese Code Corpus | [nyuuzyou/gitee-code](https://huggingface.co/datasets/nyuuzyou/gitee-code) | 536GB (3M+ repos, 819M+ files) | code-llm, chinese-code-llm, code-pretraining | 2026-07-10 | active | 高质量中文代码语料（Gitee源），含大量中文注释与文档，适合中文Code LLM预训练 |
| JEC-QA Chinese Judicial Examination QA | [hails/agieval-jec-qa-ca](https://huggingface.co/datasets/hails/agieval-jec-qa-ca) | 26,365 examples | legal-llm, rag-legal, legal-reasoning | 2026-07-10 | active | 中国国家司法考试真题QA数据集，法律领域经典benchmark |
| LeCaRD Chinese Legal Case Retrieval Dataset | [sentence-transformers/lecard-v2](https://huggingface.co/datasets/sentence-transformers/lecard-v2) | 43,000 examples | legal-llm, rag-legal, legal-case-retrieval | 2026-07-10 | active | 中文法律案例检索数据集，适合类案检索与RAG |
| Ling-Coder-SFT Chinese+English Code Instruction Dataset | [inclusionAI/Ling-Coder-SFT](https://huggingface.co/datasets/inclusionAI/Ling-Coder-SFT) | 5,000,000 examples | code-llm, chinese-code-llm, code-sft | 2026-07-10 | active | inclusionAI 开源的大规模中英双语代码SFT数据，覆盖多语言与复杂代码任务 |
| cMedQA Chinese Medical QA | - | 200,000 examples | medical-llm, rag-medical | 2026-07-09 | active | Widely used Chinese medical QA dataset |
| shibing624 Chinese Medical Dataset | [shibing624/medical](https://huggingface.co/datasets/shibing624/medical) | Chinese medical SFT/RLHF data | medical-llm, rag-medical | 2026-07-09 | active | Ready-to-use Chinese medical dataset for SFT and RLHF |
| tw-legal-qa-3M (Taiwan Legal QA) | [lianghsun/tw-legal-qa-3M](https://huggingface.co/datasets/lianghsun/tw-legal-qa-3M) | 5,393 examples | legal-llm, rag-legal | 2026-07-09 | active | Good Traditional Chinese legal QA dataset |

---

## Notes

- This table is generated from `data/**/*.json` files.
- To add a new dataset, add a JSON entry in the appropriate folder and the table will update automatically.
- For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

> **Last updated**: 2026-07-10