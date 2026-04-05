#!/usr/bin/env python3
"""
PhoennixAI HTML Patch Tool
Applies targeted changes across all (or selected) HTML files.

Usage:
  python3 tools/patch.py --op favicon
  python3 tools/patch.py --op meta-viewport
  python3 tools/patch.py --op inject-head --snippet '<script src="/js/analytics.js"></script>'
  python3 tools/patch.py --op inject-head --snippet-file tools/snippets/cookie-banner.html
  python3 tools/patch.py --op replace --find 'OLD TEXT' --replace 'NEW TEXT'
  python3 tools/patch.py --op css-var --var '--phoenix-blue' --value '#00E5FF'
  python3 tools/patch.py --files PhoennixAI_Auth_Login.html BetaDashboard.html --op favicon
  python3 tools/patch.py --dry-run --op favicon
"""

import os, re, sys, argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent

BRAND = {
    "favicon_block": (
        '<link rel="icon" type="image/svg+xml" href="/favicon.svg">\n'
        '<link rel="alternate icon" type="image/png" sizes="32x32" href="/favicon.svg">'
    ),
    "meta_charset":   '<meta charset="UTF-8">',
    "meta_viewport":  '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    "required_fonts": "fonts.googleapis.com/css2?family=Bebas+Neue",
    "css_vars": {
        "--midnight":        "#060A18",
        "--phoenix-blue":    "#00E5FF",
        "--fire":            "#FF6B2B",
        "--gold":            "#FFB830",
    },
}

FAVICON_STRIP = [
    r'<link[^>]*rel=["\'](?:icon|shortcut icon|alternate icon)["\'][^>]*/?\s*>',
    r'<link[^>]*type=["\']image/(?:x-icon|jpeg|png|svg\+xml)["\'][^>]*/?\s*>',
]


def get_html_files(root: Path, names: list[str] | None = None) -> list[Path]:
    if names:
        paths = [root / n for n in names]
        missing = [p for p in paths if not p.exists()]
        if missing:
            print(f"WARNING: not found: {[str(m) for m in missing]}")
        return [p for p in paths if p.exists()]
    return sorted(root.glob("*.html"))


def strip_favicons(content: str) -> str:
    for pat in FAVICON_STRIP:
        content = re.sub(pat, "", content)
    return content


def inject_after_head(content: str, block: str) -> tuple[str, bool]:
    for tag in ("<head>", "<HEAD>"):
        if tag in content:
            return content.replace(tag, tag + "\n" + block, 1), True
    return block + "\n" + content, True


def op_favicon(content: str) -> str:
    content = strip_favicons(content)
    content, _ = inject_after_head(content, BRAND["favicon_block"])
    return content


def op_meta_viewport(content: str) -> str:
    if BRAND["meta_viewport"] not in content:
        content, _ = inject_after_head(content, BRAND["meta_viewport"])
    return content


def op_meta_charset(content: str) -> str:
    if BRAND["meta_charset"] not in content:
        content, _ = inject_after_head(content, BRAND["meta_charset"])
    return content


def op_inject_head(content: str, snippet: str) -> str:
    if snippet in content:
        return content  # already present, skip
    content, _ = inject_after_head(content, snippet)
    return content


def op_replace(content: str, find: str, replace: str) -> str:
    return content.replace(find, replace)


def op_css_var(content: str, var: str, value: str) -> str:
    # Update CSS variable value inside :root { ... }
    pattern = rf'({re.escape(var)}\s*:\s*)[^;]+;'
    replacement = rf'\g<1>{value};'
    return re.sub(pattern, replacement, content)


def process_file(path: Path, op: str, dry_run: bool, **kwargs) -> str:
    content = path.read_text(encoding="utf-8", errors="ignore")
    original = content

    if op == "favicon":
        content = op_favicon(content)
    elif op == "meta-viewport":
        content = op_meta_viewport(content)
    elif op == "meta-charset":
        content = op_meta_charset(content)
    elif op == "inject-head":
        content = op_inject_head(content, kwargs["snippet"])
    elif op == "replace":
        content = op_replace(content, kwargs["find"], kwargs["replace"])
    elif op == "css-var":
        content = op_css_var(content, kwargs["var"], kwargs["value"])
    else:
        return f"UNKNOWN OP: {op}"

    changed = content != original
    if changed and not dry_run:
        path.write_text(content, encoding="utf-8")

    tag = "CHANGED" if changed else "UNCHANGED"
    if dry_run and changed:
        tag = "DRY-RUN (would change)"
    return tag


def main():
    parser = argparse.ArgumentParser(description="PhoennixAI HTML Patcher")
    parser.add_argument("--op", required=True,
                        choices=["favicon", "meta-viewport", "meta-charset",
                                 "inject-head", "replace", "css-var"],
                        help="Operation to apply")
    parser.add_argument("--files", nargs="*", help="Specific files (default: all *.html)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--snippet", help="HTML snippet to inject (for inject-head)")
    parser.add_argument("--snippet-file", help="File containing snippet to inject (for inject-head)")
    parser.add_argument("--find", help="Text to find (for replace)")
    parser.add_argument("--replace", dest="replace_with", help="Replacement text (for replace)")
    parser.add_argument("--var", help="CSS variable name (for css-var)")
    parser.add_argument("--value", help="CSS variable value (for css-var)")
    args = parser.parse_args()

    # Validate op-specific args
    if args.op == "inject-head":
        if args.snippet_file:
            args.snippet = Path(args.snippet_file).read_text(encoding="utf-8")
        if not args.snippet:
            parser.error("--snippet or --snippet-file required for inject-head")
    if args.op == "replace" and (not args.find or args.replace_with is None):
        parser.error("--find and --replace required for replace op")
    if args.op == "css-var" and (not args.var or not args.value):
        parser.error("--var and --value required for css-var op")

    files = get_html_files(ROOT, args.files)
    print(f"=== PhoennixAI Patch: {args.op} | {len(files)} files | dry-run={args.dry_run} ===")

    kwargs = {
        "snippet":     getattr(args, "snippet", None),
        "find":        getattr(args, "find", None),
        "replace":     getattr(args, "replace_with", None),
        "var":         getattr(args, "var", None),
        "value":       getattr(args, "value", None),
    }

    changed_count = 0
    for f in files:
        result = process_file(f, args.op, args.dry_run, **kwargs)
        if "CHANGED" in result:
            changed_count += 1
        print(f"  {result:<30} {f.name}")

    print(f"\nDone. {changed_count}/{len(files)} files {'would be ' if args.dry_run else ''}changed.")


if __name__ == "__main__":
    main()
