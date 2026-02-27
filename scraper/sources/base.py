class BaseScraper:
    source_name: str

    def fetch(self):
        raise NotImplementedError

    def parse(self, html: str):
        raise NotImplementedError

    def run(self):
        html = self.fetch()
        return self.parse(html)