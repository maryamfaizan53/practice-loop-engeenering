def get_last_n_items(items, n):
    # BUG: off-by-one, this drops the last item
    return items[:n-1]
