import matplotlib.pyplot as plt from collections import Counter

def gc_content(dna_seq): gc_count = dna_seq.count('G') + dna_seq.count('C') return (gc_count / len(dna_seq)) * 100

def at_ratio(dna_seq): a_count = dna_seq.count('A') t_count = dna_seq.count('T') return a_count / (t_count + 1e-10)  # Avoid division by zero

def find_motif(dna_seq, motif): positions = [i for i in range(len(dna_seq) - len(motif) + 1) if dna_seq[i:i+len(motif)] == motif] return positions

def plot_nucleotide_composition(dna_seq): nucleotide_counts = Counter(dna_seq) plt.bar(nucleotide_counts.keys(), nucleotide_counts.values(), color=['red', 'blue', 'green', 'orange']) plt.xlabel('Nucleotide') plt.ylabel('Count') plt.title('Nucleotide Composition') plt.show()

Example DNA sequence

dna_sequence = "ATGCGATCGTACGATCGTACGTAGCTAGCTAGTACG" motif = "CGT"

print(f"GC Content: {gc_content(dna_sequence):.2f}%") 
print(f"AT Ratio: {at_ratio(dna_sequence):.2f}") 
print(f"Motif '{motif}' found at positions: {find_motif(dna_sequence, motif)}")

plot_nucleotide_composition(dna_sequence)

