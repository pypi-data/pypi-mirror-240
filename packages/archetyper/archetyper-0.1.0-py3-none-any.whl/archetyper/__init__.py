# -*- coding: utf-8 -*-

import csv
import numpy as np
from tqdm import tqdm
from torch import mean as torchmean
from sentence_transformers import SentenceTransformer, util
from nltk import sent_tokenize


# define a class to hold our archetypes for each construct.

def z_center(input_vector: list) -> list:

    list_mean = sum(input_vector) / len(input_vector)
    list_stdev = sum([((x - list_mean) ** 2) for x in input_vector]) / len(input_vector) ** 0.5

    z_list = [(x - list_mean / list_stdev) for x in input_vector]

    return z_list

def mean_center(input_vector: list) -> list:

    list_mean = sum(input_vector) / len(input_vector)

    centered_list = [x - list_mean for x in input_vector]

    return centered_list


class ArchetypeCollection():

    def __init__(self, ) -> None:
        """
        The collection itself is empty upon initialization
        """
        self.archetype_names = []
        self.archetype_sentences = {}
        #self.archetype_detection_thresholds = {}
        return

    def add_archetype(self, name: str, sentences: list) -> None:
        """

        :param name: The name of the archetype being added
        :param sentences: A list of sentences that are used to represent the archetype
        :param detection_threshold: The cosine similarity value that is used to determine whether a sentence does, versus does not, contain an instantiation of an archetype
        :return:
        """
        # wipe out the existing entries if we already have an archetype by this name
        if name in self.archetype_names:
            self.archetype_names.remove(name)
            self.archetype_sentences.pop(name)

        self.archetype_names.append(name)
        self.archetype_sentences[name] = sentences

        print(f"Archetype added: {name}")

        return


class ArchetypeResult():

    def __init__(self, sentence_text: str, sentence_embedding) -> None:
        self.sentence_text = sentence_text
        self.sentence_embedding = sentence_embedding
        self.error_encountered = False
        self.archetype_scores = {}

        return


# this is the main machine that will do the actual scoring of the texts
class ArchetypeQuantifier():

    def __init__(self, archetypes: ArchetypeCollection, model: str, mean_center_vectors: bool = False) -> None:
        """
        Initialize an instance of the ArchetypeQuantifier class
        :param archetypes: An instance of the Archetype_Collection class
        :param model: The name of the sentence-transformers model that you want to use to quantify archetypes
        :param zcenter: Do you want to z-score the vectors prior to calculating cosine similarity? Probably leave this as False unless you have good reason.
        """
        self.results = []
        self.archetypes = archetypes
        self.model = SentenceTransformer(model)
        self.centered_vec = mean_center_vectors

        # take the archetype sentences and convert each one to an embedding.
        # then, we calculate the average embedding for each archetype construct.
        self.archetype_embeddings = {}
        self.archetype_order = {}

        order_count = 0
        for archetype_construct in self.archetypes.archetype_names:
            self.archetype_embeddings[archetype_construct] = torchmean(input=self.model.encode(
                                                                        sentences=self.archetypes.archetype_sentences[archetype_construct],
                                                                        convert_to_tensor=True),
                                                                        axis=0).tolist()

            if self.centered_vec:
                self.archetype_embeddings[archetype_construct] = mean_center(self.archetype_embeddings[archetype_construct])
            self.archetype_order[order_count] = archetype_construct
            order_count += 1

        print("ArchetypeQuantifier has been successfully instantiated.")

        return

    def evaluate_archetype_consistency(self, ) -> None:
        """
        Print output that shows something like the "internal consistency" of each archetype, based on the prototypical sentences
        :return:
        """

        for archetype_name in self.archetypes.archetype_names:

            print(f"Evaluating {archetype_name}...")

            mean_cos_sim = 0.0

            for i in range(len(self.archetypes.archetype_sentences[archetype_name])):
                archetype_test_sent = [self.archetypes.archetype_sentences[archetype_name][i]]
                archetype_rest_sents = [x for x in self.archetypes.archetype_sentences[archetype_name] if
                                        x != archetype_test_sent]

                archetype_test_embedding = torchmean(self.model.encode(
                    archetype_test_sent,
                    convert_to_tensor=True),
                    axis=0).tolist()

                archetype_rest_embedding = torchmean(self.model.encode(
                    archetype_rest_sents,
                    convert_to_tensor=True),
                    axis=0).tolist()

                if self.centered_vec:
                    archetype_test_embedding = mean_center(archetype_test_embedding)
                    archetype_rest_embedding = mean_center(archetype_rest_embedding)
                    

                cos_sim = float(util.pytorch_cos_sim(archetype_test_embedding,
                                                     archetype_rest_embedding)[0])

                mean_cos_sim += cos_sim / len(self.archetypes.archetype_sentences[archetype_name])

                print(f"\t{round(cos_sim, 5)}: {archetype_test_sent[0]}")

            print("\t--------------------")
            print(f"\t{round(mean_cos_sim, 5)}: Average item-rest cos_sim\n\n")

        return

    def get_list_of_archetypes(self, ) -> list:
        """
        Return a list or the archetype names, in order
        :return:
        """
        archetype_names = []

        for i in range(len(self.archetypes.archetype_names)):
            archetype_names.append(self.archetype_order[i])

        return archetype_names

    def batch_analyze_to_csv(self, texts: list, text_metadata: dict, csv_sent_output_location: str, csv_doc_output_location: str,
                       append_to_existing_csv: bool = False, output_encoding: str = "utf-8-sig"):
        """

        :param texts: a list of texts that you want to analyze
        :param text_metadata: a dictionary where each key is the name of the metadata variable, and the value is a list of metadata items that correspond to the input texts
        :param csv_sent_output_location: path where you want to save a CSV of your sentence-level output
        :param csv_doc_output_location: path where you want to save a CSV of your document-level output
        :param append_to_existing_csv: do you want to append to an existing CSV file?
        :param output_encoding: the file encoding that you want to use to write your CSV files
        :return:
        """

        writemode = 'w'
        if append_to_existing_csv:
            writemode = 'a'

        with open(csv_sent_output_location, writemode, encoding=output_encoding,
                  newline='') as fout_sent, open(csv_doc_output_location, writemode,
                                                 encoding=output_encoding, newline='') as fout_doc:

            csvw_sent = csv.writer(fout_sent)
            csvw_doc = csv.writer(fout_doc)

            meta_headers = list(text_metadata.keys())

            if append_to_existing_csv is False:
                csvw_sent.writerow(self.generate_csv_header_sentence_level(
                    metadata_headers=meta_headers))
                csvw_doc.writerow(self.generate_csv_header_document_level(
                    metadata_headers=meta_headers))

            for i in tqdm(range(len(texts))):

                self.analyze(texts[i])

                meta_output = []

                for meta_item in meta_headers:
                    meta_output.append(text_metadata[meta_item][i])

                csvw_sent.writerows(self.generate_csv_output_sentence_level(
                    input_metadata=meta_output))
                csvw_doc.writerow(self.generate_csv_output_document_level(
                    input_metadata=meta_output))

        return

    def analyze(self, text: str) -> None:
        """
        Takes the input text, segments into sentences, then analyzes each sentence for similarity to each archetype
        :param text:
        :return:
        """

        # take the input text and tokenize into sentences
        sentences = sent_tokenize(text.strip())
        # make sure there are no empty sentences
        sentences = [i for i in sentences if i.strip()]

        # set up a list that will contain our results
        results = []
        error_encountered = False

        sentence_embeddings = None
        try:
            # attempt to convert input sentences to embeddings
            sentence_embeddings = self.model.encode(sentences, convert_to_tensor=True).tolist()
        except:
            print("Error was encountered when trying to embed sentences.")
            error_encountered = True

        # calculate similarity between each sentence and each archetype construct
        for i in range(len(sentences)):

            # set up an ArchetypeResult object to hold our results for this sentence
            archetype_result = ArchetypeResult(sentence_text=sentences[i],
                                               sentence_embedding=None)

            for archetype_construct, archetype_embedding in self.archetype_embeddings.items():

                if error_encountered:
                    # if we encountered an error when trying to create sentence embeddings,
                    # we'll just store the results as empty.
                    archetype_result.archetype_scores[archetype_construct] = None

                else:
                    # otherwise, if everything above went well, we'll calculate the
                    # cosine similarity between the sentence embedding and each archetype embedding...

                    # first, we keep a copy of the sentence embedding
                    archetype_result.sentence_embedding = sentence_embeddings[i]

                    if self.centered_vec:
                        archetype_result.sentence_embedding = mean_center(archetype_result.sentence_embedding)

                    cos_sim = util.pytorch_cos_sim(archetype_embedding,
                                                   archetype_result.sentence_embedding)[0]

                    archetype_result.archetype_scores[archetype_construct] = float(cos_sim)

            archetype_result.error_encountered = error_encountered
            results.append(archetype_result)

        self.results = results

    def get_raw_results(self, ) -> list:
        """
        Returns a list of the class ArchetypeResult, where each element in the list corresponds to each sentence in the input text, in order
        :return:
        """
        return self.results

    def get_results_per_sentence(self, ) -> list:
        """
        Returns a list of the scores for each archetype for each sentence.  Each value is in the same order as the archetype names
        :return:
        """
        results = []
        for result in self.results:
            if not result.error_encountered:
                sentence_result = []
                for i in range(len(self.archetype_order.keys())):
                        sentence_result.append(result.archetype_scores[self.archetype_order[i]])

                results.append(sentence_result)

        return results

    def get_results_text_avgs(self, ) -> float:
        """
        Calculates the average of each archetype across all sentences in the text
        :return:
        """

        sentence_results = self.get_results_per_sentence()

        if len(sentence_results) > 0:
            sentence_results_as_np_array = np.array(sentence_results)
            results_avg = np.average(sentence_results_as_np_array, axis=0).tolist()
        else:
            results_avg = [] * len(self.get_list_of_archetypes())

        return results_avg


    def generate_csv_header_sentence_level(self, metadata_headers: list):
        """
        Helper function to generate a CSV header
        :param metadata_headers: The other headers that will be prepended to your list of archetypes
        :return:
        """
        mh = metadata_headers.copy()
        mh.append("text")
        mh.extend(self.get_list_of_archetypes())
        return mh

    def generate_csv_header_document_level(self, metadata_headers: list):

        header_data_cos_sim = self.get_list_of_archetypes()
        header_data_cos_sim = [x + "_cossim_avg" for x in header_data_cos_sim]

        mh = metadata_headers.copy()
        mh.append("NumSentences")
        mh.extend(header_data_cos_sim)

        return mh

    def generate_csv_output_sentence_level(self, input_metadata: list) -> list:

        sentence_level_results = self.get_results_per_sentence()

        output_data = []

        for i in range(len(sentence_level_results)):
            sentence_level_output_data = []
            sentence_level_output_data.extend(input_metadata)
            sentence_level_output_data.append(self.results[i].sentence_text)
            sentence_level_output_data.extend(sentence_level_results[i])
            output_data.append(sentence_level_output_data)

        return output_data

    def generate_csv_output_document_level(self, input_metadata: list, raw_counts: bool = False) -> list:

        output_data = input_metadata
        output_data.append(str(len(self.results)))
        output_data.extend(self.get_results_text_avgs())

        return output_data

