def get_matching_event(event_condition, sample_space, **kwargs):
    return set([outcome for outcome in sample_space if event_condition(outcome, **kwargs)])


def compute_probability(event_condition, sample_space, **kwargs):
    outcomes = get_matching_event(event_condition, sample_space, **kwargs)

    if isinstance(sample_space, set):
        return len(outcomes) / len(sample_space)

    return sum([sample_space[outcome] for outcome in outcomes]) / sum(sample_space.values())


def relative_likelihood_curve(weighted_sample_space):
    events = list(weighted_sample_space.keys())
    combinations = [weighted_sample_space[key] for key in events]
    sample_space_size = sum(weighted_sample_space.values())

    probabilities = [value / sample_space_size for value in combinations]

    attempts = len(events)
    freq = [head_count / attempts for head_count in events]
    relative_likelihood = [attempts * prob for prob in probabilities]

    return freq, relative_likelihood
