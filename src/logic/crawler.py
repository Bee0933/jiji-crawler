import requests

# import json

cookies = {
    "first_visit": "1675112234",
    "rid": "organic",
    "app": "acda2ead0697443f9a811b65e7413507",
    "uid": "57c625b43e5775ed4bfc589d288b5539cc7472bb",
    "app_sid": "1675112236771",
    "approve-cookie-policy": "1",
    "g_state": '{"i_p":1675119456654,"i_l":1}',
    "_js2": "UNglVSW51TnaH8m6j8zpl1ttuX7sPjqGRaX51VHF-44=",
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "Referer": "https://jiji.ng/",
    "X-Requested-With": "XMLHttpRequest",
    "X-Window-ID": "1675114863558",
    "Connection": "keep-alive",
    # 'Cookie': 'first_visit=1675112234; rid=organic; app=acda2ead0697443f9a811b65e7413507; uid=57c625b43e5775ed4bfc589d288b5539cc7472bb; app_sid=1675112236771; approve-cookie-policy=1; g_state={"i_p":1675119456654,"i_l":1}; _js2=UNglVSW51TnaH8m6j8zpl1ttuX7sPjqGRaX51VHF-44=',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


def crawl_trending():
    try:
        response = requests.get(
            "https://jiji.ng/api_web/v1/trending-items.json",
            cookies=cookies,
            headers=headers,
            timeout=5,
        )
        data = response.json()

        products = data["adverts_list"]
        # total_products = len(products)
        for product in products:
            # product.pop("badge_info","date")
            _ = [
                product.pop(key)
                for key in [
                    "badge_info",
                    "date",
                    "id",
                    "is_boost",
                    "images_count",
                    "image",
                    "is_owner",
                    "paid_info",
                    "price",
                    "user_id",
                ]
            ]

        # json.dumps(products)
        return products, None
    # pylint: disable=broad-except
    except Exception as e:
        return None, e
