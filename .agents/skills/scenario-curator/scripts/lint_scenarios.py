#!/usr/bin/env python3
"""
Scenario Linter & Integrity Checker for MkDocs Material
Validates relative Markdown links, PyMdown snippets, frontmatter, and headings.
"""

import os
import sys
import re
import argparse
from pathlib import Path
import yaml

def extract_frontmatter(content):
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1])
                return fm, parts[2]
            except Exception as e:
                return {"_error": str(e)}, parts[2]
    return {}, content

def check_frontmatter(fm, filepath):
    errors = []
    warnings = []
    if not fm:
        warnings.append(f"Frontmatter is missing in {filepath}")
        return errors, warnings
    if "_error" in fm:
        errors.append(f"YAML Syntax Error in Frontmatter: {fm['_error']}")
        return errors, warnings

    # Check required fields
    if "title" not in fm:
        warnings.append("Frontmatter is missing 'title'")
    if "description" not in fm:
        warnings.append("Frontmatter is missing 'description'")
    if "target_personas" not in fm:
        warnings.append("Frontmatter is missing 'target_personas'")
    else:
        personas = fm.get("target_personas", {})
        for p in ["persona-m365", "persona-local", "persona-cloud"]:
            if p not in personas:
                warnings.append(f"target_personas is missing key '{p}'")

    return errors, warnings

def check_markdown_links(content, filepath, root_dir):
    errors = []
    warnings = []
    # Match markdown links: [text](link)
    # Ignore external links (http://, https://, mailto:)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    file_dir = filepath.parent

    for match in link_pattern.finditer(content):
        link_text = match.group(1)
        raw_url = match.group(2).strip()

        # Skip external or anchor-only links
        if raw_url.startswith(("http://", "https://", "mailto:", "ftp://")):
            continue
        if raw_url.startswith("#"):
            continue

        # Strip anchor if present
        target_path_str = raw_url.split("#")[0]
        anchor = raw_url.split("#")[1] if "#" in raw_url else None

        if not target_path_str:
            continue

        target_file = (file_dir / target_path_str).resolve()

        # Check if target exists
        if not target_file.exists():
            errors.append(f"Broken relative link: '{raw_url}' in {filepath.name} (Resolved: {target_file})")
        else:
            # Check extension for Markdown files
            if target_file.is_file() and target_file.suffix == '.md' and not target_path_str.endswith('.md'):
                warnings.append(f"Markdown link missing '.md' extension: '{raw_url}' in {filepath.name}")

    return errors, warnings

def check_snippets(content, filepath, root_dir):
    errors = []
    warnings = []
    # Snippet syntax: --8<-- "path" or --8<-- "path:start:end"
    snippet_pattern = re.compile(r'--8<--\s+["\']([^"\']+)["\']')

    for match in snippet_pattern.finditer(content):
        snippet_ref = match.group(1).strip()
        parts = snippet_ref.split(":")
        rel_path = parts[0]
        start_line = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None
        end_line = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else None

        # Snippets in pymdownx are resolved relative to docs_dir / repo root
        target_file = (root_dir / rel_path).resolve()
        if not target_file.exists():
            # Try relative to file dir
            target_file_alt = (filepath.parent / rel_path).resolve()
            if not target_file_alt.exists():
                errors.append(f"Snippet target not found: '{snippet_ref}' in {filepath.name}")
                continue
            else:
                target_file = target_file_alt

        if start_line is not None or end_line is not None:
            try:
                with open(target_file, "r", encoding="utf-8") as tf:
                    total_lines = len(tf.readlines())
                if start_line and start_line > total_lines:
                    warnings.append(f"Snippet start_line ({start_line}) exceeds file line count ({total_lines}) in '{snippet_ref}'")
                if end_line and end_line > total_lines:
                    warnings.append(f"Snippet end_line ({end_line}) exceeds file line count ({total_lines}) in '{snippet_ref}'")
            except Exception as e:
                warnings.append(f"Failed to check snippet bounds for '{snippet_ref}': {e}")

    return errors, warnings

def lint_file(filepath, root_dir):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return [f"Could not read file {filepath}: {e}"], []

    fm, body = extract_frontmatter(content)
    fm_errors, fm_warnings = check_frontmatter(fm, filepath)
    link_errors, link_warnings = check_markdown_links(content, filepath, root_dir)
    snip_errors, snip_warnings = check_snippets(content, filepath, root_dir)

    all_errors = fm_errors + link_errors + snip_errors
    all_warnings = fm_warnings + link_warnings + snip_warnings

    return all_errors, all_warnings

def main():
    parser = argparse.ArgumentParser(description="Lint scenario files for MkDocs Material")
    parser.add_argument("--file", "-f", help="Specific scenario file to lint")
    parser.add_argument("--all", "-a", action="store_true", help="Lint all scenario files in scenarios/")
    parser.add_argument("--root", "-r", default=".", help="Repository root path")

    args = parser.parse_args()
    root_dir = Path(args.root).resolve()

    target_files = []
    if args.file:
        p = Path(args.file)
        if not p.is_absolute():
            p = (root_dir / p).resolve()
        if not p.exists():
            print(f"Error: File {p} not found.")
            sys.exit(1)
        target_files.append(p)
    elif args.all or not args.file:
        scenarios_dir = root_dir / "scenarios"
        if scenarios_dir.exists():
            target_files = sorted(list(scenarios_dir.glob("*.md")))
        else:
            print(f"Warning: scenarios directory not found at {scenarios_dir}")

    if not target_files:
        print("No scenario files found to lint.")
        sys.exit(0)

    total_errors = 0
    total_warnings = 0

    print("==================================================")
    print(" 📋 Scenario Documentation & Integrity Linter")
    print("==================================================")

    for tf in target_files:
        rel_path = tf.relative_to(root_dir) if tf.is_relative_to(root_dir) else tf
        errors, warnings = lint_file(tf, root_dir)
        total_errors += len(errors)
        total_warnings += len(warnings)

        status_symbol = "❌" if errors else ("⚠️" if warnings else "✅")
        print(f"\n{status_symbol} [{rel_path}]")

        if errors:
            print("  🔴 Errors:")
            for err in errors:
                print(f"     - {err}")
        if warnings:
            print("  🟡 Warnings:")
            for warn in warnings:
                print(f"     - {warn}")
        if not errors and not warnings:
            print("     All links, snippets, and frontmatter are valid!")

    print("\n--------------------------------------------------")
    print(f"Summary: {len(target_files)} file(s) checked | {total_errors} Error(s) | {total_warnings} Warning(s)")
    print("==================================================")

    if total_errors > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
