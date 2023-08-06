# from asyncio import as_completed
import time
from .google_play_scraper import reviews_all, Sort, reviews
from concurrent.futures import ThreadPoolExecutor, as_completed
# import pandas as pd
import json
import os
import argparse
from .utils import GetReviews


get_reviews = GetReviews()
n_threads = os.cpu_count() * 2


def review(app_name, n):
    """Call the google_play_scraper and Scrapes reviews"""

    return (
        reviews_all(
            f"{app_name}",
            country="in",
            filter_score_with=n,
            sleep_milliseconds=160,
            # sort=Sort.NEWEST,
        ),
        n,
    )


def n_reviews(app_name, n):
    """Call the google_play_scraper and Scrapes reviews"""
    resp, token = reviews(
        f"{app_name}", country="in", filter_score_with=n, sort=Sort.NEWEST, count=15000
    )
    return resp, n


def threadExecutor(app_name):
    """Calls review function with 4 threads"""

    l = [1, 2, 3, 4, 5]

    start_time = time.time()

    final_resp = []

    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        futures = [executor.submit(review, app_name, n) for n in l]

        # process each result as it is available

        for future in as_completed(futures):
            # get the  data
            data, n = future.result()
            # print(n)
            final_resp.extend(data)
            # check for no data
            if data == []:
                print(f">Error downloading score : {n}")
                fut1 = executor.submit(review, app_name, n)
                data, n = fut1.result()
                final_resp.extend(data)
                continue

    print(f"Execution time: {time.time() - start_time}")
    print(len(final_resp))
    return final_resp


def saveData(final_resp, app_name):
    """Saves the data in json format"""
    f"{app_name}_data.json"
    with open(f"{app_name}_data.json", "w") as f:
        json.dump(final_resp, f)

    #         json.dump(data, f)
    # def write_json(target_path, target_file, data):
    #     if not os.path.exists(target_path):
    #         try:
    #             os.makedirs(target_path)
    #         except Exception as e:
    #             print(e)
    #             raise
    #     with open(os.path.join(target_path, target_file), "w") as f:
    #         json.dump(data, f)

    # write_json("output", f"{app_name}_data.json", final_resp)


# def saveCsv(final_res, app_name):
#     df = pd.DataFrame(final_res)
#     df.to_csv(f"{app_name}_27042022.csv", index=False)


def PlayStoreScraper(app_name):
    """Takes app id as input; scrapes reviews with 4 threads and saves as json file"""

    data = threadExecutor(app_name)
    saveData(data, app_name)
    # saveCsv(data, app_name)
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="App Store review scraper ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("App Id", type=str, help="App Id from playstore")
    parser.add_argument("-d", "--delay", help="how many reviews to retrieve")

    args = parser.parse_args()
    config = vars(args)
    print(config)

    app_name = config["App Id"]
    delay = int(config["delay"])

    data = threadExecutor(app_name)
    saveData(data, app_name)
