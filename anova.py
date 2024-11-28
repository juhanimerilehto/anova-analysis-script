import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def perform_anova_analysis(excel_path='data.xlsx',
                         group_column='Group',      # Column containing group labels
                         value_column='Value',      # Column containing measurements
                         output_prefix='anova'):    # Prefix for output files
    """
    Performs one-way ANOVA analysis with post-hoc Tukey test.
    
    Parameters:
    -----------
    excel_path : str
        Path to Excel file containing the data
    group_column : str
        Name of column containing group labels
    value_column : str
        Name of column containing the values to compare
    output_prefix : str
        Prefix for output files
    """
    
    # Read the data
    print(f"Reading data from {excel_path}...")
    df = pd.read_excel(excel_path)
    
    # Get unique groups
    groups = df[group_column].unique()
    
    # Perform one-way ANOVA
    groups_data = [df[df[group_column] == group][value_column] for group in groups]
    f_stat, p_value = stats.f_oneway(*groups_data)
    
    # Perform Tukey's HSD test
    tukey = pairwise_tukeyhsd(df[value_column], df[group_column])
    
    # Calculate descriptive statistics
    desc_stats = df.groupby(group_column)[value_column].agg([
        'count', 'mean', 'std', 'sem'
    ]).round(4)
    
    # Create results dictionary
    results = {
        'Test Type': 'One-way ANOVA',
        'F-statistic': f_stat,
        'p-value': p_value,
        'Significant': 'Yes' if p_value < 0.05 else 'No',
        'Number of Groups': len(groups),
        'Total Observations': len(df)
    }
    
    # Convert results to DataFrame
    results_df = pd.DataFrame([results])
    
    # Create timestamp for file naming
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save results to Excel
    excel_output = f'{output_prefix}_results_{timestamp}.xlsx'
    with pd.ExcelWriter(excel_output) as writer:
        results_df.to_excel(writer, sheet_name='ANOVA Results', index=False)
        desc_stats.to_excel(writer, sheet_name='Descriptive Stats')
        pd.DataFrame(tukey._results_table).to_excel(writer, sheet_name='Tukey Results', index=False)
    
    print("\nResults saved to:", excel_output)
    
    # Create visualizations
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Boxplot with points
    sns.boxplot(x=group_column, y=value_column, data=df, ax=ax1)
    sns.swarmplot(x=group_column, y=value_column, data=df, 
                 color='0.25', size=4, alpha=0.5, ax=ax1)
    ax1.set_title(f'Group Comparisons\np = {p_value:.4f}')
    
    # Means plot with error bars (95% CI)
    sns.pointplot(x=group_column, y=value_column, data=df, 
                 ci=95, join=False, ax=ax2)
    ax2.set_title('Group Means with 95% CI')
    
    plt.tight_layout()
    
    # Save plot
    plot_output = f'{output_prefix}_plot_{timestamp}.png'
    plt.savefig(plot_output, dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Plot saved to:", plot_output)
    
    # Print results to terminal
    print("\nOne-way ANOVA Results:")
    print("---------------------")
    print(f"F-statistic: {f_stat:.4f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Significant difference: {'Yes' if p_value < 0.05 else 'No'}")
    print("\nDescriptive Statistics:")
    print(desc_stats)
    print("\nTukey's HSD Test Results:")
    print(tukey)

if __name__ == "__main__":
    # Example usage:
    # Modify these parameters according to your data
    perform_anova_analysis(
        excel_path='student_wellbeing_dataset.xlsx',
        group_column='InterventionGroup',
        value_column='PostFitnessScore',
        output_prefix='intervention_impact_anova'
    )