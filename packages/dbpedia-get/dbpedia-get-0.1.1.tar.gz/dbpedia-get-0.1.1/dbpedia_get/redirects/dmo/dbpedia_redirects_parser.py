#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Parse the large Redirects file downloaded from dbPedia's site """


import pandas as pd
from pandas import DataFrame

from tabulate import tabulate

from baseblock import BaseObject
from baseblock import Stopwatch


class DBpediaRedirectsParser(BaseObject):
    """ Parse the large Redirects file downloaded from dbPedia's site """

    def __init__(self,
                 input_file: str):
        """ Change Log

        Created:
            14-Jul-2022
            craigtrim@gmail.com
            *   https://github.com/craigtrim/dbpedia/issues/1

        Args:
            input_file (str): _description_
        """
        BaseObject.__init__(self, __name__)
        self._input_file = input_file

    @staticmethod
    def _is_valid(input_text: str or None) -> bool:
        if not input_text or input_text is None or not len(input_text):
            return False
        # if '%' in input_text:
        #     return False
        # if '(' in input_text or ')' in input_text:
        #     return False
        return input_text.replace('_', '').isalpha()

    def _to_list(self) -> list:
        """ Sample Input
            <http://dbpedia.org/resource/Astable> <http://dbpedia.org/ontology/wikiPageRedirects> <http://dbpedia.org/resource/Multivibrator> .
        """
        results = []

        def read_file():
            """
            Process the file line by line using the file's returned iterator
            """
            try:
                with open(self._input_file) as file_handler:
                    while True:
                        yield next(file_handler)
            except (IOError, OSError):
                self.logger.error('\n'.join([
                    "Error opening / processing file",
                    f"\tInput File: {self._input_file}"]))
            except StopIteration:
                pass

        ctr = 0
        sw = Stopwatch()

        for line in read_file():

            tokens = [x.split('/')[-1].split('>')[0].strip()
                      for x in line.split(' ')]

            tokens = [tokens[0], tokens[2]]
            tokens = [x.strip() for x in tokens]

            if len(tokens) != 2:
                continue

            variant = tokens[0].strip().lower()
            if not self._is_valid(variant):
                continue

            canon = tokens[1].strip().lower()
            if not self._is_valid(canon):
                continue

            canon = canon.replace('_', ' ')
            variant = variant.replace('_', ' ')

            if canon == variant:
                continue

            results.append({"Canon": canon,
                            "Variant": variant})

            ctr += 1
            if ctr % 1000000 == 0:
                self.logger.debug(f"Status {ctr} in {str(sw)}")
                sw = Stopwatch()

        return results

    def _to_dataframe(self,
                      results: list) -> DataFrame:
        sw = Stopwatch()
        results = self._to_list()

        df = pd.DataFrame(results)
        df = df.sort_values(by=['Canon'], ascending=True)

        if self.isEnabledForDebug:
            self.logger.debug('\n'.join([
                "Redirects File Parsing Completed",
                f"\tTotal Size: {len(df)}",
                f"\tTotal Time: {str(sw)}",
                tabulate(df.sample(5),
                         tablefmt='psql',
                         headers='keys')]))

        return df

    def process(self) -> DataFrame:
        return self._to_dataframe(self._to_list())
