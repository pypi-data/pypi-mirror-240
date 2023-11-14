from googleapiclient.discovery import build
import gandai as ts
import pandas as pd

def page_one(q: str) -> pd.DataFrame:
    service = build(
        "customsearch",
        "v1",
        developerKey=ts.secrets.access_secret_version("GOOGLE_SEARCH_KEY"),
    )
    results = service.cse().list(q=q, cx="12cb7a511cc804eb0").execute()
    return pd.DataFrame(results["items"])


def search(q: str, count: int = 10) -> pd.DataFrame:
    if count > 100:
        print("max @ 100 for now")
        count = 100

    all_results = []
    for i in range(0, count, 10):
        service = build(
            "customsearch",
            "v1",
            developerKey=ts.secrets.access_secret_version("GOOGLE_SEARCH_KEY"),
        )
        results = service.cse().list(q=q, cx="12cb7a511cc804eb0", start=i).execute()
        all_results.extend(results["items"])
    df = pd.DataFrame(all_results)[["title", "link", "snippet"]]
    return df


