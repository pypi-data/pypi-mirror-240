from valalgn.asl import build_full_game, plot_game, minimize_incentives, \
    subgame_perfect_equilibrium, outcome_probability, ExtensiveFormGame

# build and visualize the game
game = build_full_game(
    "</path/to/asl/description>",
    "<action_situation_id>",
    "<priority_threshold>"
)

plot_game(game, ...)

# custom function to assign utilities
def assign_utilities(game: ExtensiveFormGame) -> None:
    raise NotImplementedError
    
assign_utilities(game, ...)

# compute equilibrium strategies
subgame_mixed_strat, _, _ = subgame_perfect_equilibrium(game, minimize_incentives)

# compute outcome probabilities
outcome_prob = {t: outcome_probability(game, subgame_mixed_strat, t)
                for t in game.game_tree.terminal_nodes}

# custom function to evaluate outcomes
def outcome_evaluation(game: ExtensiveFormGame) -> None:
    raise NotImplementedError

# compute the alignment using the custom outcome evaluation
algn = sum(
    [
        outcome_prob[t]*outcome_evaluation(t, ...)
        for t in game.game_tree.terminal_nodes
    ]
)
