
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import Callable


class Finder(object):

    __cache = {}

    def _get_finder(self,
                    input_text: str) -> Callable:

        gram_level = input_text.count('_')

        if gram_level in self.__cache:
            return self.__cache[gram_level]

        elif gram_level == 0:
            from dbpedia_ent.svc import FinderN1
            self.__cache[gram_level] = FinderN1().exists

        elif gram_level == 1:
            from dbpedia_ent.svc import FinderN2
            self.__cache[gram_level] = FinderN2().exists

        elif gram_level == 2:
            from dbpedia_ent.svc import FinderN3
            self.__cache[gram_level] = FinderN3().exists

        elif gram_level > 2:
            raise NotImplementedError(gram_level)

        return self.__cache[gram_level]

    def exists(self,
               input_text: str) -> bool:
        input_text = input_text.lower().replace(' ', '_')
        finder = self._get_finder(input_text)
        return finder(input_text)
