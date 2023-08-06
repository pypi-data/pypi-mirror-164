#from this import s
from asyncio import as_completed
import time
from google_play_scraper import reviews_all, Sort
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import pandas as pd


from timeit import repeat
import functools



app_name = 'com.rapido.passenger'

def review(n):
    return reviews_all('com.rapido.passenger',country='in', filter_score_with=n, sleep_milliseconds=160, sort= Sort.NEWEST), n



l = [1,2,3,4,5]
# with ThreadPoolExecutor(max_workers = 8) as executor:
#     results = executor.map(review, l)
start_time = time.time()
final_resp = []

with ThreadPoolExecutor(max_workers =5) as executor:

        futures = [executor.submit(review, n) for n in l]
        # process each result as it is available
        for future in as_completed(futures):
            # get the  data
            data, n = future.result()
            final_resp.extend(data)
            # check for no data
            if data == []:
                print(f'>Error downloading score : {n}')
                fut1 = executor.submit(review, n)
                data, n = fut1.result()
                final_resp.extend(data)

                continue
            
print(f"Execution time: {time.time() - start_time}")


# sum1=0
# for x in results:
#     sum1 = sum1+len(x)
#     final_resp.extend(x)
# print(sum1)
print(len(final_resp))
df = pd.DataFrame(final_resp)

df.to_csv(f'{app_name}_27042022.csv', index=False)

# start_time = time.time()

# response = reviews_all('in.swiggy.android',country='in')


# print(f"Execution time: {time.time() - start_time}")

# print('Number of reviews collected is {}'.format(len(response)))