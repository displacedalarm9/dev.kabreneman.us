# UNISYS_IMPORT_RECORD
# AUID: MIG-00019
# TSN: TSN-20260404-WORKCAP
# OriginalLocation: displacedalarm9/kabreneman.us/scripts/workcap_analyzer.py
# MigratedOn: 2026-04-04

import os
import re
import yaml
from datetime import datetime
from pathlib import Path
import shutil
import time


class WorkCapAnalyzer:
    """
    WORKCAP Workspace Analyzer — UNISYS/ACCTSYS
    Analyzes markdown files within the WORKCAP module for structural integrity,
    metadata compliance, cross-reference validity, and financial metric thresholds.
    """

    # Default UNISYS/WORKCAP base path within the repository
    DEFAULT_BASE_PATH = Path(__file__).resolve().parent.parent / "financials"

    def __init__(self, base_path=None):
        self.base_path = Path(base_path) if base_path else self.DEFAULT_BASE_PATH
        self.standard_values = {
            "buffer_minimum": 110,
        }

    def archive_existing_reports(self, report_path):
        """Archive an existing report file before overwriting."""
        report_path = Path(report_path)
        if not report_path.exists():
            return

        archive_folder = report_path.parent / "archive"
        archive_folder.mkdir(parents=True, exist_ok=True)

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        archive_name = f"{report_path.stem}_{timestamp}{report_path.suffix}"
        archive_path = archive_folder / archive_name

        shutil.move(str(report_path), str(archive_path))

    def validate_file_structure(self, file_path):
        """Validate file naming conventions for review files."""
        filename = Path(file_path).name
        if "reviews" in str(file_path):
            pattern = r"\d{4}-\d{2}-\d{2}_[a-z]+\.md"
            return bool(re.match(pattern, filename))
        return True

    def parse_yaml_header(self, content):
        """Parse YAML front-matter from a markdown file.

        Handles files where an HTML comment block (UNISYS_IMPORT_RECORD)
        precedes the YAML front-matter delimiter.
        """
        # Skip leading HTML comment block if present
        stripped = content.lstrip()
        if stripped.startswith("<!--"):
            end_comment = stripped.find("-->")
            if end_comment != -1:
                stripped = stripped[end_comment + 3:].lstrip()

        if stripped.startswith("---"):
            try:
                end = stripped.index("---", 3)
                header_text = stripped[3:end]
                return yaml.safe_load(header_text)
            except Exception:
                return None
        return None

    def check_file_status(self, header):
        """Validate that file_status is a recognised value."""
        valid_statuses = {"report", "template", "protocol", "active", "core"}
        if header and "file_status" in header:
            return header["file_status"] in valid_statuses
        return False

    def check_import_record(self, content):
        """Check for presence of a UNISYS_IMPORT_RECORD block."""
        return "UNISYS_IMPORT_RECORD" in content

    def extract_metrics(self, content):
        """Extract key financial metrics from a review file's markdown tables."""
        metrics = {
            "buffer": None,
            "credit_usage": None,
            "debt_total": None,
        }

        buffer_pattern = r"\|\s*Buffer\s*\|\s*\$?([\d.]+)\s*\|"
        credit_pattern = r"\|\s*Credit Usage\s*\|\s*([\d.]+)%\s*\|"
        debt_pattern = r"\|\s*Debt Total\s*\|\s*\$?([\d.]+)\s*\|"

        if match := re.search(buffer_pattern, content, re.IGNORECASE):
            metrics["buffer"] = float(match.group(1))
        if match := re.search(credit_pattern, content, re.IGNORECASE):
            metrics["credit_usage"] = float(match.group(1))
        if match := re.search(debt_pattern, content, re.IGNORECASE):
            metrics["debt_total"] = float(match.group(1))

        return metrics

    def validate_cross_references(self, content):
        """Return a list of [See: ...] references that cannot be resolved."""
        ref_pattern = r"\[See:\s+([^\]]+)\]"
        references = re.findall(ref_pattern, content)
        invalid_refs = []

        for ref in references:
            # Strip trailing description after whitespace beyond the path
            path_part = ref.strip().split()[0]
            # Resolve relative to repo root (one level above financials/)
            repo_root = self.base_path.parent
            ref_path = repo_root / path_part
            if not ref_path.exists():
                invalid_refs.append(ref)

        return invalid_refs

    def analyze_file(self, file_path):
        """Analyze a single markdown file and return a results dict."""
        file_path = Path(file_path)
        with open(file_path, "r", encoding="utf-8") as fh:
            content = fh.read()

        results = {
            "file": str(file_path),
            "structure_valid": self.validate_file_structure(file_path),
            "status_valid": False,
            "import_record_present": self.check_import_record(content),
            "metrics": None,
            "invalid_references": [],
            "warnings": [],
        }

        header = self.parse_yaml_header(content)
        if header:
            results["status_valid"] = self.check_file_status(header)

            if "last_updated" in header:
                try:
                    last_updated = datetime.strptime(
                        str(header["last_updated"]), "%Y-%m-%d"
                    )
                    if (datetime.now() - last_updated).days > 30:
                        results["warnings"].append(
                            "File not updated in over 30 days"
                        )
                except ValueError:
                    results["warnings"].append("Invalid last_updated date format")
        else:
            results["warnings"].append("No YAML front-matter found")

        if not results["import_record_present"]:
            results["warnings"].append("Missing UNISYS_IMPORT_RECORD block")

        # Metric extraction only applies to filled review files
        if "reviews" in str(file_path):
            results["metrics"] = self.extract_metrics(content)
            if (
                results["metrics"]["buffer"] is not None
                and results["metrics"]["buffer"]
                < self.standard_values["buffer_minimum"]
            ):
                results["warnings"].append(
                    f"Buffer below minimum: "
                    f"${results['metrics']['buffer']} "
                    f"< ${self.standard_values['buffer_minimum']}"
                )

        results["invalid_references"] = self.validate_cross_references(content)

        return results

    def analyze_workspace(self):
        """Analyze all markdown files in the WORKCAP base path."""
        all_results = []

        for root, _, files in os.walk(self.base_path):
            for filename in files:
                if filename.endswith(".md"):
                    file_path = Path(root) / filename
                    results = self.analyze_file(file_path)
                    all_results.append(results)

        return self.generate_report(all_results)

    def generate_report(self, results):
        """Generate a structured markdown analysis report."""
        current_date = datetime.now().strftime("%Y-%m-%d")
        report = f"""---
last_updated: {current_date}
version: 1.0.0
file_status: report
system: ACCTSYS
subsystem: WORKCAP
---

# WORKCAP Analysis Report

Generated: {current_date}

## Summary

| Metric | Count |
|--------|-------|
| Total files analyzed | {len(results)} |
| Files with warnings | {sum(1 for r in results if r["warnings"])} |
| Files with invalid references | {sum(1 for r in results if r["invalid_references"])} |
| Files missing IMPORT_RECORD | {sum(1 for r in results if not r["import_record_present"])} |

## File Structure Issues

"""
        structure_issues = [r for r in results if not r["structure_valid"]]
        if structure_issues:
            for issue in structure_issues:
                report += f"- Invalid structure: {issue['file']}\n"
        else:
            report += "No file structure issues found.\n"

        report += "\n## Invalid Cross-References\n\n"
        ref_issues = [r for r in results if r["invalid_references"]]
        if ref_issues:
            for issue in ref_issues:
                report += f"**File:** `{issue['file']}`\n"
                for ref in issue["invalid_references"]:
                    report += f"- Missing: `{ref}`\n"
                report += "\n"
        else:
            report += "No invalid cross-references found.\n"

        report += "\n## Metrics Analysis\n\n"
        metrics_files = [r for r in results if r.get("metrics")]
        if metrics_files:
            for m in metrics_files:
                if m["metrics"]["buffer"] is not None:
                    report += f"**File:** `{m['file']}`\n"
                    report += f"- Buffer: ${m['metrics']['buffer']}\n"
                    report += f"- Credit Usage: {m['metrics']['credit_usage']}%\n"
                    report += f"- Debt Total: ${m['metrics']['debt_total']}\n"
                    if m["warnings"]:
                        report += "- Warnings:\n"
                        for warning in m["warnings"]:
                            report += f"  - {warning}\n"
                    report += "\n"
        else:
            report += "No filled review files with metrics found.\n"

        report += "\n## All Warnings\n\n"
        warned = [r for r in results if r["warnings"]]
        if warned:
            for item in warned:
                report += f"**File:** `{item['file']}`\n"
                for w in item["warnings"]:
                    report += f"- {w}\n"
                report += "\n"
        else:
            report += "No warnings.\n"

        return report


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="WORKCAP Workspace Analyzer — UNISYS/ACCTSYS"
    )
    parser.add_argument(
        "--base-path",
        default=None,
        help="Path to the WORKCAP financials directory (default: repo financials/)",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory to write the analysis report (default: <base_path>/reports/analysis/)",
    )
    args = parser.parse_args()

    analyzer = WorkCapAnalyzer(base_path=args.base_path)
    report_content = analyzer.analyze_workspace()

    current_date = datetime.now().strftime("%Y-%m-%d")
    output_dir = (
        Path(args.output_dir)
        if args.output_dir
        else analyzer.base_path / "reports" / "analysis"
    )
    report_path = output_dir / f"{current_date}_workcap_analysis.md"

    analyzer.archive_existing_reports(report_path)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as fh:
        fh.write(report_content)

    print(f"Report written to: {report_path}")
