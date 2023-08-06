from .bp import *
from .svc import *
from .dmo import *
from .dto import *


from .bp.tagger import Tagger

tagapi = Tagger()


def dbpedia_tag(input_text) -> dict:
    return tagapi.process(input_text)
