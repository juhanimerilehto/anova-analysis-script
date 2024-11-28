# Statistical Analysis Suite - ANOVA Module

**Version 1.0**
### Creator: Juhani Merilehto - @juhanimerilehto - Jyväskylä University of Applied Sciences (JAMK), Likes institute

![JAMK Likes Logo](./assets/likes_str_logo.png)

## Overview

ANOVA (Analysis of Variance) script. This Python-based tool enables automated one-way ANOVA analysis for comparing means across multiple groups. Developed for the Strategic Exercise Information and Research unit in Likes Institute, at JAMK University of Applied Sciences, this module provides comprehensive statistical output including post-hoc analysis, visualizations, Excel reports, and terminal feedback.

## Features

- **Complete ANOVA Analysis**: One-way ANOVA with Tukey's HSD post-hoc testing
- **Comprehensive Output**: F-statistics, p-values, and effect sizes
- **Advanced Visualization**: Boxplots, mean plots with confidence intervals
- **Excel Integration**: Multi-sheet results with detailed statistics
- **Post-hoc Analysis**: Automated Tukey's HSD test for multiple comparisons
- **Terminal Feedback**: Clear, formatted statistical output
- **Tested**: Tested with simulated quantitative data

## Hardware Requirements

- **Python:** 3.8 or higher
- **RAM:** 8GB recommended
- **Storage:** 1GB free space for analysis outputs
- **OS:** Windows 10/11, MacOS, or Linux

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/juhanimerilehto/anova-analysis-script.git
cd anova-analysis-script
```

### 2. Create a virtual environment:
```bash
python -m venv stats-env
source stats-env/bin/activate  # For Windows: stats-env\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python anova.py
```

With custom parameters:
```bash
python anova.py --excel_path "your_data.xlsx" --group_column "Group" --value_column "Value"
```

## Configuration Parameters

- `excel_path`: Path to Excel file (default: 'data.xlsx')
- `group_column`: Column containing group labels (default: 'Group')
- `value_column`: Column containing measurements (default: 'Value')
- `output_prefix`: Prefix for output files (default: 'anova')

## File Structure

```plaintext
├── anova-analysis-script/
│   ├── assets/
│   │   └── likes_str_logo.png
│   ├── anova.py
│   ├── requirements.txt
│   └── README.md
```

## Credits

- **Juhani Merilehto (@juhanimerilehto)** – Specialist, Data and Statistics
- **JAMK Likes** – Organization sponsor

## License

This project is licensed for free use under the condition that proper credit is given to Juhani Merilehto (@juhanimerilehto) and JAMK Likes institute. You are free to use, modify, and distribute this project, provided that you mention the original author and institution and do not hold them liable for any consequences arising from the use of the software.