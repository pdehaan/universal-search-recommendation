from .domain import DomainClassifier
from .embedly import EmbedlyClassifier
from .wikipedia import WikipediaClassifier


CLASSIFIERS = [
    DomainClassifier,
    EmbedlyClassifier,
    WikipediaClassifier,
]
