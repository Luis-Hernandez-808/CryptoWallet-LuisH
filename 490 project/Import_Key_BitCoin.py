from bit import Key
from bit.network import satoshi_to_currency_cached


key = Key('btcWİFkeyHere')
key.get_unspents()
satoshi_to_currency_cached(1500, 'usd')
satoshi_to_currency_cached(1500, 'btc')