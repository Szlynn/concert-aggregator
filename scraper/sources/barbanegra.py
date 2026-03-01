import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://www.barbanegra.hu"
PROGRAMS_URL = f"{BASE_URL}/programok"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


class BarbanegraScraper:
    source_name = "barbanegra"

    def fetch(self) -> str:
        response = requests.get(PROGRAMS_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text

    def parse(self, html: str):
        soup = BeautifulSoup(html, "lxml")

        events = []

        program_boxes = soup.select("div.program-box")

        for box in program_boxes:
            try:
                # ---- DÁTUM ----
                honap = box.select_one(".honap")
                nap = box.select_one(".nap")

                honap_text = honap.get_text(strip=True) if honap else None
                nap_text = nap.get_text(strip=True) if nap else None

                event_date = self._parse_date(honap_text, nap_text)

                # ---- CÍM ----
                title_elem = box.select_one("h2 a")
                title = title_elem.get_text(strip=True) if title_elem else None

                # ---- LINK ----
                relative_url = title_elem["href"] if title_elem else None
                event_url = f"{BASE_URL}/{relative_url}" if relative_url else None

                # ---- JEGYÁR ----
                price_elem = box.select_one(".ar")
                price = price_elem.get_text(strip=True) if price_elem else None

                if not title:
                    continue

                events.append(
                    {
                        "title": title,
                        "event_date": event_date,
                        "event_url": event_url,
                        "price": price,
                        "source": self.source_name,
                    }
                )

            except Exception as e:
                print(f"Hiba egy esemény feldolgozásakor: {e}")
                continue

        return events

    def _parse_date(self, honap: str, nap: str):
        """
        Magyar hónap + nap → datetime.date
        """
        if not honap or not nap:
            return None

        months = {
            "Január": 1,
            "Február": 2,
            "Március": 3,
            "Április": 4,
            "Május": 5,
            "Június": 6,
            "Július": 7,
            "Augusztus": 8,
            "Szeptember": 9,
            "Október": 10,
            "November": 11,
            "December": 12,
        }

        month_number = months.get(honap)
        if not month_number:
            return None

        year = datetime.now().year

        try:
            return datetime(year, month_number, int(nap)).date()
        except ValueError:
            return None
