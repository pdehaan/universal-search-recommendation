from .domain import DomainClassifier
from .opengraph import OpenGraphClassifier
from .wikipedia import WikipediaClassifier


CLASSIFIERS = [
    DomainClassifier,
    OpenGraphClassifier,
    WikipediaClassifier
]
