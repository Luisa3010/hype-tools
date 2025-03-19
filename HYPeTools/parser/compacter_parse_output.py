from .utils import load_parser_output


def compacter_output(parser_output_path, dna = True, protein = True):

    # Create output files
    with open(f'{parser_output_path}_compact_dna.fasta', 'w') as f:
        pass
    with open(f'{parser_output_path}_compact_protein.fasta', 'w') as f:
        pass

    # Load parser output    
    parser_output = load_parser_output(parser_output_path)

    for result in parser_output:
        
        if result.motifs_df is None:
            continue

        header = result.header

        if dna:
            dna_motifs = " ".join(result.motifs_df['motif'].tolist())
            with open(f'{parser_output_path}_compact_dna.fasta', 'a') as f:
                f.write(f"{header}\n{dna_motifs}\n")

        if protein:
            protein_motifs = " ".join(result.motifs_df['amino_acid'].tolist())
            with open(f'{parser_output_path}_compact_protein.fasta', 'a') as f:
                f.write(f"{header}\n{protein_motifs}\n")





def compacter_output_main(parser_output_path, dna = True, protein = True):
    compacter_output(parser_output_path, dna, protein)    