# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com), Florian Boudin, Seon
@description:

YAKE(Yet Another Keyword Extractor)，一种基于关键词统计的单文档无监督关键词提取算法：
基于5种指标：是否大写，词的位置，词频，上下文关系，词在句中频率，来计算候选词的得分，从而筛选Top-N关键词。
中文只用后4个指标。
关键词的基本过滤规则：1）候选短语限制最长三个词；2）候选短语不能是专名；3）候选短语开头和结尾不能是停用词

YAKE keyphrase extraction model.

Statistical approach to keyphrase extraction described in:

* Ricardo Campos, Vítor Mangaravite, Arian Pasquali, Alípio Mário Jorge,
  Célia Nunes and Adam Jatowt.
  YAKE! Keyword extraction from single documents using multiple local features.
  *Information Sciences*, pages 257-289, 2020.

modify from: https://pypi.org/project/iyake-cn/0.5.5/#files

"""

import math
from collections import defaultdict
import numpy as np
from pke_zh.utils.text_utils import edit_distance
from pke_zh.base import BaseKeywordExtractModel


class Yake(BaseKeywordExtractModel):
    """YAKE keyphrase extraction model."""

    def __init__(self):
        """Redefining initializer for YAKE.
        """
        super(Yake, self).__init__()
        self.words = defaultdict(set)
        """ Container for the vocabulary. """

        self.contexts = defaultdict(lambda: ([], []))
        """ Container for word contexts. """

        self.features = defaultdict(dict)
        """ Container for word features. """

        self.surface_to_lexical = {}
        """ Mapping from surface form to lexical form. """

    def candidate_selection(self, n=3):
        """Select 1-3 grams as keyphrase candidates. Candidates beginning or
        ending with a stopword are filtered out. Words that do not contain
        at least one alpha-numeric character are not allowed.

        Args:
            n (int): the n-gram length, defaults to 3.
        """
        # select ngrams from 1 to 3 grams
        self.ngram_selection(n=n)

        # filter candidates containing punctuation marks and stopwords
        self.candidate_filtering(stoplist=self.stoplist)

        # further filter candidates
        for k in list(self.candidates):
            # get the candidate
            v = self.candidates[k]

            # filter candidates starting/ending with a stopword
            if v.surface_forms[0][0].lower() in self.stoplist or v.surface_forms[0][
                -1].lower() in self.stoplist:
                del self.candidates[k]

    def _vocabulary_building(self):
        """Build the vocabulary that will be used to weight candidates. Only
        words containing at least one alpha-numeric character are kept.
        """
        # loop through sentences
        for i, sentence in enumerate(self.sentences):
            # compute the offset shift for the sentence
            shift = sum([s.length for s in self.sentences[0:i]])
            # loop through words in sentence
            for j, word in enumerate(sentence.words):
                # consider words containing at least one character
                if len(word) > 1:
                    # get the word
                    index = word.lower()
                    # add the word occurrence
                    self.words[index].add((shift + j, shift, i, word))

    def _contexts_building(self, window=2):
        """Build the contexts of the words for computing the relatedness
        feature. Words that occur within a window of n words are considered as
        context words. Only words co-occurring in a block (sequence of words
        that appear in the vocabulary) are considered.

        Args:
            use_stems (bool): whether to use stems instead of lowercase words
                for weighting, defaults to False.
            window (int): the size in words of the window used for computing
                co-occurrence counts, defaults to 2.
        """
        # loop through sentences
        for i, sentence in enumerate(self.sentences):
            # lowercase the words
            words = [w.lower() for w in sentence.words]
            # block container
            block = []
            # loop through words in sentence
            for j, word in enumerate(words):
                # skip and flush block if word is not in vocabulary
                if word not in self.words:
                    block = []
                    continue
                # add the left context
                self.contexts[word][0].extend(
                    [w for w in block[max(0, len(block) - window):len(block)]]
                )
                # add the right context
                for w in block[max(0, len(block) - window):len(block)]:
                    self.contexts[w][1].append(word)
                # add word to the current block
                block.append(word)

    def _feature_extraction(self):
        """Compute the weight of individual words using the following five
        features:

            1. CASING: gives importance to acronyms or words starting with a
               capital letter.

               CASING(w) = max(TF(U(w)), TF(A(w))) / (1 + log(TF(w)))

               with TF(U(w) being the # times the word starts with an uppercase
               letter, excepts beginning of sentences. TF(A(w)) is the # times
               the word is marked as an acronym.

            2. POSITION: gives importance to words occurring at the beginning of
               the document.

               POSITION(w) = log( log( 3 + Median(Sen(w)) ) )

               with Sen(w) contains the position of the sentences where w
               occurs.

            3. FREQUENCY: gives importance to frequent words.

               FREQUENCY(w) = TF(w) / ( MEAN_TF + STD_TF)

               with MEAN_TF and STD_TF computed on valid_tfs which are words
               that are not stopwords.

            4. RELATEDNESS: gives importance to words that do not have the
               characteristics of stopwords.

               RELATEDNESS(w) = 1 + (WR+WL)*(TF(w)/MAX_TF) + PL + PR

            5. DIFFERENT: gives importance to words that occurs in multiple
               sentences.

               DIFFERENT(w) = SF(w) / # sentences

               with SF(w) being the sentence frequency of word w.
        """
        # get the Term Frequency of each word
        TF = [len(self.words[w]) for w in self.words]

        # get the Term Frequency of non-stop words
        TF_nsw = [len(self.words[w]) for w in self.words if w not in self.stoplist]

        # compute statistics
        mean_TF = np.mean(TF_nsw)
        std_TF = np.std(TF_nsw)
        max_TF = max(TF)

        # Loop through the words
        for word in self.words:
            # Indicating whether the word is a stopwords
            self.features[word]['isstop'] = word in self.stoplist

            # Term Frequency
            self.features[word]['TF'] = len(self.words[word])

            # Uppercase/Acronym Term Frequencies
            self.features[word]['TF_A'] = 0
            self.features[word]['TF_U'] = 0
            for (offset, shift, sent_id, surface_form) in self.words[word]:
                if surface_form.isupper() and len(word) > 1:
                    self.features[word]['TF_A'] += 1
                elif surface_form[0].isupper() and offset != shift:
                    self.features[word]['TF_U'] += 1

            # 1. CASING feature, chinese text continue
            self.features[word]['CASING'] = max(self.features[word]['TF_A'],
                                                self.features[word]['TF_U'])
            self.features[word]['CASING'] /= 1.0 + math.log(self.features[word]['TF'])

            # 2. POSITION feature
            sentence_ids = list(set([t[2] for t in self.words[word]]))
            self.features[word]['POSITION'] = math.log(3.0 + np.median(sentence_ids))
            self.features[word]['POSITION'] = math.log(self.features[word]['POSITION'])

            # 3. FREQUENCY feature
            self.features[word]['FREQUENCY'] = self.features[word]['TF']
            self.features[word]['FREQUENCY'] /= (mean_TF + std_TF)

            # 4. RELATEDNESS feature
            self.features[word]['WL'] = 0.0
            if len(self.contexts[word][0]):
                self.features[word]['WL'] = len(set(self.contexts[word][0]))
                self.features[word]['WL'] /= len(self.contexts[word][0])
            self.features[word]['PL'] = len(set(self.contexts[word][0])) / max_TF

            self.features[word]['WR'] = 0.0
            if len(self.contexts[word][1]):
                self.features[word]['WR'] = len(set(self.contexts[word][1]))
                self.features[word]['WR'] /= len(self.contexts[word][1])
            self.features[word]['PR'] = len(set(self.contexts[word][1])) / max_TF

            self.features[word]['RELATEDNESS'] = 1
            self.features[word]['RELATEDNESS'] += (self.features[word]['WR'] +
                                                   self.features[word]['WL']) * \
                                                  (self.features[word]['TF'] / max_TF)

            # 5. DIFFERENT feature
            self.features[word]['DIFFERENT'] = len(set(sentence_ids))
            self.features[word]['DIFFERENT'] /= len(self.sentences)

            # assemble the features to weight words
            A = self.features[word]['CASING']
            B = self.features[word]['POSITION']
            C = self.features[word]['FREQUENCY']
            D = self.features[word]['RELATEDNESS']
            E = self.features[word]['DIFFERENT']
            self.features[word]['weight'] = (D * B) / (A + (C / D) + (E / D))

    def clear_cache(self):
        # clear previous cache
        self.words = defaultdict(set)
        self.contexts = defaultdict(lambda: ([], []))
        self.features = defaultdict(dict)
        self.surface_to_lexical = {}

    def candidate_weighting(self, window=2):
        """Candidate weight calculation as described in the YAKE paper.

        Args:
            window (int): the size in words of the window used for computing
                co-occurrence counts, defaults to 2.
        """
        if not self.candidates:
            return

        # build the vocabulary
        self._vocabulary_building()

        # extract the contexts
        self._contexts_building(window=window)

        # compute the word features
        self._feature_extraction()

        # compute candidate weights
        for k, v in self.candidates.items():
            lowercase_forms = [' '.join(t).lower() for t in v.surface_forms]
            for i, candidate in enumerate(lowercase_forms):
                TF = lowercase_forms.count(candidate)

                # computing differentiated weights for words and stopwords
                tokens = [t.lower() for t in v.surface_forms[i]]
                prod_ = 1.
                sum_ = 0.
                for j, token in enumerate(tokens):
                    if self.features[token]['isstop']:
                        term_stop = token
                        prob_t1 = 0
                        prob_t2 = 0
                        if j - 1 >= 0:
                            term_left = tokens[j - 1]
                            prob_t1 = self.contexts[term_left][1].count(
                                term_stop) / self.features[term_left]['TF']
                        if j + 1 < len(tokens):
                            term_right = tokens[j + 1]
                            prob_t2 = self.contexts[term_stop][0].count(
                                term_right) / self.features[term_right]['TF']

                        prob = prob_t1 * prob_t2
                        prod_ *= (1 + (1 - prob))
                        sum_ -= (1 - prob)
                    else:
                        prod_ *= self.features[token]['weight']
                        sum_ += self.features[token]['weight']
                if sum_ == -1:
                    # The candidate is a one token stopword at the start or
                    #  the end of the sentence
                    # Setting sum_ to -1+eps so 1+sum_ != 0
                    sum_ = -0.99999999999
                self.weights[candidate] = prod_
                self.weights[candidate] /= TF * (1 + sum_)
                self.surface_to_lexical[candidate] = k

    def is_redundant(self, candidate, prev, threshold=0.6):
        """Test if one candidate is redundant with respect to a list of already
        selected candidates. A candidate is considered redundant if its
        levenshtein distance, with another candidate that is ranked higher in
        the list, is greater than a threshold.

        Args:
            candidate (str): the lexical form of the candidate.
            prev (list): the list of already selected candidates.
            threshold (float): the threshold used when computing the
                    char sim score, defaults to 0.6.
        """
        # loop through the already selected candidates
        for prev_candidate in prev:
            dist = edit_distance(prev_candidate, candidate)
            sim_score = 1.0 - dist
            if sim_score >= threshold:
                return True
        return False

    def get_n_best(
            self,
            n=10,
            redundancy_removal=True,
            threshold=0.6
    ):
        """ Returns the n-best candidates given the weights.

            Args:
                n (int): the number of candidates, defaults to 10.
                redundancy_removal (bool): whether redundant keyphrases are
                    filtered out from the n-best list using levenshtein
                    distance, defaults to True.
                threshold (float): the threshold used when computing the
                    char sim score, defaults to 0.6.
        """
        # sort candidates by ascending weight, change dict to key list
        best = sorted(self.weights, key=self.weights.get, reverse=True)

        # remove redundant candidates
        if redundancy_removal:
            # initialize a new container for non redundant candidates
            non_redundant_best = []
            # loop through the best candidates
            for candidate in best:
                # test weather candidate is redundant
                if self.is_redundant(candidate,
                                     non_redundant_best,
                                     threshold=threshold):
                    continue
                # add the candidate otherwise
                non_redundant_best.append(candidate)
                # break computation if the n-best are found
                if len(non_redundant_best) >= n:
                    break
            # copy non redundant candidates in best container
            best = non_redundant_best

        # get the list of best candidates as (lexical form, weight) tuples
        n_best = [(u.replace(' ', ''), self.weights[u]) for u in best[:min(n, len(best))]]
        # return the list of best candidates
        return n_best

    def extract(self, input_file_or_string, n_best=10, threshold=0.6, window=2):
        keyphrases = []
        if not input_file_or_string:
            return keyphrases
        # load the content of the document.
        self.load_document(input=input_file_or_string, language='zh', normalization=None)
        self.clear_cache()
        # select {1-3}-grams not containing punctuation marks and not
        #    beginning/ending with a stop word as candidates.
        self.candidate_selection(n=3)
        if not self.candidates:
            return keyphrases
        # weight the candidates using YAKE weighting scheme, a window (in
        #    words) for computing left/right contexts can be specified.
        self.candidate_weighting(window=window)
        # Get the 10-highest scored candidates as keyphrases.
        #    redundant keyphrases are removed from the output using levenshtein
        #    distance and a threshold.
        keyphrases = self.get_n_best(n=n_best, threshold=threshold)
        return keyphrases
