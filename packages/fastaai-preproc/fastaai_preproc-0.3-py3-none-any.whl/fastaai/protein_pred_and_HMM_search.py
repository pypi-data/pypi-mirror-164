import sys
import os
import gzip
import multiprocessing
import argparse
from math import ceil
import datetime 

import pyrodigal
import pyhmmer

class progress_tracker:
	def __init__(self, total, step_size = 2, message = None, one_line = True):
		self.current_count = 0
		self.max_count = total
		#Book keeping.
		self.start_time = None
		self.end_time = None
		#Show progrexx every [step] percent
		self.step = step_size
		self.justify_size = ceil(100/self.step)
		self.last_percent = 0
		self.message = message
		
		self.pretty_print = one_line
		
		self.start()

	def curtime(self):
		time_format = "%d/%m/%Y %H:%M:%S"
		timer = datetime.datetime.now()
		time = timer.strftime(time_format)
		return time
		
	def start(self):
		print("")
		if self.message is not None:
			print(self.message)
		
		try:
			percentage = (self.current_count/self.max_count)*100
			sys.stdout.write("Completion".rjust(3)+ ' |'+('#'*int(percentage/self.step)).ljust(self.justify_size)+'| ' + ('%.2f'%percentage).rjust(7)+'% ( ' + str(self.current_count) + " of " + str(self.max_count) + ' ) at ' + self.curtime() + "\n")
			sys.stdout.flush()
			
		except:
			#It's not really a big deal if the progress bar cannot be printed.
			pass
	
	def update(self):
		self.current_count += 1
		percentage = (self.current_count/self.max_count)*100
		try:
			if percentage // self.step > self.last_percent:
				if self.pretty_print:
					sys.stdout.write('\033[A')
				sys.stdout.write("Completion".rjust(3)+ ' |'+('#'*int(percentage/self.step)).ljust(self.justify_size)+'| ' + ('%.2f'%percentage).rjust(7)+'% ( ' + str(self.current_count) + " of " + str(self.max_count) + ' ) at ' + self.curtime() + "\n")
				sys.stdout.flush()
				self.last_percent = percentage // self.step
			#Bar is always full at the end.
			if count == self.max_count:
				if self.pretty_print:
					sys.stdout.write('\033[A')
				sys.stdout.write("Completion".rjust(3)+ ' |'+('#'*self.justify_size).ljust(self.justify_size)+'| ' + ('%.2f'%percentage).rjust(7)+'% ( ' + str(self.current_count) + " of " + str(self.max_count) + ' ) at ' + self.curtime() + "\n")
				sys.stdout.flush()
				#Add space at end.
				print("")
		except:
			#It's not really a big deal if the progress bar cannot be printed.
			pass
		

#Iterator for agnostic reader
class agnostic_reader_iterator:
	def __init__(self, reader):
		self.handle_ = reader.handle
		self.is_gz_ = reader.is_gz
		
	def __next__(self):
		if self.is_gz_:
			line = self.handle_.readline().decode()
		else:
			line = self.handle_.readline()
		
		#Ezpz EOF check
		if line:
			return line
		else:
			raise StopIteration

#File reader that doesn't care if you give it a gzipped file or not.
class agnostic_reader:
	def __init__(self, file):
		self.path = file
		
		with open(file, 'rb') as test_gz:
			#Gzip magic number
			is_gz = (test_gz.read(2) == b'\x1f\x8b')
		
		self.is_gz = is_gz
		
		if is_gz:
			self.handle = gzip.open(self.path)
		else:
			self.handle = open(self.path)
			
	def __iter__(self):
		return agnostic_reader_iterator(self)
		
	def close(self):
		self.handle.close()
	
class file_importer:
	def __init__(self, genomes = None, proteins = None, output = "FastAAI", 
	compress = False, do_nt = False, trans_tables = [4], meta_mode = False, 
	do_hmm = True, trusted_cutoffs = True):
		#genomes, prots, hmms can be supplied as either directory, a file with paths 1/line, or comma-sep paths. Type is determined automatically.
		self.genomes = genomes
		self.proteins = proteins
		
		self.genome_list = None
		self.protein_list = None
		
		self.error = False
		
		self.in_files = None
		
		self.status = "genome"
		self.output = output

		self.determine_inputs()
		
		if not self.error:
			self.prep_input_files(compress, do_nt, trans_tables, meta_mode, do_hmm)
	
	def retrieve_files(self, arg):	
		done = False
		files = []
		#Case where a directory is supplied.
		if os.path.isdir(arg):
			for file in sorted(os.listdir(arg)):
				files.append(os.path.abspath(os.path.normpath(arg + '/' +file)))
			done = True

		#Case where a file containing paths is supplied.
		if os.path.isfile(arg):
			handle = agnostic_reader(arg)
			for line in handle:
				file = line.strip()
				if os.path.exists(file):			
					files.append(os.path.abspath(os.path.normpath(file)))
					
			handle.close()
			done = True
			
			if len(names) == 0 and len(files) == 0:
				#Try interpreting the file as a singular path.
				done = False
							
		#Last check.
		if not done:
			for file in arg.split(","):
				if os.path.exists(file):			
					files.append(os.path.abspath(os.path.normpath(file)))
				
		return files
	
	#Check if g/p/h
	def determine_inputs(self):	
		if self.genomes is not None:
			self.genome_list = self.retrieve_files(self.genomes)
			if self.proteins is not None:
				print("You can only supply genomes or proteins, not both.")
				self.error = True
		#Proteins, but no HMMs
		elif self.proteins is not None:
			self.protein_list = self.retrieve_files(self.proteins)
				
	def prep_input_files(self, comp, do_nt, tt, meta, do_hmm):
		self.in_files = []
		if self.genome_list is not None:
			self.status = "genome"
			for g in self.genome_list:
				f = input(genome = g, protein = None, out_dir = self.output, do_nt = do_nt, 
				trans_tables = tt, meta_mode = meta, compress = comp, do_hmm = do_hmm)
				self.in_files.append(f)
			
		if self.protein_list is not None:
			self.status = "protein"
			for p in self.protein_list:
				f = input(genome = None, protein = p, out_dir = self.output, do_nt = do_nt, 
				trans_tables = tt, meta_mode = meta, compress = comp, do_hmm = do_hmm)
				self.in_files.append(f)
	
class input:
	def __init__(self, genome = None, protein = None, do_nt = False, 
			trans_tables = [4], meta_mode = False, out_dir = None, compress = False,
			do_hmm = True):
			
		self.gen_path = genome
		self.prot_path = protein
		
		self.basename = None
		
		self.output = out_dir
		if self.output is None:
			self.output = os.getcwd()
		
		self.nt_seqs = None
		self.nt_deflines = None
		
		self.prot_seqs = None
		self.prot_deflines = None

		#prot pred opts
		self.do_nt = do_nt
		self.tt = trans_tables
		self.meta = meta_mode
		self.nt_out = None
		self.aa_out = None
		
		self.hmm_out = None
		self.do_hmm = do_hmm
		
		self.log = ''
		self.log_out = None
		
		self.do_compress = compress
		
	def read_fasta(self, file):
		cur_seq = ""
		cur_prot = ""
		
		contents = {}
		deflines = {}
		
		fasta = agnostic_reader(file)
		for line in fasta:
			if line.startswith(">"):
				if len(cur_seq) > 0:
					contents[cur_prot] = cur_seq
					deflines[cur_prot] = defline
					
				cur_seq = ""
				cur_prot = line.strip().split()[0][1:]
				defline = line.strip()[len(cur_prot)+1 :].strip()
				
			else:
				cur_seq += line.strip()
					
		fasta.close()
		
		#Final iter
		if len(cur_seq) > 0:
			contents[cur_prot] = cur_seq
			deflines[cur_prot] = defline
			
		return contents, deflines

	def get_basename(self, filename):
		if filename.endswith(".gz"):
			#Remove .gz first to make names consistent.
			self.basename = os.path.splitext(os.path.basename(filename[:-3]))[0]
		else:
			self.basename = os.path.splitext(os.path.basename(filename))[0]
		
	def load_genome(self):
		if os.path.exists(self.gen_path):
			self.nt_seqs, self.nt_deflines = self.read_fasta(self.gen_path)
			if self.basename is None:
				self.get_basename(self.gen_path)
			#Only needs to happen if the file is a genome; we already have it for proteins
			self.aa_out = os.path.normpath(self.output + "/predicted_proteins/"+self.basename+".faa.txt")
			self.hmm_out = os.path.normpath(self.output + "/hmms/"+self.basename+".hmm.txt")
			if self.do_nt:
				self.nt_out = os.path.normpath(self.output + "/predicted_proteins_nt/"+self.basename+"_nt.faa.txt")
			self.log_out = os.path.normpath(self.output + "/logs/"+self.basename+"_log.txt")
		else:
			print("Could not find genome file", self.gen_path)
			
	def predict_protein(self):
		pyrod = pyrodigal_manager(input_seqs = self.nt_seqs)
		while len(self.tt) > 0:
			table = self.tt.pop(0)
			
			pyrod.run_pyrod(table, self.aa_out, self.nt_out, self.do_compress)
			
			self.prot_seqs, self.prot_deflines = pyrod.labeled_proteins, pyrod.labeled_deflines
			
			self.log += pyrod.log
		
	def load_protein(self):
		if os.path.exists(self.prot_path):
			if self.prot_seqs is None:
				self.prot_seqs, self.prot_deflines = self.read_fasta(self.prot_path)
			if self.basename is None:
				self.get_basename(self.prot_path)	
			self.hmm_out = os.path.normpath(self.output + "/hmms/"+self.basename+".hmm.txt")
			self.log_out = os.path.normpath(self.output + "/logs/"+self.basename+"_log.txt")
		else:
			print("Could not find protein file", self.prot_path)
		
	def search_hmm(self):
		#this is defined as global already.
		hmm_manager.run(self.prot_seqs, self.prot_deflines, self.hmm_out, self.do_compress)
		self.log += hmm_manager.log
		#Reset the manager's log or it keeps building.
		hmm_manager.log = ''
	
	def make_log(self):
		out = open(self.log_out, "w")
		out.write(self.log)
		out.close()
	
	def run(self):
		if self.gen_path is not None:
			self.load_genome()
			self.predict_protein()
		else:
			self.load_protein()
			
		if self.do_hmm:
			self.search_hmm()
			
		self.make_log()
	
	
class pyhmmer_manager:
	def __init__(self):
		self.hmm_model = []
		self.hmm_model_optimized = None
		
		self.proteins_to_search = []
		self.protein_descriptions = None
		
		self.hmm_result_proteins = []
		self.hmm_result_accessions = []
		self.hmm_result_scores = []
		
		self.printable_lines = []
		
		self.log = ''
		
	#Load HMM and try to optimize.
	def load_hmm_from_file(self, hmm_path):
		hmm_set = pyhmmer.plan7.HMMFile(hmm_path)
		for hmm in hmm_set:
			self.hmm_model.append(hmm)
		
	def optimize_models(self):
		try:
			self.hmm_model_optimized = []
			
			for hmm in self.hmm_model:
				prof = pyhmmer.plan7.Profile(M = hmm.insert_emissions.shape[0], alphabet = pyhmmer.easel.Alphabet.amino())
				prof.configure(hmm = hmm, background = pyhmmer.plan7.Background(alphabet = pyhmmer.easel.Alphabet.amino()), L = hmm.insert_emissions.shape[0]-1)
				optim = prof.optimized()
				self.hmm_model_optimized.append(optim)
				
			#Clean up.
			self.hmm_model = None
		except:
			#Quiet fail condition - fall back on default model.
			self.hmm_model_optimized = None
		

	#Convert passed sequences.
	def convert_protein_seqs_in_mem(self, contents, deflines = None):
		#Clean up.
		self.proteins_to_search = []
		self.protein_descriptions = deflines
		
		for protein in contents:
			#Skip a protein if it's longer than 100k AA.
			if len(contents[protein]) >= 100000:
				self.log += protein + " was longer than 100k nt ("+ str(len(contents[protein])) + " bp) and had to be skipped by PyHMMER\n"
				continue
			as_bytes = protein.encode()
			#Pyhmmer digitization of sequences for searching.
			easel_seq = pyhmmer.easel.TextSequence(name = as_bytes, sequence = contents[protein])
			easel_seq = easel_seq.digitize(pyhmmer.easel.Alphabet.amino())
			self.proteins_to_search.append(easel_seq)
			
		easel_seq = None		
		
	def execute_search(self):
		if self.hmm_model_optimized is None:
			top_hits = list(pyhmmer.hmmsearch(self.hmm_model, self.proteins_to_search, cpus=1, bit_cutoffs="trusted"))
		else:
			top_hits = list(pyhmmer.hmmsearch(self.hmm_model_optimized, self.proteins_to_search, cpus=1, bit_cutoffs="trusted"))
		
		self.printable_lines = []
		
		self.hmm_result_proteins = []
		self.hmm_result_accessions = []
		self.hmm_result_scores = []
		
		for model in top_hits:
			for hit in model:
				target_name = hit.name.decode()
				target_acc = hit.accession
				if target_acc is None:
					target_acc = "-"
				else:
					target_acc = target_acc.decode()
				
				query_name = hit.best_domain.alignment.hmm_name.decode()
				query_acc = hit.best_domain.alignment.hmm_accession.decode()
				
				full_seq_evalue = "%.2g" % hit.evalue
				full_seq_score = round(hit.score, 1)
				full_seq_bias = round(hit.bias, 1)
				
				best_dom_evalue = "%.2g" % hit.best_domain.alignment.domain.i_evalue
				best_dom_score = round(hit.best_domain.alignment.domain.score, 1)
				best_dom_bias = round(hit.best_domain.alignment.domain.bias, 1)

				#I don't know how to get most of these values.
				exp = 0
				reg = 0
				clu = 0
				ov  = 0
				env = 0
				dom = len(hit.domains)
				rep = 0
				inc = 0
				
				try:
					description = self.protein_descriptions[target_name]
				except:
					description = ""
				
				writeout = [target_name, target_acc, query_name, query_acc, full_seq_evalue, \
				full_seq_score, full_seq_bias, best_dom_evalue, best_dom_score, best_dom_bias, \
				exp, reg, clu, ov, env, dom, rep, inc, description]
				
				#Format and join.
				writeout = [str(i) for i in writeout]
				writeout = '\t'.join(writeout)
				
				self.printable_lines.append(writeout)
				
				self.hmm_result_proteins.append(target_name)
				self.hmm_result_accessions.append(query_acc)
				self.hmm_result_scores.append(best_dom_score)
		
	def to_hmm_file(self, output, compress):
		#PyHMMER data is a bit hard to parse. For each result:
		
		content = '\n'.join(self.printable_lines) + '\n'
		
		if compress:
			content = content.encode()
			fh = gzip.open(output+".gz", "wb")
			fh.write(content)
			fh.close()
			content = None
		else:
			fh = open(output, "w")
			fh.write(content)
			fh.close()
			
		content = None
		
	#If we're doing this step at all, we've either loaded the seqs into mem by reading the prot file
	#or have them in mem thanks to pyrodigal.
	def run(self, prots, deflines, hmm_output, do_compress):
		try:
			self.convert_protein_seqs_in_mem(prots, deflines)
			self.execute_search()
			self.to_hmm_file(hmm_output, do_compress)
		except:
			print(output, "cannot be created. HMM search failed. This file will be skipped.")
			self.best_hits = None
		
def hmm_preproc_initializer(hmm_files):
	if hmm_files is not None:
		global hmm_manager
		
		hmm_manager = pyhmmer_manager()
		for file in hmm_files:
			if os.path.exists(file):
				hmm_manager.load_hmm_from_file(file)
			
		hmm_manager.optimize_models()
	
def runner(file):
	file.run()
	
class pyrodigal_manager:
	def __init__(self, input_seqs, is_meta = False):
		self.sequences = input_seqs
		self.convert_seqs()
		#Concatenation of up to first 32 million bp in self.sequences - prodigal caps at this point.
		self.training_seq = None
		
		self.log = ''
		
		#Predicted genes go here
		self.predicted_genes = None
		self.labeled_proteins = None
		self.labeled_deflines = None
		
		#This is the pyrodigal manager - this does the gene predicting.
		self.manager = pyrodigal.OrfFinder(meta=is_meta)
		self.is_meta = is_meta
		
		if not self.is_meta:
			self.get_training_seq()
			
		
	def convert_seqs(self):
		for defline in self.sequences:
			self.sequences[defline] = self.sequences[defline].encode()
			
	#Collect up to the first 32 million bases for use in training seq.
	def get_training_seq(self):
		running_sum = 0
		seqs_added = 0
		if self.training_seq is None:
			self.training_seq = []
			for defline in self.sequences:
				running_sum += len(self.sequences[defline])
				if seqs_added > 0:
					#Prodigal interleaving logic - add this breaker between sequences, starting at sequence 2
					self.training_seq.append(b'TTAATTAATTAA')
					running_sum += 12
					
				seqs_added += 1
					
				#Handle excessive size
				if running_sum >= 32000000:					
					self.log += "Warning:  Sequence is long (max 32000000 for training).\n"
					self.log += "Training on the first 32000000 bases.\n"
				
					to_remove = running_sum - 32000000
					
					#Remove excess characters
					cut_seq = self.sequences[defline][:-to_remove]
					#Add the partial seq
					self.training_seq.append(cut_seq)
					
					#Stop the loop and move to training
					break
				
				#add in a full sequence
				self.training_seq.append(self.sequences[defline])

			if seqs_added > 1:
				self.training_seq.append(b'TTAATTAATTAA')
				
			self.training_seq = b''.join(self.training_seq)
		
		if len(self.training_seq) < 20000:
			self.log += "Can't train on 20 thousand or fewer characters. Switching to meta mode.\n"
			self.manager = pyrodigal.OrfFinder(meta=True)
			self.is_meta = True
		else:
			#G is 71, C is 67; we're counting G + C and dividing by the total.
			gc = round(((self.training_seq.count(67) + self.training_seq.count(71))/ len(self.training_seq)) * 100, 2)
			self.log += str(len(self.training_seq)) + " bp seq created, " + str(gc) + " pct GC\n"
				
	def train_manager(self, table):
		self.log += "Training using translation table " + str(table) + "\n"
		self.manager.train(self.training_seq, translation_table = table)
		
	def predict_genes(self, table):
		if self.is_meta:
			self.log += "Finding genes in metagenomic mode.\n"
		else:
			self.log += "Finding genes with translation table " + str(table) + "\n\n"
			
		self.predicted_genes = {}
		for seq in self.sequences:
			self.log += "Finding genes in sequence " + seq + " ("+str(len(self.sequences[seq]))+ " bp)... "
			self.predicted_genes[seq] = self.manager.find_genes(self.sequences[seq])
			self.log += "done! " + str(len(self.predicted_genes[seq])) + " found!\n"
			
	#Break lines into size base pairs per line. Prodigal's default for bp is 70, aa is 60.
	def num_bp_line_format(self, string, size = 70):
		#ceiling funciton without the math module
		ceiling = int(round((len(string)/size)+0.5, 0))
		formatted = '\n'.join([string[(i*size):(i+1)*size] for i in range(0, ceiling)])
		return formatted
	
	#Writeouts
	def write_results(self, aa_out, nt_out = None, compress = False):
		self.log += "Writing protein sequences... "
		
		aa_content = ''
		nt_content = ''
		
		self.labeled_proteins = {}
		self.labeled_deflines = {}
		
		for seq in self.predicted_genes:
			count = 1
			seqname = ">"+ seq + "_"
			for gene in self.predicted_genes[seq]:
				prot_name = seqname + str(count)
				defline = " # ".join([prot_name, str(gene.begin), str(gene.end), str(gene.strand), str(gene._gene_data)])
				
				if nt_out is not None:
					nt_content += defline
					nt_content += "\n"
					nt_content += self.num_bp_line_format(gene.sequence(), size = 70)
					nt_content += "\n"
				
				aa_content += defline
				aa_content += "\n"
				
				translation = gene.translate()
				self.labeled_proteins[prot_name[1:]] = translation
				self.labeled_deflines[prot_name[1:]] = defline[(len(prot_name)+1):]
				
				aa_content += self.num_bp_line_format(translation, size = 60)
				aa_content += "\n"
				
				count += 1
			
		if compress:
			if nt_out is not None:
				nt_content = nt_content.encode()
				out_writer = gzip.open(nt_out+".gz", "wb")
				out_writer.write(nt_content)
				out_writer.close()
			
			aa_content = aa_content.encode()
			out_writer = gzip.open(aa_out+".gz", "wb")
			out_writer.write(aa_content)
			out_writer.close()

		else:
			if nt_out is not None:
				out_writer = open(nt_out, "w")
				out_writer.write(nt_content)
				out_writer.close()
				
			out_writer = open(aa_out, "w")
			out_writer.write(aa_content)
			out_writer.close()
		
		self.log += "done!\n"
	
	
	def run_pyrod(self, table, aa, nt, comp):
		self.train_manager(table)
		self.predict_genes(table)
		#Comparison from GTDB
		#codingBases += prodigalParser.coding_bases(seq_id)
		#if (table_coding_density[4] - table_coding_density[11] > 0.05) and table_coding_density[4] > 0.7:
		#	best_translation_table = 4
		self.write_results(aa, nt, comp)
		
def options():
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
			description='''''')

	parser.add_argument('-g', '--genomes',  dest = 'genomes', default = None, help =  'A directory containing genomes in FASTA format.')
	parser.add_argument('-p', '--proteins', dest = 'proteins', default = None, help = 'A directory containing protein amino acids in FASTA format.')

	parser.add_argument('-o', '--output',   dest = 'output', default = "FastAAI", help = 'The directory to place the database and any protein or HMM files this program creates. By default, a directory named "FastAAI" will be created in the current working directory and results will be placed there.')
						
	parser.add_argument('--threads',  dest = 'threads', type=int, default = 1, help = 'The number of processors to use. Default 1.')
	parser.add_argument('--compress', dest = "do_comp", action = 'store_true', help = 'Gzip compress generated proteins, HMMs. Off by default.')
	
	parser.add_argument('--trans_table', dest = 'tt', default = "11", help = 'Translation table for proteins. Default 11.')
	parser.add_argument('--meta', dest = 'meta', action = 'store_true', help = 'Run Prodigal in metagenome mode. Default off.')
	parser.add_argument('--nt_too', dest = 'do_nt', action = 'store_true', help = 'Output nucleotide versions of predicted proteins. Only works if proteins are being predicted.')

	parser.add_argument('--hmm_files', dest = 'hmms', default = None, help = 'Comma-sep list of paths to HMMs you want to run. If this is empty, no HMMs can be searched.')
	parser.add_argument('--no_hmms', dest = 'no_hmms', action = 'store_true', help = 'Just predict proteins, no HMMs')
	
	args, unknown = parser.parse_known_args()
	
	return parser, args

def prep_dirs(outdir, do_prots, do_nt, do_hmm):
	if not os.path.exists(outdir):
		os.makedirs(outdir, exist_ok = True)
		
	if do_prots:
		if not os.path.exists(outdir+"/predicted_proteins"):
			os.mkdir(outdir+"/predicted_proteins")
		if do_nt:
			if not os.path.exists(outdir+"/predicted_proteins_nt"):
				os.mkdir(outdir+"/predicted_proteins_nt")
			
	if do_hmm:	
		if not os.path.exists(outdir+"/hmms"):
			os.mkdir(outdir+"/hmms")
		
	if not os.path.exists(outdir+"/logs"):
		os.mkdir(outdir+"/logs")
	
	
def main():
	parser, opts = options()
	genomes, proteins = opts.genomes, opts.proteins
	out = opts.output
	try:
		threads = int(opts.threads)
	except:
		print("Couldn't parse threads defaulting to 1")
		threads = 1
		
	compress_outputs = opts.do_comp
	
	try:
		tt = [int(t) for t in opts.tt.split(",")]
	except:
		print("Couldn't parse trans table option:", tt, "Quitting.")
		
	nt = opts.do_nt
	meta = opts.meta
	
	hmms = opts.hmms
	if hmms is not None:
		hmms = hmms.split(",")
		
	skip_hmm = opts.no_hmms
	
	if hmms is None and not skip_hmm:
		print("No HMM file supplied. Skipping HMM prediction.")
		skip_hmm = True
	
	files = file_importer(genomes = genomes, proteins = proteins, output = out,	
	compress = compress_outputs, do_nt = nt, trans_tables = tt, meta_mode = meta,
	do_hmm = not skip_hmm)
	
	if files.status == "genome":
		prep_dirs(out, True, nt, not skip_hmm)
	
	tracker = progress_tracker(total = len(files.in_files), message = "Predicting proteins and/or searching HMMs")
	
	pool = multiprocessing.Pool(threads, initializer = hmm_preproc_initializer, initargs = (hmms,))
	
	for result in pool.imap_unordered(runner, files.in_files):
		tracker.update()
	
	pool.close()
	
	print("All done.")

	
	
	
if __name__ == "__main__":
	main()
