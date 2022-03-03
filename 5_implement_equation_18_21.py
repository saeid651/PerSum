### This program implements equation 18.21:
###
### q_k = sigma_k_inverse ** tr(U_k) ** q
###
### In our case, "q" is the tf-representation of a sentence.
###
### We generate two output files for each (relevant) input document.
### The first output file contains q_k for each sentence, one sentence per line, k = 200.
### The second output file contains q_k for each sentence, one sentence per line, k = 200,
### computed using sigma_k_inverse and U_k on relevant documents only.


import glob, numpy, os, string


def preprocess(complete_text):
    t = ""
    for c in list(complete_text):
        if c not in string.punctuation:
            t += c
    return t


# Extract names of relevant documents for latter processing
relevant_file = open("relevant_documents", "r")
relevant_files = filter(lambda y: y != "", [x.strip() for x in relevant_file.readlines()])
tot_count_2 = len(relevant_files)
relevant_file.close()


# Extract vocabulary
vocab_file = open("vocabulary_file", "r")
vocab = filter(lambda y: y != "", [x.strip() for x in vocab_file.readlines()])
vocab = [x.split()[1] for x in vocab]
vocab_file.close()


# Extract vocabulary of relevant docs only
vocab_file_r = open("vocabulary_file_relevant_only", "r")
vocab_r = filter(lambda y: y != "", [x.strip() for x in vocab_file_r.readlines()])
vocab_r = [x.split()[1] for x in vocab_r]
vocab_file_r.close()


# Pre-compute multiplier matrix 1
u_T = numpy.transpose(numpy.load("u_k.npy"))
sigma_k_inverse = numpy.diag(numpy.load("Sigma_k_inverse.npy"))
multiplier_matrix = numpy.matrix(sigma_k_inverse) * numpy.matrix(u_T)


# Pre-compute multiplier matrix 2
u_rel_only_T = numpy.transpose(numpy.load("u_k_relevant_only.npy"))
sigma_k_inverse_rel_only = numpy.diag(numpy.load("Sigma_k_inverse_relevant_only.npy"))
multiplier_matrix_rel_only = numpy.matrix(sigma_k_inverse_rel_only) * numpy.matrix(u_rel_only_T)


# Set up output directory 1
outdir = "q_k/"
if not os.path.exists(outdir):
    os.makedirs(outdir)


# Set up output directory 2
outdir_r = "q_k_relevant_only/"
if not os.path.exists(outdir_r):
    os.makedirs(outdir_r)



print "Starting computation ..."



# Actual computation starts here.
all_files = glob.glob("hamshahri_normalized_tokenized/*")
tot_count = len(all_files)


docID_r = 0


for docID, infilename in enumerate(all_files, 1):

    if os.path.basename(infilename).replace(".txt", "") not in relevant_files:
        continue

    else:
        docID_r += 1


    outfile = open(outdir + os.path.basename(infilename), "w")
    outfile_r = open(outdir_r + os.path.basename(infilename), "w")


    infile = open(infilename, "r")
    line = infile.readline()

    while line:

        line = line.strip()
        if len(line) == 0:
            line = infile.readline()
            continue

        complete_text = preprocess(line)
        words = filter(lambda y: y != "", complete_text.split())
        unique_words = list(set(words))

        q = numpy.transpose(numpy.matrix([words.count(word) if word in unique_words else 0 for word in vocab]))
        q_k = numpy.transpose(multiplier_matrix * q).tolist()[0]
        outfile.write(" ".join([str(x) for x in q_k]) + "\n")

        q_rel_only = numpy.transpose(numpy.matrix([words.count(word) if word in unique_words else 0 for word in vocab_r]))
        q_k_rel_only = numpy.transpose(multiplier_matrix_rel_only * q_rel_only).tolist()[0]
        outfile_r.write(" ".join([str(x) for x in q_k_rel_only]) + "\n")

        line = infile.readline()
        # print "one line done"


    infile.close()
    outfile.close()
    outfile_r.close()

    if os.path.basename(infilename).replace(".txt", "") in relevant_files:
        print "Finished", docID_r, "of", tot_count_2, ":  ", os.path.basename(infilename).replace(".txt", "")



