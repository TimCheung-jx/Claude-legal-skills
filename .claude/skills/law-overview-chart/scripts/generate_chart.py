#!/usr/bin/env python3
"""
Generate a visual overview chart HTML for Chinese laws and regulations.

Usage:
    python generate_chart.py <input_json> <output_html>
    python generate_chart.py -  # reads JSON from stdin, outputs HTML to stdout
"""

import json
import sys
import os


def generate_html(data: dict) -> str:
    """Generate HTML overview chart from parsed law data."""

    law_name = data.get("law_name", "法律法规概览")
    chapters = data.get("chapters", [])

    # CSS styles
    css = """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 50%, #90caf9 100%);
            min-height: 100vh;
            padding: 40px 20px;
            color: #2c3e50;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        .page-title {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            color: #0d47a1;
            margin-bottom: 40px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .chapter-section {
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.5);
        }
        .chapter-title {
            font-size: 20px;
            font-weight: 700;
            color: #1565c0;
            margin-bottom: 16px;
            padding-bottom: 8px;
            border-bottom: 2px solid #bbdefb;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .chapter-title::before {
            content: "";
            display: inline-block;
            width: 4px;
            height: 20px;
            background: #1565c0;
            border-radius: 2px;
        }
        .articles-grid {
            display: grid;
            gap: 12px;
        }
        .article-card {
            background: #ffffff;
            border-radius: 10px;
            padding: 14px 10px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            border: 1px solid rgba(0, 0, 0, 0.04);
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: default;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 70px;
        }
        .article-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
        }
        .article-number {
            font-size: 12px;
            color: #78909c;
            margin-bottom: 4px;
            font-weight: 500;
        }
        .article-topic {
            font-size: 14px;
            font-weight: 600;
            color: #37474f;
            line-height: 1.3;
            word-break: keep-all;
        }
        /* Highlight levels */
        .article-card.highlight-red {
            background: #e74c3c;
            border-color: #c0392b;
        }
        .article-card.highlight-red .article-number,
        .article-card.highlight-red .article-topic {
            color: #ffffff;
        }
        .article-card.highlight-orange {
            background: #e67e22;
            border-color: #d35400;
        }
        .article-card.highlight-orange .article-number,
        .article-card.highlight-orange .article-topic {
            color: #ffffff;
        }
        .article-card.highlight-blue {
            background: #3498db;
            border-color: #2980b9;
        }
        .article-card.highlight-blue .article-number,
        .article-card.highlight-blue .article-topic {
            color: #ffffff;
        }
        /* Print optimization */
        @media print {
            body {
                background: #e3f2fd;
                padding: 20px;
            }
            .chapter-section {
                break-inside: avoid;
                page-break-inside: avoid;
            }
        }
        /* Responsive */
        @media (max-width: 768px) {
            .page-title { font-size: 24px; }
            .chapter-title { font-size: 16px; }
            .articles-grid { grid-template-columns: repeat(2, 1fr) !important; }
        }
    """

    # Determine grid columns based on article count per chapter
    def get_columns(count: int) -> int:
        if count <= 4:
            return count
        elif count <= 6:
            return 3
        elif count <= 12:
            return 4
        elif count <= 20:
            return 5
        else:
            return 6

    # Build chapter sections
    chapters_html = []
    for chapter in chapters:
        title = chapter.get("title", "")
        articles = chapter.get("articles", [])
        if not articles:
            continue

        cols = get_columns(len(articles))
        grid_style = f"grid-template-columns: repeat({cols}, 1fr);"

        cards_html = []
        for article in articles:
            num = article.get("number", "")
            topic = article.get("topic", "")
            highlight = article.get("highlight", False)
            level = article.get("level", "red" if highlight else "")

            # Determine CSS class
            if level == "red" or (highlight and not level):
                card_class = "article-card highlight-red"
            elif level == "orange":
                card_class = "article-card highlight-orange"
            elif level == "blue":
                card_class = "article-card highlight-blue"
            else:
                card_class = "article-card"

            cards_html.append(
                f'<div class="{card_class}">'
                f'<div class="article-number">{num}</div>'
                f'<div class="article-topic">{topic}</div>'
                f'</div>'
            )

        cards_str = "\n".join(cards_html)
        chapters_html.append(
            f'<div class="chapter-section">\n'
            f'  <div class="chapter-title">{title}</div>\n'
            f'  <div class="articles-grid" style="{grid_style}">\n'
            f'    {cards_str}\n'
            f'  </div>\n'
            f'</div>'
        )

    chapters_str = "\n".join(chapters_html)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>《{law_name}》概览图</title>
    <style>{css}</style>
</head>
<body>
    <div class="container">
        <h1 class="page-title">《{law_name}》概览</h1>
        {chapters_str}
    </div>
</body>
</html>"""

    return html


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_chart.py <input_json> [output_html]", file=sys.stderr)
        print("       python generate_chart.py -  # read stdin, write stdout", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    # Read input
    if input_path == "-":
        data = json.load(sys.stdin)
    else:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

    # Generate HTML
    html = generate_html(data)

    # Write output
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"HTML generated: {output_path}")
    else:
        print(html)


if __name__ == "__main__":
    main()
