#!/usr/bin/env python3
"""
Auto-generate DATASETS.md from structured JSON files in data/
Run this script from the repository root.
"""

import json
from pathlib import Path
from datetime import datetime
import sys

DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_FILE = Path(__file__).parent.parent / "DATASETS.md"

CATEGORY_ORDER = [
    "pretraining",
    "instruction",
    "preference",
    "long_context",
    "evaluation",
    "tasks",
    "domain"
]

CATEGORY_TITLES = {
    "pretraining": "🔥 Pretraining & Foundation Corpora",
    "instruction": "📝 Instruction Tuning / SFT",
    "preference": "❤️ Preference & Alignment (RLHF / DPO)",
    "long_context": "📏 Long-Context Data",
    "evaluation": "📊 Evaluation & Benchmarks",
    "tasks": "🧩 Traditional NLP Tasks",
    "domain": "🏥 Domain-Specific"
}

def load_json_files():
    """Load all JSON files from data/ subdirectories."""
    datasets = []
    for category_dir in DATA_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith("."):
            continue
        category = category_dir.name
        for json_file in category_dir.glob("*.json"):
            try:
                with open(json_file, encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        item["_category"] = category
                        item["_source_file"] = str(json_file.relative_to(DATA_DIR))
                        datasets.append(item)
            except (json.JSONDecodeError, OSError) as e:
                print(f"Error: Failed to load {json_file}: {e}")
                sys.exit(1)
    return datasets

def format_size(item):
    size = item.get("size", "")
    num = item.get("num_examples")
    if num:
        return f"{num:,} examples"
    return size or "-"

def format_recommended_for(item):
    rec = item.get("recommended_for", [])
    if isinstance(rec, list):
        return ", ".join(rec)
    return rec or "-"

def generate_table(datasets, category):
    """Generate Markdown table for a category."""
    filtered = [d for d in datasets if d.get("_category") == category]
    if not filtered:
        return ""

    lines = [
        f"## {CATEGORY_TITLES.get(category, category.title())}",
        "",
        "| Title | HF Dataset ID | Size | Recommended For | Last Verified | Status | Remarks |",
        "|-------|---------------|------|------------------|---------------|--------|---------|"
    ]

    for item in sorted(filtered, key=lambda x: x.get("title", "")):
        title = item.get("title", "Untitled")
        hf_id = item.get("hf_dataset_id", "")
        if hf_id:
            hf_link = f"[{hf_id}](https://huggingface.co/datasets/{hf_id})"
        else:
            hf_link = "-"

        size = format_size(item)
        rec_for = format_recommended_for(item)
        last_verified = item.get("last_verified", "-")
        status = item.get("status", "active")
        remarks = item.get("remarks", "")[:80]  # truncate long remarks

        lines.append(
            f"| {title} | {hf_link} | {size} | {rec_for} | {last_verified} | {status} | {remarks} |"
        )

    lines.append("")
    return "\n".join(lines)

def generate_datasets_md():
    datasets = load_json_files()
    if not datasets:
        print("No datasets found.")
        return

    content = [
        "# CLUEDatasetSearch - Datasets Overview",
        "",
        "> **Auto-generated overview** of all datasets. Use `Ctrl+F` to search.",
        "",
        "This file is **automatically updated** via GitHub Actions when datasets change.",
        "",
        "---",
        "",
        "## 📍a Quick Reference",
        "",
        "- **HF Dataset ID** links are preferred for downloading.",
        "- See individual JSON files in `data/` for full metadata.",
        "- Last generated: " + datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
        "",
        "---",
        ""
    ]

    for category in CATEGORY_ORDER:
        table = generate_table(datasets, category)
        if table:
            content.append(table)

    # Add footer
    content.extend([
        "---",
        "",
        "## Notes",
        "",
        "- This table is generated from `data/**/*.json` files.",
        "- To add a new dataset, add a JSON entry in the appropriate folder and the table will update automatically.",
        "- For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
        f"> **Last updated**: {datetime.now().strftime('%Y-%m-%d')}"
    ])

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

    print(f"Generated {OUTPUT_FILE} with {len(datasets)} datasets.")

if __name__ == "__main__":
    generate_datasets_md()