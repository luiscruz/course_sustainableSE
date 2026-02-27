#!/usr/bin/env python3
"""
Generate violin plots for energy and time distributions from EnergiBridge CSV files.

Usage:
    python scripts/generate_violin_plots.py \
        --data-dir <path/to/energibridge_runs_all_languages> \
        --output-dir 2026/p1_measuring_software/img/g8_programming_languages_data_ingestion
"""

import argparse
import csv
import math
from pathlib import Path
from collections import defaultdict

def load_data(data_dir):
    """Load energy and time data from EnergiBridge CSV files."""
    runs_dir = Path(data_dir)
    energy_data = defaultdict(list)
    time_data = defaultdict(list)
    
    for csv_file in sorted(runs_dir.glob('*_measured_*.csv')):
        lang = csv_file.name.split('_')[0]
        
        with csv_file.open('r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            first = next(reader)
            last = first
            for last in reader:
                pass
        
        t0 = float(first['Time'])
        t1 = float(last['Time'])
        duration_s = (t1 - t0) / 1000.0
        
        e0 = float(first['PACKAGE_ENERGY (J)'])
        e1 = float(last['PACKAGE_ENERGY (J)'])
        energy_j = e1 - e0
        
        energy_data[lang].append(energy_j)
        time_data[lang].append(duration_s)
    
    return energy_data, time_data

def create_violin_svg(data_dict, title, ylabel, output_path, y_range=None):
    """Create a violin plot SVG from data dictionary {lang: [values]}."""
    langs = ['rust', 'python', 'go', 'java']
    colors = {
        'python': '#1f77b4',
        'go': '#ff7f0e',
        'rust': '#2ca02c',
        'java': '#d62728'
    }
    
    W, H = 900, 500
    padL, padR, padT, padB = 80, 40, 60, 80
    plotW = W - padL - padR
    plotH = H - padT - padB
    
    # Determine y range
    all_vals = [v for vals in data_dict.values() for v in vals]
    if y_range is None:
        y_min, y_max = min(all_vals), max(all_vals)
        y_pad = (y_max - y_min) * 0.1
        y_min -= y_pad
        y_max += y_pad
    else:
        y_min, y_max = y_range
    
    def Y(val):
        return padT + plotH * (1 - (val - y_min) / (y_max - y_min))
    
    def X(i):
        return padL + plotW * (i + 0.5) / len(langs)
    
    # Kernel density estimation (simplified)
    def kde(values, x_min, x_max, n_points=100):
        """Simple KDE using Gaussian kernel."""
        if not values:
            return []
        std = math.sqrt(sum((v - sum(values)/len(values))**2 for v in values) / len(values))
        if std < 1e-6:
            std = (x_max - x_min) * 0.1
        x_vals = [x_min + (x_max - x_min) * i / (n_points - 1) for i in range(n_points)]
        densities = []
        for x in x_vals:
            density = sum(math.exp(-0.5 * ((x - v) / std) ** 2) for v in values)
            densities.append(density)
        max_d = max(densities) if densities else 1
        return [(x, d / max_d) for x, d in zip(x_vals, densities)]
    
    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    svg.append('<style>text{font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif; fill:#111;} .axis{stroke:#333;stroke-width:1.5;} .grid{stroke:#ddd;stroke-width:1;} .violin{fill-opacity:0.6; stroke:#333; stroke-width:1.5;} .median{stroke:#000; stroke-width:2;} .quartile{stroke:#555; stroke-width:1.5;}</style>')
    svg.append(f'<text x="{W/2}" y="28" text-anchor="middle" font-size="18" font-weight="600">{title}</text>')
    
    # Axes
    svg.append(f'<line class="axis" x1="{padL}" y1="{padT}" x2="{padL}" y2="{padT+plotH}"/>')
    svg.append(f'<line class="axis" x1="{padL}" y1="{padT+plotH}" x2="{padL+plotW}" y2="{padT+plotH}"/>')
    
    # Y-axis ticks and grid
    n_ticks = 6
    for k in range(n_ticks):
        val = y_min + (y_max - y_min) * k / (n_ticks - 1)
        yy = Y(val)
        svg.append(f'<line class="grid" x1="{padL}" y1="{yy:.1f}" x2="{padL+plotW}" y2="{yy:.1f}"/>')
        svg.append(f'<text x="{padL-10}" y="{yy+4:.1f}" text-anchor="end" font-size="11">{val:.1f}</text>')
    svg.append(f'<text x="20" y="{padT+plotH/2}" transform="rotate(-90 20 {padT+plotH/2})" text-anchor="middle" font-size="13" font-weight="500">{ylabel}</text>')
    
    # Violin plots
    violin_width = plotW / (len(langs) * 2.5)
    
    for i, lang in enumerate(langs):
        if lang not in data_dict or not data_dict[lang]:
            continue
        
        vals = sorted(data_dict[lang])
        cx = X(i)
        
        # Statistics
        n = len(vals)
        median = vals[n//2] if n % 2 == 1 else (vals[n//2-1] + vals[n//2]) / 2
        q1 = vals[n//4]
        q3 = vals[3*n//4]
        
        # KDE for violin shape
        kde_pts = kde(vals, y_min, y_max, 80)
        if kde_pts:
            # Left side
            path_left = f"M {cx:.1f} {Y(kde_pts[0][0]):.1f}"
            for x_density, y_val in kde_pts:
                x_offset = -violin_width * x_density * 0.5
                path_left += f" L {cx + x_offset:.1f} {Y(y_val):.1f}"
            # Right side
            for x_density, y_val in reversed(kde_pts):
                x_offset = violin_width * x_density * 0.5
                path_left += f" L {cx + x_offset:.1f} {Y(y_val):.1f}"
            path_left += " Z"
            
            svg.append(f'<path class="violin" d="{path_left}" fill="{colors[lang]}"/>')
        
        # Median line
        svg.append(f'<line class="median" x1="{cx-violin_width*0.6:.1f}" y1="{Y(median):.1f}" x2="{cx+violin_width*0.6:.1f}" y2="{Y(median):.1f}"/>')
        
        # Quartile box
        box_h = abs(Y(q1) - Y(q3))
        box_y = Y(q3)
        svg.append(f'<rect x="{cx-violin_width*0.3:.1f}" y="{box_y:.1f}" width="{violin_width*0.6:.1f}" height="{box_h:.1f}" fill="none" class="quartile"/>')
        
        # Whiskers (simplified: min/max)
        svg.append(f'<line class="quartile" x1="{cx:.1f}" y1="{Y(vals[0]):.1f}" x2="{cx:.1f}" y2="{Y(vals[-1]):.1f}"/>')
        svg.append(f'<line class="quartile" x1="{cx-violin_width*0.2:.1f}" y1="{Y(vals[0]):.1f}" x2="{cx+violin_width*0.2:.1f}" y2="{Y(vals[0]):.1f}"/>')
        svg.append(f'<line class="quartile" x1="{cx-violin_width*0.2:.1f}" y1="{Y(vals[-1]):.1f}" x2="{cx+violin_width*0.2:.1f}" y2="{Y(vals[-1]):.1f}"/>')
        
        # Language label
        svg.append(f'<text x="{cx:.1f}" y="{padT+plotH+28}" text-anchor="middle" font-size="13" font-weight="500">{lang.title()}</text>')
    
    svg.append('</svg>')
    
    output_path.write_text('\n'.join(svg), encoding='utf-8')
    print(f"Generated: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Generate violin plots from EnergiBridge CSVs')
    parser.add_argument('--data-dir', required=True, help='Path to energibridge_runs_all_languages directory')
    parser.add_argument('--output-dir', default='2026/p1_measuring_software/img/g8_programming_languages_data_ingestion', help='Output directory for SVG files')
    args = parser.parse_args()
    
    energy_data, time_data = load_data(args.data_dir)
    
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    create_violin_svg(
        energy_data,
        'Energy distribution across measured runs (violin plot)',
        'Package energy (J)',
        output_dir / 'energy_violin.svg'
    )
    
    create_violin_svg(
        time_data,
        'Time distribution across measured runs (violin plot)',
        'Wall time (s)',
        output_dir / 'time_violin.svg'
    )
    
    print(f"\nGenerated violin plots in {output_dir}")
    print("  - energy_violin.svg")
    print("  - time_violin.svg")

if __name__ == '__main__':
    main()
