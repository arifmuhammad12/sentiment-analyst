from google_play_scraper import reviews, Sort
import csv

scrapreview, continuation_token = reviews(
    'com.ruangguru.livestudents',
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=15000
)      

with open('ulasan_aplikasi.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scrapreview:
        writer.writerow([review['content']])

print("Jumlah data:", len(scrapreview))
print("Scraping selesai")