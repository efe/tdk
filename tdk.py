import click
import requests
from bs4 import BeautifulSoup


class Word:
    def __init__(self, content):
        self.content = content

        self.make_request()
        self.make_soup()
        self.get_output()

    def __repr__(self):
        return self.content

    def make_request(self):
        url = 'http://www.tdk.gov.tr/index.php?option=com_bts&arama=kelime&guid=TDK.GTS.59a3f56279dcb1.32989506'
        payload = {
            "kelime": self.content,
            "kategori": "verilst",
            "ayn": "tam",
            "gonder": "ARA"
        }
        try:
            response = requests.post(url, data=payload)
        except requests.exceptions.ConnectionError:
            print('internette sorun var.')
            exit()
        self.response = response

    def make_soup(self):
        soup = BeautifulSoup(self.response.text, 'html.parser')
        self.soup = soup

    def get_output(self):
        html = self.soup.find("p", "thomicb")
        try:
            text = html.text.replace('\n', '').strip()
        except AttributeError:
            text = 'kelimeyi bulamadik. :('
        self.text = text


@click.command()
@click.argument('input')
def cli(input):
    """A command line tool to query meaning of Turkish word from official dictionary."""
    word = Word(input)
    click.echo(word.text)

