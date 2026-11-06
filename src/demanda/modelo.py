def estimar(ventas, factor=1.1):
    """Devuelve la media de ventas multiplicada por el factor."""
    if factor <= 0:
        raise ValueError(f"el factor debe ser mayor que 0: {factor}")
    if not ventas:
        raise ValueError("no hay ventas para estimar")
    for venta in ventas:
        if venta < 0:
            raise ValueError(f"venta negativa no válida: {venta}")
    return sum(ventas) / len(ventas) * factor
