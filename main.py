#account number : 101-002-19374105-002
#token 5db257a406b291a834f25bad76c72b1a-1b2e917ba34c549045c6d6fc86e38bbd

import pandas as pd
import tpqoa

api = tpqoa.tpqoa("oanda.cfg")
print(api)
accSum = api.get_account_summary()
print(accSum)