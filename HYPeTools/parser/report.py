from .utils import load_parser_output
import pandas as pd
from collections import Counter

def generate_report(parser_output_path):

    # Load parser output
    parser_output = load_parser_output(parser_output_path)

    # Convert parser results to DataFrame
    data = [{
        'read': result.read,
        'avg_score': result.avg_score,
        'motif_df': result.motif_df,
        'excluded_pct': result.excluded_pct
    } for result in parser_output]
    
    df = pd.DataFrame(data)
    
    # Extract motifs from motif_df and join them
    hvds = df['motif_df'].apply(lambda x: ' '.join(x['motif'].tolist()) if not x.empty else '').tolist()
    
    # Count motif occurrences
    all_hvds = []
    for hvd_str in hvds:
        if hvd_str:  # Skip empty strings
            all_hvds.extend(hvd_str.split())
            
    hvd_counts = Counter(all_hvds)
    
    print("\nTop 10 most frequent HVDs:")
    for hvd, count in hvd_counts.most_common(10):
        print(f"{hvd}: {count}")    
    
    # Get statistical description of numerical columns
    print("\nStatistical Summary:")
    print(df[['avg_score', 'excluded_pct']].describe())

    # Count empty reads
    empty_reads = df['read'].apply(lambda x: not bool(x)).sum()
    print(f"Number of empty reads:\t\t\t\t\t {empty_reads}")

    # Not empty reads
    not_empty_reads = df['read'].apply(lambda x: bool(x)).sum()
    print(f"Number of not empty reads:\t\t\t\t {not_empty_reads}")

    # Get number of reads with low quality
    low_quality_reads = df[df['avg_score'] < 0.92 and df['excluded_pct'] > 0.05].shape[0]
    print(f"Number of reads with low quality:\t\t\t {low_quality_reads}")

    # Get number of reads with low quality
    low_medium_quality_reads = df[df['avg_score'] < 0.98 or df['excluded_pct'] > 0.04].shape[0]
    print(f"Number of reads with medium quality:\t\t\t {low_medium_quality_reads - low_quality_reads}")
    
    # Get number of reads with perfect quality
    perfect_quality_reads = df[df['avg_score'] ==1 and df['excluded_pct'] == 0.00].shape[0]

    # Get number of reads with high quality
    high_quality_reads = df[df['avg_score'] > 0.98 and df['excluded_pct'] < 0.04].shape[0]
    print(f"Number of reads with high - but not perfect quality:\t {high_quality_reads - perfect_quality_reads}")
    
    print(f"Number of reads with perfect quality:\t\t\t {perfect_quality_reads}")
    

    
    

def report_main(parser_output_path):
    
    generate_report(parser_output_path)