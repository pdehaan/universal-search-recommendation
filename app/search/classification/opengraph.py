from urllib.parse import urlparse

from .base import BaseClassifier


class OpenGraphClassifier(BaseClassifier):
    """
    Classifier that is applied if the result has Facebook OpenGraph tags in the
    matching document's body. Adds a list of OpenGraph data to the response
    with items that look like this:

    {
        "content": "website",
        "property": "og:type"
    }

    for each different tag.
    """
    type = 'opengraph'

    def is_match(self, result):
        self.og_tags = [t for t in self.document('meta[property^="og:"]') if
                        'property' in t.attrib]
        return len(self.og_tags) > 0

    def enhance(self):
        return [{
            'content': tag.attrib.get('content'),
            'property': tag.attrib.get('property')
        } for tag in self.og_tags]
