from nse.dataclasses.Suggestions import Suggestion, Suggestions

from dataclasses import asdict

def extract_suggestions(data:dict) -> Suggestions:

    symbols=[]
    for symbol in data['symbols']+data['mfsymbols']:
        symbols.append(Suggestion(
            symbol=symbol['symbol'],
            symbol_info=symbol['symbol_info'],
            url=symbol['url'],
            type=symbol['result_type'],
            sub_type=symbol['result_sub_type']))


    return Suggestions(symbols)