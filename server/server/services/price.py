from server.configs.algorand import tinyman_client
from server.utils.constants import ALGO_ASSET_ID, USDC_ASSET_ID


def get_price():
    ALGO = tinyman_client.fetch_asset(ALGO_ASSET_ID)
    USDC = tinyman_client.fetch_asset(USDC_ASSET_ID)

    pool = tinyman_client.fetch_pool(USDC, ALGO)
    print(f"Pool Info: {pool.info()}")

    quote = pool.fetch_fixed_input_swap_quote(amount_in=ALGO(1_000_000), slippage=0.01)
    print(quote)

    print(f"USDC per ALGO: {quote.price}")
    print(f"USDC per ALGO (worst case): {quote.price_with_slippage}")
