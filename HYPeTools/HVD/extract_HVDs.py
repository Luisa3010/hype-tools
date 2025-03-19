#!/usr/bin/env python3

"""
This script splits HYPe reads into HVDs (Hypervariable Domains) and conserved domains from FASTA files by identifying the positions of the 
specified start and end markers. It can process either a single FASTA file or a directory of FASTA files.


"""

import os
import argparse
from tqdm import tqdm
from .utils import extract_hvd_from_read

def process_fasta_file(input_path, output_path, start, end):
    hvd_outfile = output_path + "_hvd.fasta"
    c1_outfile = output_path + "_c1.fasta"
    c2_outfile = output_path + "_c2.fasta"

    # Open input and output files
    with open(input_path, 'r') as infile, open(hvd_outfile, 'w') as hvd_outfile, \
        open(c1_outfile, 'w') as c1_outfile, open(c2_outfile, 'w') as c2_outfile:
        current_id = None
        for line in infile:
            line = line.strip()
            
            # Check if this is a header line starting with '>'
            if line.startswith('>'):
                current_id = line
            # If we have a sequence line (after header)
            elif current_id is not None:
                # Process the read to extract HVD
                hvd, c1, c2 = extract_hvd_from_read(line, start, end)
                # Write header and HVD sequence
                hvd_outfile.write(f"{current_id}\n")
                hvd_outfile.write(f"{hvd}\n")
                c1_outfile.write(f"{current_id}\n")
                c1_outfile.write(f"{c1}\n")
                c2_outfile.write(f"{current_id}\n")
                c2_outfile.write(f"{c2}\n")
                current_id = None

def extract_hvds(input_path, start, end):
    """Extract HVDs from either a single file or directory of files"""
    
    if os.path.isfile(input_path):
        # Process single file
        process_fasta_file(input_path, input_path, start, end)
        
    elif os.path.isdir(input_path):
        # Process directory
        files = [f for f in os.listdir(input_path) 
                if os.path.isfile(os.path.join(input_path, f)) and f.endswith('.fasta')]
        
        output_folder = input_path + "_output"
        os.makedirs(output_folder, exist_ok=True)
        
        for filename in tqdm(files, desc="Processing files"):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_folder, filename)
            process_fasta_file(input_file, output_file, start, end)


def extract_main(input_path, start, end):
   
    extract_hvds(input_path, start, end)
