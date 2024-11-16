import os
from dotenv import load_dotenv

from tinyman.v2.client import TinymanV2TestnetClient
from algosdk.v2client import algod

load_dotenv()

algod_token = str(os.getenv("ALGOD_TOKEN"))
algod_server = str(os.getenv("ALGOD_SERVER"))


algod_client = algod.AlgodClient(algod_token, algod_server)
tinyman_client = TinymanV2TestnetClient(algod_client)
