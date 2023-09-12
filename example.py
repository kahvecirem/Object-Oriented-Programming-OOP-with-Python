class Organism:
    def _init_(self, name, species):
        self.name = name
        self.species = species
        self.genes = []

    def add_gene(self, gene_name, sequence):
        gene = Gene(gene_name, sequence)
        self.genes.append(gene)

    def describe(self):
        print(f"Organism Name: {self.name}")
        print(f"Species: {self.species}")
        print("Genes:")
        for gene in self.genes:
            print(f"- {gene.name}: {gene.sequence}")

class Gene:
    def _init_(self, name, sequence):
        self.name = name
        self.sequence = sequence

# Organizm oluşturma
organism1 = Organism("Sample Organism", "Homo sapiens")
organism1.add_gene("Gene A", "ATGCGTA")
organism1.add_gene("Gene B", "TAGCTAG")

# Organizmayı tanımlama
organism1.describe()
