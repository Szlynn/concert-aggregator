from scraper.sources.registry import SCRAPERS


class ScraperService:
    def run_all(self):
        for scraper in SCRAPERS:
            html = scraper.fetch()
            events = scraper.parse(html)
            # mentés adatbázisba itt
            for event in events:
                print(event)
