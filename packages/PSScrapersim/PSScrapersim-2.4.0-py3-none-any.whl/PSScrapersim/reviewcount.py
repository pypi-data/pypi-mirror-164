from google_play_scraper import app

result = app(
    'app.yulu.bike',
    lang='en', # defaults to 'en'
    country='in' # defaults to 'us'
)
print(result['reviews'])


# #https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
# #com.rapido.passenger com.meesho.supply



