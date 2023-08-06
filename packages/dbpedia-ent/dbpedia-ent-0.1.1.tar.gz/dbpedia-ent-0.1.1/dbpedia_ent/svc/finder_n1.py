
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import Callable


class FinderN1(object):

    __cache = {}

    def _get_finder(self,
                    first_char: str) -> Callable:

        if first_char in self.__cache:
            return self.__cache[first_char]

        if first_char == 'a':
            from dbpedia_ent.dto.n1.a import FinderN1a
            self.__cache[first_char] = FinderN1a().exists

        if first_char == 'b':
            from dbpedia_ent.dto.n1.b import FinderN1b
            self.__cache[first_char] = FinderN1b().exists

        if first_char == 'c':
            from dbpedia_ent.dto.n1.c import FinderN1c
            self.__cache[first_char] = FinderN1c().exists

        if first_char == 'd':
            from dbpedia_ent.dto.n1.d import FinderN1d
            self.__cache[first_char] = FinderN1d().exists

        if first_char == 'e':
            from dbpedia_ent.dto.n1.e import FinderN1e
            self.__cache[first_char] = FinderN1e().exists

        if first_char == 'f':
            from dbpedia_ent.dto.n1.f import FinderN1f
            self.__cache[first_char] = FinderN1f().exists

        if first_char == 'g':
            from dbpedia_ent.dto.n1.g import FinderN1g
            self.__cache[first_char] = FinderN1g().exists

        if first_char == 'h':
            from dbpedia_ent.dto.n1.h import FinderN1h
            self.__cache[first_char] = FinderN1h().exists

        if first_char == 'i':
            from dbpedia_ent.dto.n1.i import FinderN1i
            self.__cache[first_char] = FinderN1i().exists

        if first_char == 'j':
            from dbpedia_ent.dto.n1.j import FinderN1j
            self.__cache[first_char] = FinderN1j().exists

        if first_char == 'k':
            from dbpedia_ent.dto.n1.k import FinderN1k
            self.__cache[first_char] = FinderN1k().exists

        if first_char == 'l':
            from dbpedia_ent.dto.n1.l import FinderN1l
            self.__cache[first_char] = FinderN1l().exists

        if first_char == 'm':
            from dbpedia_ent.dto.n1.m import FinderN1m
            self.__cache[first_char] = FinderN1m().exists

        if first_char == 'n':
            from dbpedia_ent.dto.n1.n import FinderN1n
            self.__cache[first_char] = FinderN1n().exists

        if first_char == 'o':
            from dbpedia_ent.dto.n1.o import FinderN1o
            self.__cache[first_char] = FinderN1o().exists

        if first_char == 'p':
            from dbpedia_ent.dto.n1.p import FinderN1p
            self.__cache[first_char] = FinderN1p().exists

        if first_char == 'q':
            from dbpedia_ent.dto.n1.q import FinderN1q
            self.__cache[first_char] = FinderN1q().exists

        if first_char == 'r':
            from dbpedia_ent.dto.n1.r import FinderN1r
            self.__cache[first_char] = FinderN1r().exists

        if first_char == 's':
            from dbpedia_ent.dto.n1.s import FinderN1s
            self.__cache[first_char] = FinderN1s().exists

        if first_char == 't':
            from dbpedia_ent.dto.n1.t import FinderN1t
            self.__cache[first_char] = FinderN1t().exists

        if first_char == 'u':
            from dbpedia_ent.dto.n1.u import FinderN1u
            self.__cache[first_char] = FinderN1u().exists

        if first_char == 'v':
            from dbpedia_ent.dto.n1.v import FinderN1v
            self.__cache[first_char] = FinderN1v().exists

        if first_char == 'w':
            from dbpedia_ent.dto.n1.w import FinderN1w
            self.__cache[first_char] = FinderN1w().exists

        if first_char == 'x':
            from dbpedia_ent.dto.n1.x import FinderN1x
            self.__cache[first_char] = FinderN1x().exists

        if first_char == 'y':
            from dbpedia_ent.dto.n1.y import FinderN1y
            self.__cache[first_char] = FinderN1y().exists

        if first_char == 'z':
            from dbpedia_ent.dto.n1.z import FinderN1z
            self.__cache[first_char] = FinderN1z().exists

        if first_char not in self.__cache:
            raise ValueError(first_char)

        return self.__cache[first_char]

    def exists(self,
               input_text: str) -> bool:

        input_text = input_text.lower()
        unigram_finder = self._get_finder(input_text[0])
        return unigram_finder(input_text)
