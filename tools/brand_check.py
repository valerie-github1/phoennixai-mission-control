#!/usr/bin/env python3
"""
PhoennixAI Brand Consistency Checker
Scans all HTML files and reports any brand violations.

Usage:
  python3 tools/brand_check.py            # full report
  python3 tools/brand_check.py --fix      # auto-fix what it can
  python3 tools/brand_check.py --json     # machine-readable output

Exit code: 0 = all clean, 1 = violations found
"""

import os, re, sys, json, argparse
from pathlib import Path
from dataclasses import dataclass, field, asdict

ROOT = Path(__file__).parent.parent

# ── Brand rules ────────────────────────────────────────────────────────────────

RULES = {
    "favicon": {
        "desc": "SVG favicon via /favicon.svg",
        "check": lambda c: 'href="/favicon.svg"' in c,
        "fix_op": "favicon",
    },
    "meta_charset": {
        "desc": "UTF-8 charset declaration",
        "check": lambda c: bool(re.search(r'<meta\s[^>]*charset=["\']?UTF-8', c, re.I)),
        "fix_op": "meta-charset",
    },
    "meta_viewport": {
        "desc": "Responsive viewport meta tag",
        "check": lambda c: bool(re.search(r'<meta\s[^>]*name=["\']viewport["\']', c, re.I)),
        "fix_op": "meta-viewport",
    },
    "no_data_uri_favicon": {
        "desc": "No data: URI favicon (browser-blocked)",
        "check": lambda c: "data:image/svg+xml;base64" not in c and "data:image/x-icon" not in c,
        "fix_op": "favicon",   # re-running favicon op strips data URIs
    },
    "google_fonts": {
        "desc": "Google Fonts (Bebas Neue + DM Sans) loaded",
        "check": lambda c: "fonts.googleapis.com" in c and "Bebas+Neue" in c,
        "fix_op": None,  # too page-specific to auto-fix
    },
    "brand_color_midnight": {
        "desc": "Brand midnight colour #060A18 referenced",
        "check": lambda c: "#060A18" in c or "060A18" in c.upper(),
        "fix_op": None,
    },
    "brand_color_phoenix": {
        "desc": "Brand electric cyan #00E5FF referenced",
        "check": lambda c: "#00E5FF" in c or "00E5FF" in c.upper(),
        "fix_op": None,
    },
    "no_inline_bgcolor": {
        "desc": "No legacy bgcolor attribute",
        "check": lambda c: not bool(re.search(r'\bbgcolor\s*=', c, re.I)),
        "fix_op": None,
    },
    "doctype": {
        "desc": "HTML5 doctype present",
        "check": lambda c: c.lstrip().lower().startswith("<!doctype html"),
        "fix_op": None,
    },
    "lang_attr": {
        "desc": "html[lang] attribute set",
        "check": lambda c: bool(re.search(r'<html[^>]+lang=', c, re.I)),
        "fix_op": None,
    },
    "title_tag": {
        "desc": "Page has a <title> tag",
        "check": lambda c: bool(re.search(r'<title>[^<]+</title>', c, re.I)),
        "fix_op": None,
    },
}

FIXABLE_OPS = {
    "favicon":       ["python3", "tools/patch.py", "--op", "favicon"],
    "meta-charset":  ["python3", "tools/patch.py", "--op", "meta-charset"],
    "meta-viewport": ["python3", "tools/patch.py", "--op", "meta-viewport"],
}

# ── Data structures ─────────────────────────────────────────────────────────────

@dataclass
class FileResult:
    name: str
    violations: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def clean(self) -> bool:
        return not self.violations


@dataclass
class Report:
    total: int = 0
    clean: int = 0
    files: list[FileResult] = field(default_factory=list)

    def summary(self) -> dict:
        return {
            "total": self.total,
            "clean": self.clean,
            "violations": self.total - self.clean,
            "pass_rate": f"{100 * self.clean // self.total}%" if self.total else "N/A",
        }


# ── Core logic ──────────────────────────────────────────────────────────────────

# Rules that are important for every page
REQUIRED_RULES = {"favicon", "meta_charset", "meta_viewport", "no_data_uri_favicon", "doctype", "title_tag"}

# Rules that only apply to full product pages (skip CV/JobDescription/InstagramPost etc.)
BRAND_ONLY_PAGES = re.compile(
    r'^(PhoennixAI_|BetaDashboard|index|phoennixai_)', re.I
)

def check_file(path: Path) -> FileResult:
    result = FileResult(name=path.name)
    content = path.read_text(encoding="utf-8", errors="ignore")

    is_brand_page = bool(BRAND_ONLY_PAGES.match(path.name))

    for rule_id, rule in RULES.items():
        if rule_id not in REQUIRED_RULES and not is_brand_page:
            continue  # skip brand-only rules for CV/Job files
        if not rule["check"](content):
            result.violations.append(f"{rule_id}: {rule['desc']}")

    return result


def run_check(files: list[Path]) -> Report:
    report = Report(total=len(files))
    for f in files:
        result = check_file(f)
        if result.clean:
            report.clean += 1
        report.files.append(result)
    return report


def auto_fix(violations_by_op: dict[str, list[str]]):
    """Run patch.py for each fixable op on the affected files."""
    import subprocess
    for op, fnames in violations_by_op.items():
        if op not in FIXABLE_OPS:
            continue
        cmd = FIXABLE_OPS[op] + ["--files"] + fnames
        print(f"\n  Fixing [{op}] on {len(fnames)} file(s)...")
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
        print(result.stdout)
        if result.returncode != 0:
            print(f"  ERROR: {result.stderr}")


# ── Output formatters ───────────────────────────────────────────────────────────

PASS = "\033[92m✓\033[0m"
FAIL = "\033[91m✗\033[0m"
WARN = "\033[93m⚠\033[0m"


def print_report(report: Report):
    print("\n=== PhoennixAI Brand Consistency Report ===\n")
    for fr in sorted(report.files, key=lambda r: (r.clean, r.name)):
        icon = PASS if fr.clean else FAIL
        print(f"  {icon} {fr.name}")
        for v in fr.violations:
            print(f"       {WARN} {v}")

    s = report.summary()
    print(f"\n{'─'*48}")
    print(f"  Files checked : {s['total']}")
    print(f"  Clean         : {s['clean']}")
    print(f"  Violations    : {s['violations']}")
    print(f"  Pass rate     : {s['pass_rate']}")
    print(f"{'─'*48}\n")

    if s['violations'] == 0:
        print("  All pages are brand-compliant.\n")
    else:
        print("  Run with --fix to auto-repair fixable violations.\n")


def print_json(report: Report):
    data = {
        "summary": report.summary(),
        "files": [
            {"name": fr.name, "clean": fr.clean, "violations": fr.violations}
            for fr in report.files
        ],
    }
    print(json.dumps(data, indent=2))


# ── Entry point ─────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="PhoennixAI Brand Checker")
    parser.add_argument("--fix", action="store_true", help="Auto-fix fixable violations")
    parser.add_argument("--json", action="store_true", help="Output JSON report")
    parser.add_argument("--files", nargs="*", help="Specific files to check (default: all)")
    args = parser.parse_args()

    if args.files:
        files = [ROOT / f for f in args.files if (ROOT / f).exists()]
    else:
        files = sorted(ROOT.glob("*.html"))

    report = run_check(files)

    if args.json:
        print_json(report)
    else:
        print_report(report)

    if args.fix:
        # Collect violations by op
        violations_by_op: dict[str, list[str]] = {}
        for fr in report.files:
            for v in fr.violations:
                rule_id = v.split(":")[0]
                op = RULES.get(rule_id, {}).get("fix_op")
                if op:
                    violations_by_op.setdefault(op, []).append(fr.name)

        if violations_by_op:
            print("Auto-fixing...")
            auto_fix(violations_by_op)
            # Re-run to confirm
            print("\nRe-checking after fixes...\n")
            report2 = run_check(files)
            print_report(report2)
            sys.exit(0 if report2.clean == report2.total else 1)

    sys.exit(0 if report.clean == report.total else 1)


if __name__ == "__main__":
    main()
