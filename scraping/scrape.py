from bs4 import BeautifulSoup
from language import Language

def scrape_esl_page(language: Language):
    assert language in [member for member in Language], "Language not supported!"
    print(f"Scraping data in ({language})")

    language = language.value
    scrape_file = f'data/scraped-html/page-{language}.html'

    with open(scrape_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    count = 0

    output_file = f'data/{language}-data.txt'

    with open(output_file, 'w') as f:
        for word in soup.find_all('a'):
            flag=0
            word_details = word.get('data-caption')
            if word_details is None:
                continue
            word_details = BeautifulSoup(word_details, 'html.parser')
            if word_details.find('a') is None:
                print(word_details)
                continue
            meaning = word_details.find('h4').text.strip()
            if '-' in meaning:
                flag=1
                meaning = meaning.split('-')[0].rstrip()
            link = word_details.find('a').get('href')
            if meaning:
                f.write(f"{meaning}: {link}\n")
                if(flag):
                    with open("chinese.txt","a") as g:
                        g.write(meaning+'\n')
                else:
                    with open("english.txt","a") as h:
                        h.write(meaning+'\n')
                count += 1

    print("No. of resources:", count)

if __name__ == '__main__':
    scrape_esl_page(Language.ENGLISH)
        

    