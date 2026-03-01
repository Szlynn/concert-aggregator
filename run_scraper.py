from scraper.sources.barbanegra import BarbanegraScraper


def main():
    import pdb

    pdb.set_trace()
    scraper = BarbanegraScraper()
    html = scraper.fetch()
    events = scraper.parse(html)

    for event in events:
        print(event)


if __name__ == "__main__":
    main()
