import random
from datetime import datetime

from jinja2 import FileSystemLoader, Environment
from dateutil.relativedelta import relativedelta

TEMPLATES = 'templates'
WHOLE_SALERS = ["67535", "02308", "06219"]

print("Start .... ")

# accounts = [
#     {
#         "id": x, "wholesaler": "67535"
#     } for x in range(1000000, 1100000)]

# delivery_windows = [
#     {
#         "id": str(int(datetime.now().timestamp() * 1000)) + str(x),
#         "wholesaler": "67535",
#         "accountId": random.randint(1000000, 1100000),
#         "updatedTime": datetime.now().strftime("%Y-%m-%d")
#
#     } for x in range(900000)
# ]
#
# invoices = [
#     {
#         "accountId": random.randint(1000000, 1100000),
#         "wholesaler": WHOLE_SALERS[random.randint(0, 2)],
#         "dateFull": datetime.now().strftime("{\"$date\": \"%Y-%m-%dT%H:%M:%S.000Z\"}"),
#         "timestamp": str(int(datetime.now().timestamp() * 1000)) + str(x)
#     } for x in range(1500000)
# ]
#
# account_groups = [
#     {
#         "id": x,
#         "wholesaler": "67535",
#         "accountIds": '","'.join([f"ACC_GEN_{random.randint(1000000, 1100000)}-67535" for z in range(random.randint(10, 100))]),
#         "dateFull": datetime.now().strftime("{\"$date\": \"%Y-%m-%dT%H:%M:%S.000Z\"}")
#     } for x in range(500, 136 + 500)
# ]
#
#

free_good_groups = [
    {
        "id": x,
        "wholesaler": "67535",
        "dateFull": datetime.now().strftime("{\"$date\": \"%Y-%m-%dT%H:%M:%S.000Z\"}"),
        "skuIds": '","'.join([f"{str(random.randint(10041, 616824)).zfill(6)}-C-67535" for z in range(random.randint(10, 100))]),
    } for x in range(100000, 20000 + 100000)
]

sku_groups = [
    {
        "id": x,
        "wholesaler": "67535",
        "dateFull": datetime.now().strftime("{\"$date\": \"%Y-%m-%dT%H:%M:%S.000Z\"}"),
        "skuIds": '","'.join([f"{str(random.randint(10041, 616824)).zfill(6)}-C-67535" for z in range(random.randint(10, 100))]),
    } for x in range(100000, 200000 + 100000)
]

promotions = list()

# Free Good
promotions.extend(
    {
        "id": x,
        "wholesaler": "67535",
        "accountGroupIds": '","'.join([f"ACC_GROUP_GEN_{random.randint(500, 136 + 500)}-67535" for z in range(random.randint(1, 7))]),
        "freeGoodGroupIds": '","'.join([f"FREE_GOOD_GROUP_GEN_{random.randint(100000, 20000 + 100000)}-67535" for z in range(random.randint(1, 7))]),
        "datePlusOneYear": (datetime.now() + relativedelta(years=1)).strftime("{\"$date\": \"%Y-%m-%dT%H:%M:%S.000Z\"}"),
        "dateFull": datetime.now().strftime("{\"$date\": \"%Y-%m-%dT%H:%M:%S.000Z\"}"),
        "type": "STEPPED_FREE_GOOD",
    } for x in range(1000000, 250000 + 1000000)
)

# Discounts
promotions.extend(
    {
        "id": x,
        "wholesaler": "67535",
        "accountGroupIds": '","'.join([f"ACC_GROUP_GEN_{random.randint(500, 136 + 500)}-67535" for z in range(random.randint(1, 7))]),
        "skuGroupIds": '","'.join([f"SKU_GROUP_GEN_{random.randint(100000, 20000 + 100000)}-67535" for z in range(random.randint(1, 7))]),
        "datePlusOneYear": (datetime.now() + relativedelta(years=1)).strftime("{\"$date\": \"%Y-%m-%dT%H:%M:%S.000Z\"}"),
        "dateFull": datetime.now().strftime("{\"$date\": \"%Y-%m-%dT%H:%M:%S.000Z\"}"),
        "type": "STEPPED_DISCOUNT",
    } for x in range(1250000, 250000 + 1250000)
)


def main():
    file_loader = FileSystemLoader(TEMPLATES)
    env = Environment(loader=file_loader)
    # env.get_template('US-Account.json.jinja').stream(accounts=accounts).dump('export/US-Account.json')
    # print(f"Done! {len(promotions)}")
    # env.get_template('US-DeliveryWindow.json.jinja').stream(deliveryWindows=delivery_windows).dump('export/US-DeliveryWindow.json')
    # print(f"DeliveryWindow Done! {len(delivery_windows)}")
    # env.get_template('US-Invoice.json.jinja').stream(invoices=invoices).dump('export/US-Invoice.json')
    # print(f"Invoice Done! {len(invoices)}")
    # env.get_template('US-AccountGroup.json.jinja').stream(accountGroups=account_groups).dump('export/US-AccountGroup.json')
    # print(f"AccountGroup Done! {len(account_groups)}")
    env.get_template('US-FreeGoodGroup.json.jinja').stream(freeGoodGroups=free_good_groups).dump('export/US-FreeGoodGroup.json')
    print(f"FreeGoodGroup Done! {len(free_good_groups)}")
    env.get_template('US-SkuGroup.json.jinja').stream(skuGroups=sku_groups).dump('export/US-SkuGroup.json')
    print(f"SkuGroup Done! {len(sku_groups)}")
    env.get_template('US-Promotion.json.jinja').stream(promotions=promotions).dump('export/US-Promotion.json')
    print(f"Promotion Done! {len(promotions)}")


if __name__ == '__main__':
    main()
