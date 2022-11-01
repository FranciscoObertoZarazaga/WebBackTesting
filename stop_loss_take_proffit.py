def limit(price, ref_price, coef):
    stop_loss_price = ref_price * coef
    return stop_loss_price if price < stop_loss_price else None


def set_limit(price, max_price, buy_price, sl_rate, tp_rate):
    tp_price = None if tp_rate is None else limit(price, max_price, tp_rate)
    sl_price = None if sl_rate is None else limit(price, buy_price, sl_rate)
    if tp_price is not None and tp_price > buy_price:
        return tp_price, -1
    elif sl_price is not None:
        return sl_price, -1
