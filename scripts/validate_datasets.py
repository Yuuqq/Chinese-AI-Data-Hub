#!/usr/bin/env python3
"""
CLUEDatasetSearch Data Hub - 简单验证脚本
用法: python scripts/validate_datasets.py
"""

import json
import os
import sys
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

REQUIRED_FIELDS = ["id", "title", "description", "category"]

def validate_json_file(filepath):
    print(f"验证: {filepath.name}")
    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print("  ❌ 根元素必须是 list")
            return False
        
        errors = 0
        for i, item in enumerate(data):
            for field in REQUIRED_FIELDS:
                if field not in item:
                    print(f"  ❌ 第 {i+1} 条缺少必填字段: {field}")
                    errors += 1
        
        if errors == 0:
            print(f"  ✅ 通过 ({len(data)} 条数据)")
        return errors == 0
    except Exception as e:
        print(f"  ❌ 解析失败: {e}")
        return False

def main():
    print("=== CLUEDatasetSearch Data Hub 验证 ===\n")
    json_files = list(DATA_DIR.rglob("*.json"))
    
    if not json_files:
        print("data/ 目录下没有 JSON 文件")
        return
    
    all_ok = True
    for f in json_files:
        if not validate_json_file(f):
            all_ok = False
        print()
    
    if all_ok:
        print("🎉 所有文件验证通过！")
    else:
        print("⚠️  存在问题，请修复后重试。")
        sys.exit(1)

if __name__ == "__main__":
    main()