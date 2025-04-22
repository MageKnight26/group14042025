import decimal
import logging

from pywebio.input import slider, FLOAT, NUMBER
from pywebio.input import input as pw_input
from pywebio.output import put_html, put_success

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("shop.log"), logging.StreamHandler()],
)

APPLE_PRICE = decimal.Decimal(52.75)
BANANAS_PRICE = decimal.Decimal(81.40)

logging.debug("debug")
logging.info("info")
# HEADER

put_html("<h1>Welcome to our Fruit Shop</h1>")

# INPUT SECTION

apple_weight = slider(
    "Вага яблук", type=FLOAT, min_value=0, max_value=5, value=0.01, required=True
)
apple_weight = decimal.Decimal(apple_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)
logging.info(f"{apple_weight=}")

bananas_weight = pw_input(
    "Вага бананів", type=NUMBER, required=True, min=0, max=10, value=3
)
bananas_weight = decimal.Decimal(bananas_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)
logging.info(f"{bananas_weight=}")

apple_cost = (APPLE_PRICE * apple_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
bananas_cost = (BANANAS_PRICE * bananas_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
total_cost = apple_cost + bananas_cost
put_success(
    f"Чек \nЦіна яблук:\t{apple_cost} грн. \nЦіна бананів:\t{bananas_cost} грн. \nЗагальна сума:\t{total_cost} грн."
)
pass
