import pandas as pd
from .utils import load_parser_output, write_results

def filter_parsed(parser_output_path, min_alignment_score=0.7, min_avg_score=0.95, max_excluded_pct=0.05, min_quality_score=1.1):

    # Create output file
    with open(f'{parser_output_path}_filtered_min_as{min_alignment_score}_min_avg_as{min_avg_score}_max_ex_pct{max_excluded_pct}_min_qs{min_quality_score}.fasta', 'w') as f:
        pass

    # Load parser output
    parser_output = load_parser_output(parser_output_path)

    filtered_output = []
    for result in parser_output:
        data = {
        'header': result.header,
        'read': result.read,
        'avg_score': result.avg_score,
            'motif_df': result.motif_df,
            'excluded_pct': result.excluded_pct
        }

        # Filter reads based on score and excluded percentage
        if result.avg_score >= min_avg_score and result.excluded_pct <= max_excluded_pct and result.motif_df['quality_score'].min() >= min_quality_score and result.motif_df['alignment_score'].min() >= min_alignment_score:

            # Write the filtered reads to a new file
            write_results(f'{parser_output_path}_filtered.fasta', result.header, result.read, result.motif_df, result.excluded_pct, result.avg_score)


    # Convert parser results to DataFrame
    
    
    df = pd.DataFrame(data)

    # Filter reads based on score and excluded percentage
    df = df[df['avg_score'] >= min_avg_score]
    df = df[df['excluded_pct'] <= max_excluded_pct]
    df = df[df['motif_df']['quality_score'].min() >= min_quality_score]
    df = df[df['motif_df']['alignment_score'].min() >= min_alignment_score]


    # Get the compacted reads
    

def filter_parsed_main(parser_output_path, min_alignment_score=0.7, min_avg_score=0.95, max_excluded_pct=0.05, min_quality_score=1.1):

    filter_parsed(parser_output_path, min_alignment_score, min_avg_score, max_excluded_pct, min_quality_score)