def calculate_traffic(weight, hour):
    # Calcula el factor de trafico
    if hour < 7 or hour >= 20:
        traffic_factor = 1.5
    elif hour >= 7 and hour < 10:
        traffic_factor = 1.2
    elif hour >= 10 and hour < 17:
        traffic_factor = 1.0
    else:
        traffic_factor = 0.8

    # Actualiza el peso de la arista
    return weight * traffic_factor

