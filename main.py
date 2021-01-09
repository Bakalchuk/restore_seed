from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic

from secret_example import known, passphrases

mnemonics = [""]

for k, options in known.items():
    current_mnemonic = mnemonics.copy()
    mnemonics = []
    for opt in options:
        mnemonics.extend([s + " {}".format(opt) for s in current_mnemonic])

mnemonics = [s[1:] for s in mnemonics]

warnings = set()
value_errors = set()
i = 0
for mnemonic in mnemonics:
    for passphrase in passphrases:
        try:
            w = Wallet.create("Wallet_{}".format(i),
                              keys=mnemonic,
                              network='bitcoin',
                              account_id=i,
                              scheme="bip32",
                              password=passphrase)
            account_btc = w.new_account('Account BTC')
            w.get_key()
            w.get_key(account_btc.account_id)
            w.info()
            print(w.transactions_full())
        except Warning as w:
            warnings.add(w)
        except ValueError as v:
            value_errors.add(v)
        i += 1

print("Warnings:")
for w in warnings:
    print(w)

print("Value errors:")
for v in value_errors:
    print(v)


def is_word(word):
    print(word in Mnemonic().wordlist())
