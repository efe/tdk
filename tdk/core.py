from requests_html import HTMLSession

from tdk.constants import QUERY_URL


class TurkishWord:
    def __init__(self, term):
        self.term = term
        self.response = None

    def __repr__(self):
        return self.term

    def query(self):
        session = HTMLSession()

        payload = {
            "kelime": self.term,
            "kategori": "verilst",
            "ayn": "tam",
            "gonder": "ARA"
        }

        self.response = session.post(QUERY_URL, data=payload)
        session.close()

    @property
    def meaning(self):
        try:
            result = self.response.html.find('.thomicb', first=True).text
            result = result.replace('\n', '').strip()
            return result
        except AttributeError:
            from tdk.exceptions import WordNotFoundException
            raise WordNotFoundException()
