import pandas as pd


def get_option_chain(symbol):

    df = pd.DataFrame({

        "Strike":[24900,24950,25000,25050,25100],

        "CE OI":[120000,250000,360000,240000,180000],

        "PE OI":[140000,200000,410000,310000,160000]

    })

    return df