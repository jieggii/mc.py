from random import choices


def get_random_next_frame(available_frames: dict) -> str or None:
    population = [frame for frame in available_frames.keys()]
    weights = [weight for weight in available_frames.values()]

    if population:
        return choices(population=population, weights=weights)[0]

    else:
        return None
