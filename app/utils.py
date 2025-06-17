def execute_strategy(
    strategy_map: dict, method_type: str, book, action: str
) -> str | None:
    strategy = strategy_map.get(method_type)
    if not strategy:
        raise ValueError(f"Unknown {action} type: {method_type}")
    method = getattr(strategy, action)
    return method(book)
