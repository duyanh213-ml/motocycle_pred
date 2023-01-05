from bs4 import BeautifulSoup
import requests


MIN_PAGES = 7
MAX_PAGES = 250
MAIN_DOMAIN = f"https://xe.chotot.com/"


FILE_PATH = r"/home/duyanh/Documents/VS_WorkSpace/projects/programming_for_DS_v1/data/moto_raw.csv"


def check_none(info, main_info_text):
    if info:
        return info.text.replace(" ", "")
    return "Null"


def scrape_data():
    for i in range(MIN_PAGES, MAX_PAGES):
        mainURL = f"{MAIN_DOMAIN}/mua-ban-xe-may?page={i}"

        main_text = requests.get(mainURL).text
        soup = BeautifulSoup(main_text, "lxml")
        motors = soup.find_all(
            "li", class_="AdItem_wrapperAdItem__S6qPH AdItem_big__70CJq")

        for motor in motors:
            infoURL = f"{MAIN_DOMAIN}{motor.a['href']}"

            info_text = requests.get(infoURL).text
            main_info_text = BeautifulSoup(info_text, "lxml")

            brand = main_info_text.find(
                "a", itemprop="motorbikebrand")
            brand = check_none(brand, main_info_text)

            reg_year = main_info_text.find(
                "span", itemprop="regdate")
            reg_year = check_none(reg_year, main_info_text)

            motor_condition = main_info_text.find(
                "span", itemprop="condition_ad")
            motor_condition = check_none(motor_condition, main_info_text)

            motor_cap = main_info_text.find(
                "span", itemprop="motorbikecapacity")
            motor_cap = check_none(motor_cap, main_info_text)

            motor_model = main_info_text.find(
                "a", itemprop="motorbikemodel")
            motor_model = check_none(motor_model, main_info_text)

            km_nums = main_info_text.find(
                "span", itemprop="mileage_v2")
            km_nums = check_none(km_nums, main_info_text)

            motor_type = main_info_text.find(
                "span", itemprop="motorbiketype")
            motor_type = check_none(motor_type, main_info_text)

            price = main_info_text.find(
                "span", itemprop="price")
            price = check_none(price, main_info_text)

            csv_row = f"{brand},{reg_year},{motor_condition},{motor_cap},{motor_model},{km_nums},{motor_type},{price}\n"

            print(csv_row)
            print(i)
            # open the file in the write mode
            with open(f'{FILE_PATH}', 'a') as f:
                f.write(csv_row)


if __name__ == "__main__":
    scrape_data()
