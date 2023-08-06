from kbbi_scraper import constants, utils

from functools import cached_property
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--headless")

import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

class Word:
    def __init__(self, word):
        self.input_word = word
        self.url = f'{constants.SOURCE_URL}/{word}'

    def __repr__(self):
        return self.input_word
    
    @cached_property
    def soup(self):
        bowl = utils.load_soup_bowl()
        
        if self.input_word in bowl:
            return BeautifulSoup(bowl[self.input_word], 'html.parser')
        else:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get(self.url)
            try:
                element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
                soup = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
                self.driver.close()


                # Clean and store fetched html locally
                for ads in soup.find_all('script'):
                    ads.decompose()

                for ads in soup.find_all('ins'):
                    ads.decompose()

                bowl[self.input_word] = soup.decode()
                utils.dump_soup_bowl(bowl)
                return soup
            except TimeoutException:
                print("Failed to load web source")

    @cached_property
    def desc_section(self):
        return self.soup.find('div', {'id': 'desc'})

    @cached_property
    def d1_section(self):
        return self.soup.find('div', {'id': 'd1'})

    @cached_property
    def base_word(self) -> str:
        return ''.join(self.syllables)

    @cached_property
    def word(self) -> str:
        if (self.d1_section.select_one('b.mjk') and self.d1_section.select_one('b.mjk').parent == self.d1_section):
            return self.d1_section.select_one('b.mjk').next_element.text.replace('--', self.base_word).title()
        else:
            return self.syllables

    @cached_property
    def syllables(self) -> list:
        try:
            syllable = self.d1_section.select_one('span.per-suku').text.strip('/').strip('\\')
        except AttributeError:
            syllable = self.d1_section.find('b', {'class': 'highlight'}).text.strip('/').strip('\\')
        
        try:
            word_number = self.d1_section.find('b').find('sup').text
            return syllable.replace(word_number, '').split('·')
        except AttributeError:
            return syllable.split('·')

    @cached_property
    def definition(self) -> list:
        meaning = []
        for num in self.d1_section.find_all_next('b', {'class': 'num'}):
            # Cuma nomor yang ada di div d1 section, yang ada didalem div sub_17 skip
            if num.parent == self.d1_section:

                # Arti dari peribahasa jangan dibawa, itu untuk property peribahasa
                if num.find_previous('em', {'class': 'pb'}):
                    continue
    
                if num.text == "1":
                    category = constants.CATEGORY[self.d1_section.find_next('em', {'class': 'jk'}).text.lower()]
                    m = num.next_element.next_element
                else:
                    category = constants.CATEGORY[num.find_next('em', {'class': 'jk'}).text.lower()] or constants.CATEGORY[self.d1_section.find_next('em', {'class': 'jk'}).text.lower()]

                    # Check if word is in the same category as the previous word
                    if category == constants.CATEGORY[self.d1_section.find_next('em', {'class': 'jk'}).text.lower()]:
                        m = num.next_element.next_element
                    else:
                        m = num.select_one('em.jk').next_element.next_element

                m_formatted = m.text.strip().strip(';').strip(':').capitalize()
                if (', ' in m_formatted and m.next_element == m.find_next_sibling('em')):
                    m_formatted.replace(',', '')
                    m_formatted += f"({m.find_next_sibling('em').text})"
                    
                meaning.append({
                    'meaning': m_formatted,
                    'category': category,
                    'example': m.find_next('em').text.replace('--', m_formatted).strip().strip(';').capitalize() if m.text.strip().endswith(':') else None
                })
            
        if not len(meaning):
            if (self.d1_section.select_one('b.mjk') and self.d1_section.select_one('b.mjk').parent == self.d1_section):
                m = self.d1_section.select_one('b.mjk').next_element.next_element
            else:
                m = self.d1_section.select_one('em.jk').next_element.next_element

            m_formatted = m.text.strip().strip(';').strip(':').capitalize()

            if (',' in m_formatted and m.next_element == m.find_next_sibling('em')):
                m_formatted += f"({m.find_next_sibling('em').text})"
                m_formatted = m_formatted.replace(',', '').strip()
                
            meaning.append(
                {
                    'meaning': m_formatted,
                    'category': constants.CATEGORY[self.d1_section.select_one('em.jk').text.lower()],
                    'example': None
                }
            )
        return meaning
    
    @cached_property
    def related_words(self):
        related_words = []

        for related_word in self.soup.select_one('div#word div#w1 ul#u1').find_all('li'):
            link = related_word.find_next('a')
            if 'cur' in link['class']:
                continue

            related_words.append(Word(link.get('href').lstrip('./')))

        for related_word in self.soup.select_one('div#word div#w2 ul#u2').find_all('li'):
            related_words.append(Word(related_word.find_next('a').get('href').lstrip('./')))

        return related_words

    @cached_property
    def pribahasa(self) -> list:
        meaning = []
        # Cari tag em dengan class pb untuk pribahasa
        for pb in self.d1_section.select("em.pb"):
            mean = []
            pb_text = ''
            # looping jika next element adalah tag b dengan class num, itu berarti pribahasa memiliki lebih dari 1 arti
            if 'class' in pb.next_sibling.next_sibling.attrs and 'num' in pb.next_sibling.next_sibling['class']:
                for num in pb.find_all_next('b', {'class': 'num'}):
                    mean.append(self._format_string(num.next_sibling))
            
            if not len(mean):
                mean.append(self._format_string(pb.next_sibling).split(';')[0])

            if '--' in pb.previous_sibling:
                previous_pb = [ex for ex in (pb.previous_sibling.split(';') if ':' not in pb.previous_sibling else pb.previous_sibling.split(':')) if '--' in ex][0]
                pb_text = f'{previous_pb} {pb.text}'

            if not pb_text:
                pb_text = pb.text

            meaning.append(
                {
                    'meaning': mean,
                    'pribahasa': [ex for ex in self._format_pribahasa(pb_text).split(';') if self.word in ex ][0]
                }
            )

        return meaning

    def _format_pribahasa(self, str) -> str:
       return str.strip().replace('--', self.word).replace(', pb', '')

    def _format_string(self, str) -> str:
        return str.strip().strip(';').strip(':').capitalize()
            
    def _is_already_in_bowl(self):
        return self.input_word in utils.load_soup_bowl()