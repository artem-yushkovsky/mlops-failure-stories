import sys
import markdown
import argparse
from pathlib import Path

def get_parser():
    p = argparse.ArgumentParser()
    p.add_argument("--in_md", type=Path, required=True)
    p.add_argument("--in_html_template", type=Path, required=True)
    p.add_argument("--out_html", type=Path, required=True)
    return p
    

if __name__ == "__main__":
    args = get_parser().parse_args()
    in_md = args.in_md
    in_html_template = args.in_html_template
    out_html = args.out_html

    inner_html = markdown.markdown(in_md.read_text())
    result_html = in_html_template.read_text().replace("{{content}}", inner_html)
    out_html.write_text(result_html)
    print(f"[+] Success: {in_md} + {in_html_template} -> {out_html}")
