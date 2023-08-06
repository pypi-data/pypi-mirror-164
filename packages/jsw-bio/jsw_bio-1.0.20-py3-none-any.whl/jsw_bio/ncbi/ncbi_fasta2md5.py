import hashlib


def ncbi_fasta2md5(fasta_str):
    lines = fasta_str.split('\n')
    seq = ''.join(lines[1:]).strip()
    seq = seq.replace('\n', '')

    print('processed seq is: ',seq)
    md5 = hashlib.md5(seq.encode('utf-8')).hexdigest()
    return md5.upper()
