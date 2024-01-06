import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

def read_and_combine_excel_sheets(file_path):
    """
    Reads an Excel file with multiple sheets and combines them into a single DataFrame.
    Adds a column to indicate the sheet name.
    """
    all_sheets = pd.read_excel(file_path, sheet_name=None)
    df_combined = pd.concat(
        {sheet_name: sheet.assign(Sheet_Name=sheet_name) for sheet_name, sheet in all_sheets.items()},
        ignore_index=True
    )
    return df_combined

def split_aggregate_score_column(df, column_name):
    """
    Splits a column containing aggregate scores into two separate columns for min and max scores.
    """
    df[['Min Aggregate', 'Max Aggregate']] = df[column_name].str.split('-', expand=True)
    df['Min Aggregate'] = pd.to_numeric(df['Min Aggregate'], errors='coerce')
    df['Max Aggregate'] = pd.to_numeric(df['Max Aggregate'], errors='coerce')
    return df

def create_dumbbell_charts(df, group_column, min_col, max_col, label_col):
    """
    Creates dumbbell charts for each group in the DataFrame.
    Each chart shows the range of values from min_col to max_col, labeled by label_col.
    """
    grouped = df.groupby(group_column)
    for name, group in grouped:
        plt.figure(figsize=(10, len(group) * 0.5))
        plt.hlines(y=group[label_col], xmin=group[min_col], xmax=group[max_col], color='skyblue')
        plt.plot(group[min_col], group[label_col], 'o', markersize=5, color='green')
        plt.plot(group[max_col], group[label_col], 'o', markersize=5, color='red')
        plt.title(f'Dumbbell Chart of Aggregate Score for {name}')
        plt.xlabel('Aggregate Score')
        plt.ylabel('Course Name')
        plt.gca().invert_yaxis()  # Invert y-axis for better readability
        plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))  # Only integer values on x-axis
        plt.tight_layout()
        
        # Saving the chart to a file
        output_path = f"{output_dir}/Dumbbell_Chart_{name}.png"  # Specify the format and directory here
        plt.savefig(output_path, format='png', dpi=300)
        plt.close()  # Close the plot to free memory

# Main execution
if __name__ == "__main__":
    file_path = 'your_excel_file.xlsx'  # Replace with your file path
    df_combined = read_and_combine_excel_sheets(file_path)
    df_combined = split_aggregate_score_column(df_combined, '2023 Range of Aggregate Score (Net)')
    create_dumbbell_charts(df_combined, 'Sheet_Name', 'Min Aggregate', 'Max Aggregate', 'Course Name ')
