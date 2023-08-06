
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import Callable


class FinderN2(object):

    __cache = {}

    def _get_finder(self,
                    first_char: str) -> Callable:

        if first_char in self.__cache:
            return self.__cache[first_char]

        if first_char == 'a':
            from dbpedia_ent.dto.n2.a import FinderN2a
            self.__cache[first_char] = FinderN2a().exists

        if first_char == 'b':
            from dbpedia_ent.dto.n2.b import FinderN2b
            self.__cache[first_char] = FinderN2b().exists

        if first_char == 'c':
            from dbpedia_ent.dto.n2.c import FinderN2c
            self.__cache[first_char] = FinderN2c().exists

        if first_char == 'd':
            from dbpedia_ent.dto.n2.d import FinderN2d
            self.__cache[first_char] = FinderN2d().exists

        if first_char == 'e':
            from dbpedia_ent.dto.n2.e import FinderN2e
            self.__cache[first_char] = FinderN2e().exists

        if first_char == 'f':
            from dbpedia_ent.dto.n2.f import FinderN2f
            self.__cache[first_char] = FinderN2f().exists

        if first_char == 'g':
            from dbpedia_ent.dto.n2.g import FinderN2g
            self.__cache[first_char] = FinderN2g().exists

        if first_char == 'h':
            from dbpedia_ent.dto.n2.h import FinderN2h
            self.__cache[first_char] = FinderN2h().exists

        if first_char == 'i':
            from dbpedia_ent.dto.n2.i import FinderN2i
            self.__cache[first_char] = FinderN2i().exists

        if first_char == 'j':
            from dbpedia_ent.dto.n2.j import FinderN2j
            self.__cache[first_char] = FinderN2j().exists

        if first_char == 'k':
            from dbpedia_ent.dto.n2.k import FinderN2k
            self.__cache[first_char] = FinderN2k().exists

        if first_char == 'l':
            from dbpedia_ent.dto.n2.l import FinderN2l
            self.__cache[first_char] = FinderN2l().exists

        if first_char == 'm':
            from dbpedia_ent.dto.n2.m import FinderN2m
            self.__cache[first_char] = FinderN2m().exists

        if first_char == 'n':
            from dbpedia_ent.dto.n2.n import FinderN2n
            self.__cache[first_char] = FinderN2n().exists

        if first_char == 'o':
            from dbpedia_ent.dto.n2.o import FinderN2o
            self.__cache[first_char] = FinderN2o().exists

        if first_char == 'p':
            from dbpedia_ent.dto.n2.p import FinderN2p
            self.__cache[first_char] = FinderN2p().exists

        if first_char == 'q':
            from dbpedia_ent.dto.n2.q import FinderN2q
            self.__cache[first_char] = FinderN2q().exists

        if first_char == 'r':
            from dbpedia_ent.dto.n2.r import FinderN2r
            self.__cache[first_char] = FinderN2r().exists

        if first_char == 's':
            from dbpedia_ent.dto.n2.s import FinderN2s
            self.__cache[first_char] = FinderN2s().exists

        if first_char == 't':
            from dbpedia_ent.dto.n2.t import FinderN2t
            self.__cache[first_char] = FinderN2t().exists

        if first_char == 'u':
            from dbpedia_ent.dto.n2.u import FinderN2u
            self.__cache[first_char] = FinderN2u().exists

        if first_char == 'v':
            from dbpedia_ent.dto.n2.v import FinderN2v
            self.__cache[first_char] = FinderN2v().exists

        if first_char == 'w':
            from dbpedia_ent.dto.n2.w import FinderN2w
            self.__cache[first_char] = FinderN2w().exists

        if first_char == 'x':
            from dbpedia_ent.dto.n2.x import FinderN2x
            self.__cache[first_char] = FinderN2x().exists

        if first_char == 'y':
            from dbpedia_ent.dto.n2.y import FinderN2y
            self.__cache[first_char] = FinderN2y().exists

        if first_char == 'z':
            from dbpedia_ent.dto.n2.z import FinderN2z
            self.__cache[first_char] = FinderN2z().exists

        if first_char in self.__cache:
            return self.__cache[first_char]

    def exists(self,
               input_text: str) -> bool:

        input_text = input_text.lower()
        finder = self._get_finder(input_text[0])
        return finder(input_text)
