from bs4 import BeautifulSoup

def scrape_ar_letters():
    print("Scraping data to retrieve arabic letters:")
    scrape_file = f'data/scraped-html/en-arabic-letters.html'

    with open(scrape_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    count = 0

    output_file = f'data/en-arabic-letters.txt'

    with open(output_file, 'w') as f:
        for word in soup.find_all('a'):
            word_details = word.get('data-caption')
            if word_details is None:
                continue
            word_details = BeautifulSoup(word_details, 'html.parser')
            if word_details.find('a') is None:
                print(word_details)
                continue
            meaning = word_details.find('h4').text.strip()
            if meaning:
                f.write(f"{meaning}\n")
                count += 1

    print("No. of resources:", count)

    with open('data/en-arabic-letters.txt') as f:
        lines = list(sorted(f.readlines()))
    
    with open('data/en-arabic-letters.txt', 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    scrape_ar_letters()
        

    