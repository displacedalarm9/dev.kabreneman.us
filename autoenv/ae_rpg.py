# AUTOENV — AE-RPG (AUTOENV Report Generator)
# TSN:          TSN-20260404-AUTOENV
# AUID:         AUID-AE-RPG-00001
# Subsystem:    AUTOENV
# CreatedBy:    Kyle Breneman / @copilot
# CreatedOn:    2026-04-04
# Governance:   docs/G-00003_autoenv-overview.md
# Standard:     UNISYS metadata standard.md (X-00002_)
#
# AE-RPG is a cross-system pawn daemon that reads synced DOCSYS datasets,
# analyzes/aggregates data to surface patterns, and produces fixed-format
# R-Class reports with static layout and dynamic header/footer.
#
# AE-RPG is NOT a Report, Form, Procedure, or Workflow. It is a programmatic
# component that produces R-Class report artifacts.
#
# Immutable identity fields (TSN, AUID, UDIS, CreatedBy, CreatedOn, Class)
# are treated as read-only per X-00002_, Section 5.

from __future__ import annotations

import json
import logging
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Logging — UTC timestamps
# ---------------------------------------------------------------------------

_handler = logging.StreamHandler()
_handler.setFormatter(logging.Formatter(
    fmt="%(asctime)s [AE-RPG] %(levelname)s — %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
))
_handler.formatter.converter = time.gmtime  # type: ignore[attr-defined]

logging.basicConfig(
    format="%(asctime)s [AE-RPG] %(levelname)s — %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    level=logging.INFO,
    handlers=[_handler],
)
log = logging.getLogger("ae_rpg")

# ---------------------------------------------------------------------------
# Immutable identity fields (read-only; never generated here)
# ---------------------------------------------------------------------------

IMMUTABLE_FIELDS = frozenset(
    {"tsn", "auid", "udis", "created_by", "created_on", "class_"}
)

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class AERPGInput:
    """Validated input contract for a single AE-RPG run.

    All fields are required.  AE-RPG will reject any input that is missing
    a required field or carries an attempt to override an immutable field.
    """

    tsn: str                    # Inherited TSN from the originating event
    data_sources: list[str]     # Paths to structured input files / datasets
    report_type: str            # Report type identifier (maps to a template)
    parameters: dict[str, Any]  # Analysis parameters (date range, filters …)
    operator: str               # Operator ID passed through to output metadata
    template_id: str            # Template ID for the fixed-format output layout

    def validate(self) -> None:
        """Raise ValueError loudly if any required field is missing or empty."""
        missing = []
        for attr in ("tsn", "data_sources", "report_type",
                     "parameters", "operator", "template_id"):
            val = getattr(self, attr)
            if val is None or val == "" or val == [] or val == {}:
                missing.append(attr)
        if missing:
            raise ValueError(
                f"AE-RPG input validation failed — missing required fields: "
                f"{missing}.  Execution halted."
            )
        if not self.tsn.startswith("TSN-"):
            raise ValueError(
                f"AE-RPG input validation failed — TSN format invalid: "
                f"'{self.tsn}'.  Expected format: TSN-YYYYMMDD-LABEL."
            )


@dataclass
class AERPGOutput:
    """Metadata envelope for a generated AE-RPG report artifact."""

    tsn: str                # Inherited (never regenerated)
    auid: str               # New AUID — must be supplied by caller (DOCSYS identity layer)
    udis: str               # New UDIS — must be supplied by caller at instantiation
    class_: str = "R"       # Always R-Class; immutable after assignment
    created_by: str = "AE-RPG"
    created_on: str = field(
        default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    )
    report_type: str = ""
    operator: str = ""
    template_id: str = ""
    body: str = ""          # Rendered report content


@dataclass
class PMFEntry:
    """Provenance Metadata File record for a generated report."""

    tsn: str
    auid: str
    udis: str
    lifecycle: str
    created_by: str
    created_on: str
    related_artifacts: list[str]
    provenance_notes: str


# ---------------------------------------------------------------------------
# Template renderer
# ---------------------------------------------------------------------------


class ReportTemplate:
    """Minimal fixed-format report template.

    Layout is static (defined here).  Dynamic header/footer is applied once,
    at instantiation time only — it is never re-applied to an existing report.
    """

    HEADER = (
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "UNISYS — AE-RPG GENERATED REPORT\n"
        "TSN:        {tsn}\n"
        "AUID:       {auid}\n"
        "UDIS:       {udis}\n"
        "Class:      R\n"
        "CreatedBy:  {created_by}\n"
        "CreatedOn:  {created_on}\n"
        "Operator:   {operator}\n"
        "Template:   {template_id}\n"
        "ReportType: {report_type}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    )

    FOOTER = (
        "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "END OF REPORT  |  {auid}  |  {created_on}\n"
        "Unified System Architecture™  UNISYS™  ©2026 Kyle Breneman\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    )

    @classmethod
    def render(cls, output: AERPGOutput) -> str:
        """Apply dynamic header/footer to the static report body (once only)."""
        ctx = {
            "tsn": output.tsn,
            "auid": output.auid,
            "udis": output.udis,
            "created_by": output.created_by,
            "created_on": output.created_on,
            "operator": output.operator,
            "template_id": output.template_id,
            "report_type": output.report_type,
        }
        return cls.HEADER.format(**ctx) + output.body + cls.FOOTER.format(**ctx)


# ---------------------------------------------------------------------------
# Core AE-RPG engine
# ---------------------------------------------------------------------------


class AERPG:
    """AUTOENV Report Generator — pawn daemon.

    Accepts a validated AERPGInput, reads and analyzes data sources, and
    produces an AERPGOutput (R-Class report) plus a PMF.

    Identity fields (AUID, UDIS) must be injected by the caller, which is
    responsible for requesting them from the DOCSYS identity layer.  AE-RPG
    never self-generates identity.
    """

    def __init__(self, auid: str, udis: str) -> None:
        """
        Parameters
        ----------
        auid:
            New AUID allocated by the DOCSYS identity layer for this report.
        udis:
            New UDIS allocated by the DOCSYS identity layer at instantiation.
        """
        self._validate_identity(auid, "auid")
        self._validate_identity(udis, "udis")
        self._auid = auid
        self._udis = udis

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def run(self, inp: AERPGInput) -> tuple[str, str]:
        """Execute a full AE-RPG report generation run.

        Returns
        -------
        (report_text, pmf_json)
            report_text — fully rendered R-Class report (header + body + footer)
            pmf_json    — serialised PMF (Provenance Metadata File) as JSON string
        """
        log.info("AE-RPG run started  TSN=%s  template=%s", inp.tsn, inp.template_id)

        # 1. Validate input
        inp.validate()
        log.info("Input validation passed.")

        # 2. Load and validate data sources
        records = self._load_data_sources(inp.data_sources)
        log.info("Loaded %d record(s) from %d source(s).",
                 len(records), len(inp.data_sources))

        # 3. Analyze data
        body = self._analyse(records, inp.parameters, inp.report_type)
        log.info("Analysis complete.")

        # 4. Build output envelope
        output = AERPGOutput(
            tsn=inp.tsn,
            auid=self._auid,
            udis=self._udis,
            report_type=inp.report_type,
            operator=inp.operator,
            template_id=inp.template_id,
            body=body,
        )

        # 5. Render report (dynamic header/footer applied here — once only)
        report_text = ReportTemplate.render(output)

        # 6. Build PMF
        pmf = PMFEntry(
            tsn=inp.tsn,
            auid=self._auid,
            udis=self._udis,
            lifecycle="Draft",
            created_by="AE-RPG",
            created_on=output.created_on,
            related_artifacts=list(inp.data_sources),
            provenance_notes=(
                f"Generated by AE-RPG daemon.  "
                f"Template: {inp.template_id}.  "
                f"ReportType: {inp.report_type}.  "
                f"Operator: {inp.operator}."
            ),
        )
        pmf_json = json.dumps(pmf.__dict__, indent=2)

        log.info(
            "AE-RPG run complete.  AUID=%s  UDIS=%s  output_size=%d chars",
            self._auid, self._udis, len(report_text),
        )
        return report_text, pmf_json

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _validate_identity(value: str, field_name: str) -> None:
        """Fail loudly if a required identity field is absent or empty."""
        if not value or not value.strip():
            raise ValueError(
                f"AE-RPG identity validation failed — '{field_name}' must be "
                f"provided by the DOCSYS identity layer.  "
                f"AE-RPG does not self-assign identity fields."
            )

    @staticmethod
    def _load_data_sources(sources: list[str]) -> list[dict[str, Any]]:
        """Load structured records from a list of file paths.

        Supported formats: JSON (.json), JSON-Lines (.jsonl).
        Each source must be a valid, readable file.  Missing or unreadable
        sources cause an immediate, logged failure.
        """
        records: list[dict[str, Any]] = []
        for src in sources:
            path = Path(src)
            if not path.exists():
                msg = f"AE-RPG data source not found: '{src}'.  Execution halted."
                log.error(msg)
                raise FileNotFoundError(msg)
            if not path.is_file():
                msg = f"AE-RPG data source is not a file: '{src}'.  Execution halted."
                log.error(msg)
                raise ValueError(msg)
            suffix = path.suffix.lower()
            try:
                raw = path.read_text(encoding="utf-8")
                if suffix == ".json":
                    data = json.loads(raw)
                    if isinstance(data, list):
                        records.extend(data)
                    else:
                        records.append(data)
                elif suffix == ".jsonl":
                    for line in raw.splitlines():
                        line = line.strip()
                        if line:
                            records.append(json.loads(line))
                else:
                    msg = (
                        f"AE-RPG unsupported data source format '{suffix}' in "
                        f"'{src}'.  Supported: .json, .jsonl.  Execution halted."
                    )
                    log.error(msg)
                    raise ValueError(msg)
            except (json.JSONDecodeError, OSError) as exc:
                msg = f"AE-RPG failed to read '{src}': {exc}.  Execution halted."
                log.error(msg)
                raise RuntimeError(msg) from exc
            log.info("Loaded source: %s  (%d records total so far)", src, len(records))
        return records

    @staticmethod
    def _analyse(
        records: list[dict[str, Any]],
        parameters: dict[str, Any],
        report_type: str,
    ) -> str:
        """Aggregate and analyze records according to parameters.

        Returns the static body section of the report (plain text).
        Layout is deterministic — same inputs always produce the same body.
        """
        lines: list[str] = []
        lines.append(f"Report Type : {report_type}")
        lines.append(f"Parameters  : {json.dumps(parameters, sort_keys=True)}")
        lines.append(f"Record Count: {len(records)}")
        lines.append("")

        if not records:
            lines.append("(no records to analyze)")
            return "\n".join(lines)

        # --- numeric field aggregation ---
        numeric_fields: dict[str, list[float]] = {}
        for rec in records:
            if not isinstance(rec, dict):
                continue
            for k, v in rec.items():
                if isinstance(v, (int, float)):
                    numeric_fields.setdefault(k, []).append(float(v))

        if numeric_fields:
            lines.append("Numeric Field Summary")
            lines.append("─" * 60)
            col_w = max(len(k) for k in numeric_fields) + 2
            lines.append(
                f"  {'Field'.ljust(col_w)}  {'Count':>8}  {'Sum':>14}  "
                f"{'Min':>14}  {'Max':>14}  {'Avg':>14}"
            )
            lines.append("  " + "─" * (col_w + 74))
            for fname, vals in sorted(numeric_fields.items()):
                count = len(vals)
                total = sum(vals)
                mn = min(vals)
                mx = max(vals)
                avg = total / count if count else 0.0
                lines.append(
                    f"  {fname.ljust(col_w)}  {count:>8}  {total:>14.2f}  "
                    f"{mn:>14.2f}  {mx:>14.2f}  {avg:>14.2f}"
                )
            lines.append("")

        # --- date-range filter note ---
        date_from = parameters.get("date_from")
        date_to = parameters.get("date_to")
        if date_from or date_to:
            lines.append(
                f"Date Range Filter: {date_from or '(none)'} — {date_to or '(none)'}"
            )
            lines.append("")

        # --- pattern detection: flag fields whose max > threshold ---
        threshold = parameters.get("threshold")
        if threshold is not None:
            lines.append(f"Threshold Analysis (threshold={threshold})")
            lines.append("─" * 60)
            flagged = False
            for fname, vals in sorted(numeric_fields.items()):
                if max(vals) > threshold:
                    lines.append(f"  FLAGGED: '{fname}' max={max(vals):.2f} > {threshold}")
                    flagged = True
            if not flagged:
                lines.append("  No fields exceeded the threshold.")
            lines.append("")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _cli() -> None:
    """Minimal CLI: ae_rpg.py <input_json> <auid> <udis> [output_dir]

    input_json — path to a JSON file matching the AERPGInput schema
    auid       — AUID allocated by the DOCSYS identity layer for this report
    udis       — UDIS allocated by the DOCSYS identity layer at instantiation
    output_dir — (optional) directory to write report.txt and pmf.json;
                 defaults to the current directory
    """
    if len(sys.argv) < 4:
        print(
            "Usage: ae_rpg.py <input_json> <auid> <udis> [output_dir]",
            file=sys.stderr,
        )
        sys.exit(1)

    input_path = Path(sys.argv[1])
    auid = sys.argv[2]
    udis = sys.argv[3]
    output_dir = Path(sys.argv[4]) if len(sys.argv) > 4 else Path(".")

    if not input_path.exists():
        log.error("Input file not found: %s", input_path)
        sys.exit(1)

    try:
        raw = json.loads(input_path.read_text(encoding="utf-8"))
        inp = AERPGInput(
            tsn=raw["tsn"],
            data_sources=raw["data_sources"],
            report_type=raw["report_type"],
            parameters=raw.get("parameters", {}),
            operator=raw["operator"],
            template_id=raw["template_id"],
        )
    except (KeyError, json.JSONDecodeError) as exc:
        log.error("Failed to parse input file '%s': %s", input_path, exc)
        sys.exit(1)

    engine = AERPG(auid=auid, udis=udis)
    report_text, pmf_json = engine.run(inp)

    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "report.txt"
    pmf_path = output_dir / "pmf.json"

    report_path.write_text(report_text, encoding="utf-8")
    pmf_path.write_text(pmf_json, encoding="utf-8")

    log.info("Report written to: %s", report_path)
    log.info("PMF written to:    %s", pmf_path)


if __name__ == "__main__":
    _cli()
