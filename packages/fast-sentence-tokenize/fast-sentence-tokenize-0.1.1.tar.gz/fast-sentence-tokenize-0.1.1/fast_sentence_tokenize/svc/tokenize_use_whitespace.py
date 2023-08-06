#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Whitespace Tokenizer """


class TokenizeUseWhitespace(object):
    """ Whitespace Tokenizer """

    def __init__(self):
        """
        Created:
            12-Oct-2021
            craigtrim@gmail.com
        """
        pass

    def process(self,
                input_text: str) -> list:
        return input_text.split()
