import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import numpy as np
import pandas as pd
import random

from copy import deepcopy
from itertools import combinations, product
from networkx.algorithms.dag import descendants
from networkx.algorithms.shortest_paths.generic import shortest_path
from networkx.algorithms.simple_paths import all_simple_edge_paths
from scipy.optimize import Bounds, LinearConstraint, minimize

from typing import Any, Callable, Dict, List, Set, Tuple


class NormalFormGame:
    """A general, n-player general-sum normal-form game.

    A finite, n-person normal form game is a tuple :math:`(N, A, u)`, where:

    - :math:`N=\{1, 2, ..., n\}` is the set of players.
    - :math:`A=A_1 \\times A_2 \\times ... \\times A_n` is the set of joint
      actions, where :math:`A_i` is the set of actions available to player
      :math:`i`.
    - :math:`u=(u_1,u_2,...,u_n)`, where :math:`u_i:A \\rightarrow R` are
      real-valued payoff functions.

    Parameters
    ----------
    players : List[Any]
        The list of players that participate in the game.
    actions : List[Tuple[Any, ...]]
        A list of tuples. Each tuple corresponds to the domain of actions (or
        'pure' strategies) available to each player in order, *i.e.* actions for
        player 1, actions for player 2, etc.
    payoff_function : Dict[Tuple[Any, ...], Tuple[float, ...]]
        A dictionary mapping joint actions to player's payoffs. The dictionary
        format is: tuple of joint actions (key) : tuple of players' float value
        payoffs (value).
    **kwargs
        Arbitrary keyword arguments.

    Attributes
    ----------
    action_to_index : Dict[int, Dict[Any, int]]
        A dictionary of dictionaries. For every player, it stores a dictionary
        mapping the player's domain of actions to integers.
    num_players : int
        The number of players in the game.
    payoffs : Dict[int, numpy.ndarray]
        Dictionary mapping every player to their payoff array. The indices of
        the matrix correspond are stored in `action_to_index`.
    player_actions : Dict[int, List[Any]]
        A dictionary mapping every player to the list of actions she has
        available.
    **kwargs
        Arbitrary keyword arguments.

    Raises
    ------
    ValueError
        If the number of action options does not equal the number of players. If
        there are outcomes for whom no utility has been provided. If there is
        some outcome for which the number of payoff elements does not match the
        number of players in the game.

    """

    def __init__(
            self,
            players: List[Any],
            actions: List[Tuple[Any, ...]],
            payoff_function: Dict[Tuple[Any, ...], Tuple[float, ...]],
            **kwargs
        ) -> None:
        self.players = players
        self.num_players = len(self.players)

        # assign actions to players
        if len(actions) != self.num_players:
            raise ValueError("the number of action options provided must \
                equal the number of players")
        self.player_actions = {}
        for i in range(self.num_players):
            self.player_actions[i] = actions[i]

        # map actions to integers for every player
        self.action_to_index = {}
        for i in range(self.num_players):
            self.action_to_index[i] = {}
            for j, a in enumerate(self.player_actions[i]):
                self.action_to_index[i][a] = j

        # build payoff arrays
        self.payoffs = {}
        payoff_array_shape = tuple([len(acts) for acts in
                                    self.player_actions.values()])
        for i in range(self.num_players):
            self.payoffs[i] = np.zeros(shape=payoff_array_shape)

        # check that all the possible outcomes are included in the payoff
        input_outcomes = set(payoff_function.keys())
        all_outcomes = self.all_outcomes()
        difference = all_outcomes - input_outcomes
        if difference != set():
            raise ValueError("outcomes {} not included in the payoff function"
                             .format(difference))

        for rewards in payoff_function.values():
            if len(rewards) != self.num_players:
                raise ValueError("payoff {} should have as many elements as \
                    players there are in the game".format(rewards))
        # function
        for joint_actions, rewards in payoff_function.items():
            joint_indexes = self.actions_to_indices(*joint_actions)
            for i in range(self.num_players):
                self.payoffs[i][joint_indexes] = rewards[i]

        # store additional keyword arguments
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        """For printing the game to console, only for two-player games.

        Returns
        -------
        str
            String representation of the game matrix.

        """
        if self.num_players != 2:
            return "Normal Form Game"
        actions1 = self.action_to_index[0].keys()
        actions2 = self.action_to_index[1].keys()
        numpy_matrix = np.empty(shape=(len(actions1), len(actions2)))*np.nan
        matrix = pd.DataFrame(numpy_matrix, index=actions1, columns=actions2,
                              dtype=object)
        for a1, a2 in product(actions1, actions2):
            outcome = self.pure_strategies_rewards(a1, a2)
            matrix.at[a1, a2] = outcome
        return matrix.to_string(justify='center') + "\n"

    def actions_to_indices(self, *args) -> Tuple[int, ...]:
        """Map a list of joint actions to a list of integers.

        Parameters
        ----------
        *args
            Joint actions taken by the players.

        Returns
        -------
        indices : Tuple[int, ...]
            Tuple of integer indices corresponding to the joint actions.

        Raises
        ------
        ValueError
            If the number of actions does not match the number of players in
            the game.

        """
        if len(args) != self.num_players:
            raise ValueError("number of actions must match number of players")
        indices = tuple(self.action_to_index[i][a] for i, a in enumerate(args))
        return indices

    def pure_strategies_rewards(self, *args) -> Tuple[float, ...]:
        """Get the rewards for every player when they play a pure strategy.

        Parameters
        ----------
        *args
            Joint actions taken by the players.

        Returns
        -------
        round_rewards : Tuple[float, ...]
            Rewards obtained by the players.

        """
        action_indices = self.actions_to_indices(*args)
        round_rewards = tuple(
            self.payoffs[i][tuple(action_indices)] for i in range(self.num_players)
        )
        return round_rewards

    def num_outcomes(self) -> int:
        """Compute how many different outcomes are possible in this game.

        Returns
        -------
        int
            The number of possible outcomes.

        """
        num_outcomes = 1
        for player_actions in self.player_actions.values():
            num_outcomes *= len(player_actions)
        return num_outcomes

    def all_outcomes(self) -> Set[Tuple[Any, ...]]:
        """Return all the possible outcomes.

        Returns
        -------
        all_outcomes : Set[Tuple[Any, ...]]
            A set of all the outcomes, as tuples of player's actions.

        """
        all_outcomes = set(product(*self.player_actions.values()))
        return all_outcomes

    def is_zero_sum(self) -> bool:
        """Check whether the game is zero-sum.

        A normal form game is *zero sum* if the payoff functions fulfill the
        following property:

        .. math::
        
            \sum\limits_{i} u_i(a_1,...,a_n) = 0 \quad \\forall i \in N,
            \\forall a_1,...,a_n \in A

        Returns
        -------
        bool
            Is the game zero-sum(`True`) or not (`False`).

        """
        for z in self.all_outcomes():
            total_payoff = sum(self.pure_strategies_rewards(*z))
            if total_payoff != 0.:
                return False
        return True

    def __check_valid_mixed_strategy(self, mixed_strategy: Dict[Any, float]) \
            -> None:
        """Check if a mixed strategy is a valid probability distribution.

        Parameters
        ----------
        mixed_strategy : Dict[Any, float]
            Map from action to probability.

        Raises
        ------
        ValueError
            If the sum of probabilities across actions does not equal unity
            within a tolerance of 1.E.3.

        """
        if not np.isclose(sum(mixed_strategy.values()), 1., atol=1.E-3):
            raise ValueError("sum of probability distribution over actions \
                              must equal 1 with tolerance 1.E-3")

    def mixed_strategy_support(self, player: int,
                               mixed_strategy: Dict[Any, float]) -> Set[Any]:
        """Get the support set of a given player's mixed strategy.

        Parameters
        ----------
        player : int
            Who is playing the mixed strategy. Takes values :math:`1, 2,...,n`
        mixed_strategy : Dict[Any, float]
            Probability distribution.

        Returns
        -------
        Set[Any]
            The set of actions with non-zero probability in the mixed strategy.

        """
        self.__check_valid_mixed_strategy(mixed_strategy)
        i = player-1
        support = set()
        for a in self.player_actions[i]:
            try:
                p_a = mixed_strategy[a]
            except KeyError:
                p_a = 0
            if p_a > 0:
                support.add(a)
        return support

    def mixed_strategies_rewards(self, *args) -> Tuple[float, ...]:
        """Return the expected rewards from a mixed strategy profile.

        .. math:: u_i(s) = \sum\limits_{a\in A} u_i(a) \prod\limits_{j\in N} \
          s_j(a_j)

        Parameters
        ----------
        args
            Players' mixed strategies, as dictionaries mapping actions to
            probabilities. For every mixed strategy, it is checked that it is a
            valid probability distribution.
        """
        for ms in args:
            self.__check_valid_mixed_strategy(ms)
        rewards = tuple(0 for _ in range(self.num_players))
        players_actions = [mixed_strat.keys() for mixed_strat in args]
        pure_action_profiles = product(*players_actions)

        for pap in pure_action_profiles:
            probabilities = [args[i][a] for i, a in enumerate(pap)]
            joint_probability = np.prod(probabilities)
            joint_rewards = self.pure_strategies_rewards(*pap)
            rewards = tuple(r+joint_probability*jr for r, jr in
                            zip(rewards, joint_rewards))
        return rewards

    def switch_incentive(
            self,
            player: Any,
            action: Any,
            mixed_strategy: Dict[Any, Dict[Any, float]]
        ) -> float:
        """Compute the incentive for a player to switch to a pure strategy.

        Given a general mixed strategy profile, compute the incentive of
        ``player`` to switch to a pure strategy where ``action`` is played. It
        corresponds to the formula:

        .. math::

            c_{i}^{j}(s) = u_i(a_{j}^{i}, s_{-j}) - u_i(s) \\
            d_{i}^{j}(s) = max(c_{i}^{j}(s), 0)

        where the subindex corresponds to the :math`i`-th player and the
        superindex corresponds to its :math`j`-th action.

        Parameters
        ----------
        player : Any
            The player for whom the incentive is computed.
        action : Any
            The action that the player is tempted of swictching to as a pure
            strategy.
        mixed_strategy : Dict[Any, Dict[Any, float]]
            The original mixed strategy for all players.

        Returns
        -------
        float
            :math:`d_{i}^{j}(s)`.

        References
        ----------
        Shohan, Y., & Leyton-Browm, K. (2009). Computing Solution Concepts of
        Normal-Form Games. In Multiagent Systems: Algorithmic, Game-Theoretic,
        and Logical Foundations (pp. 87–112). Cambridge University Press.

        """
        for ms in mixed_strategy.values():
            self.__check_valid_mixed_strategy(ms)

        # utility under the original mixed strategy
        ms = [mixed_strategy[p] for p in self.players]
        mixed_strat_utility = self.mixed_strategies_rewards(*ms)

        # utility if player switches to pure strategy
        player_index = self.players.index(player)
        player_pure_strat = {a: 0 for a in self.player_actions[player_index]}
        player_pure_strat[action] = 1

        switch_strat = [mixed_strategy[p] for p in self.players]
        switch_strat[player_index] = player_pure_strat
        switch_strat_utility = self.mixed_strategies_rewards(*switch_strat)

        c = switch_strat_utility[player_index] - \
            mixed_strat_utility[player_index]
        if c > 0:
            return c
        return 0.

    def incentive_target_function(
            self,
            mixed_strategy:
            Dict[Any, Dict[Any, float]]
        ) -> float:
        """Compute the target function to minimize the incentive to swicth.

        Compute the target function that is to be minimised when all players do
        not have an incentive to switch from the equilibrium mixed strategy.

        .. math::

            f(s) = \sum\limits_{i \in G} \sum\limits_{j \in A_j} (d_i^j(s))^2

        Parameters
        ----------
        mixed_strategy : Dict[Any, Dict[Any, float]]
            The mixed strategy for which the total switching incentive is being
            computed.

        Returns
        -------
        float
            :math:`f(s)`.

        References
        ----------
        Shohan, Y., & Leyton-Browm, K. (2009). Computing Solution Concepts of
        Normal-Form Games. In Multiagent Systems: Algorithmic, Game-Theoretic,
        and Logical Foundations (pp. 87–112). Cambridge University Press.

        """
        f = 0.
        for n, p in enumerate(self.players):
            for a in self.player_actions[n]:
                incentive = self.switch_incentive(p, a, mixed_strategy)
                f += incentive**2
        return f

    def completely_random_strat_vector(self) -> List[float]:
        """Compute the vector of completely random strategies.

        Build the list that correponds to the vector of completely random
        strategies. To be used as the initial guess in an optimization
        procedure.

        Returns
        -------
        List[float]
            The vector of completely random strategies.

        """
        initial_guess = []
        for i in range(self.num_players):
            num_player_actions = len(self.player_actions[i])
            player_random_strat = [1/num_player_actions] * num_player_actions
            initial_guess += player_random_strat
        return initial_guess

    def strategies_vec2dic(self, vector: List[float]) -> Dict[Any, Dict[Any, float]]:
        """Turn a vector representing a strategy into dictionary format.

        Includes checks that the input vector has the correct size, and that
        the mixed strategies encoded in the vector are proper probability
        distributions.

        Parameters
        ----------
        vector : List[float]
            A joint strategy encoded as a vector.

        Returns
        -------
        Dict[Any, Dict[Any, float]]
            The dictionary format of the input strategy vector.

        """
        # check that the vector has the right length
        actions_per_player = [len(self.player_actions[i]) for i in
                              range(self.num_players)]
        total_num_actions = sum(actions_per_player)
        assert len(vector) == total_num_actions, "strategies vector has \
            length {}, {} required".format(len(vector), total_num_actions)

        strategies = {}
        for i in range(self.num_players):
            if i == 0:
                first_index = 0
            else:
                first_index = sum(actions_per_player[:i])
            last_index = first_index + actions_per_player[i]
            player_strat_vec = vector[first_index:last_index]
            player_strat_dic = {a: x for a, x in zip(self.player_actions[i],
                                                     player_strat_vec)}
            self.__check_valid_mixed_strategy(player_strat_dic)
            strategies[self.players[i]] = player_strat_dic
        return strategies

    def make_strat_bounds(self) -> Bounds:
        """Build the bounds [0,1] for a joint strategy profile vector.

        In any vector encoding a joint strategy, all components must be between
        0 and 1.

        Returns
        -------
        scipy.optimize.Bounds

        """
        actions_per_player = [len(self.player_actions[i]) for i in
                              range(self.num_players)]
        total_num_actions = sum(actions_per_player)
        low_bounds = [0 for _ in range(total_num_actions)]
        high_bounds = [1 for _ in range(total_num_actions)]
        return Bounds(low_bounds, high_bounds)

    def make_linear_constraints(self) -> LinearConstraint:
        """Build the linear constraints for a joint strategies vector.

        In a vector that encodes a joint strategy profile, the components that
        make up the mixed srtategies of any individual must add up to one. This
        method encodes this requirement.

        Returns
        -------
        scipy.optimize.LinearConstraint

        """
        actions_per_player = [len(self.player_actions[i]) for i in
                              range(self.num_players)]
        total_num_actions = sum(actions_per_player)
        player_indices = []
        matrix = []
        for i in range(self.num_players):
            if i == 0:
                first_index = 0
            else:
                first_index = sum(actions_per_player[:i])
            last_index = first_index + actions_per_player[i]
            player_indices.append((first_index, last_index))
            row = [0]*first_index + [1]*actions_per_player[i] + \
                [0]*(total_num_actions-last_index)
            matrix.append(row)
        eq_constraints = {'type': 'eq',
                          'fun': lambda x: np.array([sum(x[f:l]) - 1
                                                     for f, l in
                                                     player_indices]),
                          'jac': lambda x: matrix}
        return eq_constraints


R, T, S, P = 6., 9., 0., 3.

prisoners_dilemma = NormalFormGame(
    players=['alice', 'bob'],
    actions=[(True, False)]*2,
    payoff_function={
        (True, True): (R, R),
        (True, False): (S, T),
        (False, True): (T, S),
        (False, False): (P, P)
    }
)


rock_paper_scissors = NormalFormGame(
    players=['alice', 'bob'],
    actions=[('Rock', 'Paper', 'Scissors')]*2,
    payoff_function={
        ('Rock', 'Rock'): (0, 0),
        ('Rock', 'Paper'): (-1, 1),
        ('Rock', 'Scissors'): (1, -1),
        ('Paper', 'Rock'): (1, -1),
        ('Paper', 'Paper'): (0, 0),
        ('Paper', 'Scissors'): (-1, 1),
        ('Scissors', 'Rock'): (-1, 1),
        ('Scissors', 'Paper'): (1, -1),
        ('Scissors', 'Scissors'): (0, 0)
    }
)


class ExtensiveFormGame:
    """Implementation of a game in extensive form.

    The game is initialized 'empty', meaning with minimal attribute
    assignments. Attributes are then set through the various methods. The
    extensive form game is modelled as described in the reference, see the
    chapter on extensive games.

    Parameters
    ----------
    **kwargs
      Additional keyword arguments.

    Attributes
    ----------
    game_tree : networkx.DiGraph
        Game tree, directed graph. Other than the methods and attributes of the
        class, two additional attributes are set:
        * root (Any): The root node, initialized to None.
        * terminal_nodes (List[Any]): The list of terminal nodes, initialized
        to an empty list.
        The game tree is initialized as empty.
    information_partition : Dict[Any, List[Set[Any]]]
        For every player (key), it maps it to the list of the information
        sets (values).
    is_perfect_informtion : bool, `True`
        The game is initialized as being of perfect information.
    players : List[Any]
        List of players in the game. It is initialized empty.
    probability : Dict[Any, Dict[Tuple[Any, Any], float]]
        Probability distributions over the outgoing edges at every node where
        chance takes an action. The keys are the nodes where chance acts. The
        values are dictionaries mapping every outgoing edge from that node to
        its probability.
    turn_function : Dict[Any, Any]
        Function that maps every non-terminal node to the player whose turn it
        is to take an action at the node.
    utility : Dict[Any, Dict[Any, float]]
        For every terminal node, it maps the utility that the various players
        (excluding chance) assign to it.

    See Also
    --------
    networkx.DiGraph

    """

    def __init__(self, **kwargs) -> None:
        # players
        self.players = []

        # game tree
        self.game_tree = nx.DiGraph()
        self.game_tree.root = None
        self.game_tree.terminal_nodes = []

        # turn function
        self.turn_function = {}

        # information partition
        self.information_partition = {}
        self.is_perfect_information = True

        # probability distribution over chance edges
        self.probability = {}

        # utility function
        self.utility = {}

        # additional info
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __check_player_in_game(self, player_id: Any) -> None:
        """Check that the given player is actually in the game.

        Parameters
        ----------
        player_id : Any

        Raises
        ------
        ValueError
            If the player is not in the game.

        """
        if player_id not in self.players:
            raise ValueError("player {} not in game".format(player_id))

    def __check_nonterminal_node(self, node_id: Any) -> None:
        """Check that a node is in the game tree.

        Parameters
        ----------
        node_id : Any

        Raises
        ------
        ValueError
            If the node is not in the game tree.

        """
        if node_id not in self.get_nonterminal_nodes():
            raise ValueError("node {} is a terminal node".format(node_id))

    def __check_terminal_node(self, node_id: Any) -> None:
        """Check that a node is terminal.

        Parameters
        ----------
        node_id : Any

        Raises
        ------
        ValueError
            If the node is not terminal.

        """
        if node_id not in self.game_tree.terminal_nodes:
            raise ValueError("node {} is not a terminal node".format(node_id))

    def add_players(self, *players_id: Any) -> None:
        """Add a lists of players to the game, encoded in any data structure.

        Parameters
        ----------
        players_id : List[Any]
          Players to be added to the game. Exclude 'chance'.

        Raises
        ------
        ValueError
          If 'chance' is among the players to be added.

        """
        for p in players_id:
            if p == 'chance':
                raise ValueError("player 'chance' cannot be added to the game")
            if p not in self.players:
                self.players.append(p)
                self.information_partition[p] = []

    def add_node(
            self,
            node_id: Any,
            player_turn: Any = None,
            is_root: bool = False
        ) -> None:
        """Add a node the game tree.

        If the node is non-terminal and it is not a chance node, perfect
        information is assumed. A set containing the single node is added to
        the information partition of the player playing at the node.

        Also, if the node is non-terminal (regardless of whether it is a
        chance node or not), it is added to `turn_function` and its player is
        assigned.

        Parameters
        ----------
        node_id : Any
            Node to be added.
        player_turn : Any, optional
            Whose player has the turn at the node. If None is given, it is
            assumed that the node is terminal. The default is None.
        is_root : bool, optional
            Whether the node is the root of the game tree. The default is
            False.

        """
        self.game_tree.add_node(node_id)

        # if player turn given
        if player_turn:
            self.turn_function[node_id] = player_turn
            # add player to game if not already there
            if player_turn not in self.players and player_turn != 'chance':
                self.players.append(player_turn)
            # if not a chance node, assume perfect information
            if player_turn != 'chance':
                self.__check_player_in_game(player_turn)
                self.information_partition[player_turn].append({node_id})

        # if player turn not given, it is a terminal node
        else:
            self.game_tree.terminal_nodes.append(node_id)

        # assign as root if indicated
        if is_root:
            self.game_tree.root = node_id

    def set_node_player(self, node_id: Any, player_turn: Any) -> None:
        """Set the player at a node after it has been added to the game tree.

        If the node had been designated as a terminal, remove it from that
        list.

        Parameters
        ----------
        node_id : Any
            The node whose player changes.
        player_turn : Any
            The new player that takes turn at the node.

        """
        self.turn_function[node_id] = player_turn
        # add player to game if not already there
        if player_turn not in self.players and player_turn != 'chance':
            self.players.append(player_turn)
        # delete node from terminal nodes if there
        if node_id in self.game_tree.terminal_nodes:
            self.game_tree.terminal_nodes.remove(node_id)

    def add_edge(self, from_node: Any, to_node: Any, label: Any) -> None:
        """Add an edge to the game tree between two nodes.

        Parameters
        ----------
        from_node : Any
            Origin node of the edge.
        to_node : Any
            Destination node of the edge.
        label : Any
            The edge label corresponsing to the action being take.

        """
        self.game_tree.add_edge(from_node, to_node, action=label)

    def get_nonterminal_nodes(self) -> List[Any]:
        """Obtain the list of non-terminal nodes in the game tree.

        Returns
        -------
        List[Any]
            List of non-terminal nodes.

        """
        nonterminal_nodes = []
        for n in self.game_tree.nodes:
            if n not in self.game_tree.terminal_nodes:
                nonterminal_nodes.append(n)
        return nonterminal_nodes

    def get_theta_partition(self) -> Dict[Any, Set[Any]]:
        """Get the turns partition.

        The turns partition (or :math:`\Theta` partition) splits the
        non-terminal nodes into disjunct sets, according to whose turn it is
        to play at the node (including the 'chance' player).

        Returns
        -------
        Dict[Any, Set[Any]]
            For every player in the game, including 'chance', the set of nodes
            where it is that player's turn to play.

        """
        # initialize partitions to empty set
        theta_partition = {}
        for p in self.players:
            theta_partition[p] = set()
        theta_partition['chance'] = set()
        # add nodes to their corresponding partition
        for n in self.get_nonterminal_nodes():
            node_turn = self.turn_function[n]
            theta_partition[node_turn].add(n)
        return theta_partition

    def get_player_utility(self, player_id: Any) -> Dict[Any, float]:
        """Return the utility function for the given player.

        Parameters
        ----------
        player_id : Any

        Returns
        -------
        Dict[Any, float]
            A map from every terminal node to the utility assigned to it by
            the given player.

        """
        self.__check_player_in_game(player_id)
        utility_i = {}
        for n in self.game_tree.terminal_nodes:
            utility_i[n] = self.utility[n][player_id]
        return utility_i

    def get_available_actions(self, node: Any) -> Set[Any]:
        """Get what actions are available at the given node.

        Parameters
        ----------
        node : Any

        Returns
        -------
        Set[Any]
            Set of available actions according to the game tree.

        """
        actions = set()
        for e in self.game_tree.out_edges(node):
            a = self.game_tree.get_edge_data(*e)['action']
            actions.add(a)
        return actions

    def get_choice_set(self, player_id: Any, information_set: Set[Any]) -> Set[Any]:
        """Get the choice set for some player at some information set.

        Parameters
        ----------
        player_id : Any
        information_set : Set[Any]
          The information set for which the choice set is to be retrieved.

        Returns
        -------
        List[Tuple[Any]]
          List of edges outgoing from every node in the information set.

        """
        self.__check_player_in_game(player_id)
        assert information_set in self.information_partition[player_id], \
            "information set {} does not belong to player {}'s information \
        partition".format(information_set, player_id)
        choice_set = self.get_available_actions(list(information_set)[0])
        return choice_set

    def get_utility_table(self) -> pd.DataFrame:
        """Get a pandas dataframe with the utility for every player.

        Returns
        -------
        utility_table : pandas.DataFrame

        """
        data = {}
        terminal_nodes = self.game_tree.terminal_nodes
        data['Terminal node'] = terminal_nodes
        for pos in self.players:
            data[pos.capitalize()] = [self.utility[n][pos] for n in
                                      terminal_nodes]
        utility_table = pd.DataFrame(data)
        utility_table.set_index('Terminal node', inplace=True)
        return utility_table

    def add_information_sets(
            self,
            player_id: Any,
            *additional_info_sets: Set[Any]
        ) -> None:
        """Add an information set to the partition of the given player.

        This method does not require that all nodes where ``player_id`` takes
        an actions are included in some information set. It does check that all
        the nodes in the information partition to be added belong to the theta
        partition of ``player_id``, and that they have no been previously
        included in some other information set.

        Parameters
        ----------
        player_id : Any
            The game player whose information partition is to be expanded.
        *additional_info_sets : Set[Any]
            The information sets that are to be added.

        """
        self.__check_player_in_game(player_id)

        self.is_perfect_information = False

        # check that the nodes in the information sets belong to the theta
        # partition of the player
        theta_partition = self.get_theta_partition()[player_id]
        # check that the nodes in the additional information sets are not
        # already in the information partition
        all_sets = self.information_partition[player_id]
        info_sets_union = [x for y in all_sets for x in y]
        for s in additional_info_sets:
            for n in s:
                assert n in theta_partition, "node {} not in the turn \
                    function of player {}".format(n, player_id)
                assert n not in info_sets_union, "node {} already in \
                    information partition of player {}".format(n, player_id)

        for s in additional_info_sets:
            self.information_partition[player_id].append(s)

    def set_information_partition(
            self,
            player_id: Any,
            *partition: Set[Any]
        ) -> None:
        """Set the information partition of the given player.

        It is only useful to call this method when modeling games with
        imperfect information, otherwise when nodes are added to the game tree
        perfect information is assumed by default.

        The method checks that all the nodes where it is the player's turn to
        move are included in the information partition, and viceversa, that at
        all the nodes in the various information sets it is the player's turn.
        Also, it checks that all the nodes in any given information set have
        the same number of outgoing edges, and that they are non-terminal.

        Parameters
        ----------
        player_id : Any

        partition : Set[Any]
            Information sets making up the player's information partition.

        Raises
        ------
        AssertionError
            If the union of information sets does not correspon to the same nodes
            where it is the player's turn to play, or
            If some nodes in the same information set have different amounts of
            outgoing edges, or
            If some node is terminal.

        Notes
        -----
        Please note that the method does not check that all the information
        sets provided are disjunct.

        """
        self.__check_player_in_game(player_id)

        self.is_perfect_information = False

        # check that all the nodes where the player plays are included in the
        # information partition
        theta_player = self.get_theta_partition()[player_id]
        nodes_in_info_sets = set()
        for p in partition:
            nodes_in_info_sets.update(p)
        assert theta_player == nodes_in_info_sets, "the information set for\
      player {} is missing some nodes".format(player_id)

        for p in partition:
            # check that all nodes in information set have the same available
            # actions
            all_avail_actions = [self.get_available_actions(n) for n in p]
            assert all(av == all_avail_actions[0] for av in
                       all_avail_actions), "nodes in information set {} have \
                       different available actions".format(p)

            # check that nodes are not terminal
            for n in p:
                self.__check_nonterminal_node(n)

        # replace current partition with the new one
        self.information_partition[player_id] = []
        for p in partition:
            self.information_partition[player_id].append(p)

    def set_probability_distribution(
            self,
            node_id: Any,
            prob_dist: Dict[Tuple[Any], float]
        ) -> None:
        """Set the probabilities over the outgoing edges of a chance node.

        Parameters
        ----------
        node_id : Any
            Node over whose outgoing edges the probability is given.
        prob_dist : Dict[Tuple[Any], float]
            Probability distribution over the outgoing edges of the node.

        Raises
        ------
        ValueError
            If at the given node, it is not chance's turn, or if one of the
            provided edges does not have the given node as origin, or if there
            is some edge going out from the node for which the probability
            is not specified.
        AssertionError
            If the sum of the probabilities over all the edges is not close to
            unity with :math:`10-^{3}` absolute tolerance.

        """
        if self.turn_function[node_id] != 'chance':
            raise ValueError("it is not chance's turn at node {}".
                             format(node_id))
        outgoing_edges = self.game_tree.out_edges(node_id)
        for e in prob_dist.keys():
            if e not in outgoing_edges:
                raise ValueError("edge {} is not an outgoing edge from {}"
                                 .format(e, node_id))
        for e in outgoing_edges:
            if e not in prob_dist.keys():
                raise ValueError("probability not specified for edge {}".
                                 format(e))
        assert np.isclose([sum(prob_dist.values())], [1], atol=1.E-3)[0], \
            "sum over probability distribution of edges must be close to 1"
        self.probability[node_id] = prob_dist

    def set_uniform_probability_distribution(self, node_id: Any) -> None:
        """Set a equal probabilities over the outgoing edges of a chance node.

        Parameters
        ----------
        node_id : Any
            A node where chance takes its turn.

        """
        outgoing_edges = self.game_tree.out_edges(node_id)
        uniform_prob_dist = {e: 1/len(outgoing_edges) for e in outgoing_edges}
        self.set_probability_distribution(node_id, uniform_prob_dist)

    def set_utility(self, node_id: Any, utilities: Dict[Any, float]) -> None:
        """Set the utility for all players at the given terminal node.

        Parameters
        ----------
        node_id : Any
            A terminal node.
        utilities : Dict[Any, float]
            Dictionary that maps every player in the game to the utility it
            assigns to the terminal node.

        """
        self.__check_terminal_node(node_id)
        self.utility[node_id] = {}
        for pos, u in utilities.items():
            self.__check_player_in_game(pos)
            self.utility[node_id][pos] = u

    def get_action_sequence(self, terminal_node: Any) -> Tuple[List[Tuple[str, str]], float]:
        """Get the sequence of actions and probability to a terminal node.

        Parameters
        ----------
        terminal_node : Any
            The terminal node to get the sequence of actions from the root.

        Returns
        -------
        action_sequence : List[Tuple[str,str]]
            The sequence of action from the root to the terminal node, as a
            list of tuples of (player, action).
        probability : float
            The probability of the sequence of actions.

        """
        self.__check_terminal_node(terminal_node)
        paths = list(all_simple_edge_paths(self.game_tree, self.game_tree.root,
                                           terminal_node))
        assert len(paths) == 1, "path search has not return just one single \
                                 path"
        path = paths[0]
        action_sequence = []
        probability = 1
        for (n1, n2) in path:
            active_player = self.turn_function[n1]
            if active_player == 'chance':
                probability *= self.probability[n1][(n1, n2)]
                continue
            action = self.game_tree.get_edge_data(n1, n2)['action']
            action_sequence.append((active_player, action))
        return action_sequence, probability


def hierarchy_pos(
        G: Any,
        root: Any = None,
        width: float = 1.,
        vert_gap: float = 0.2,
        vert_loc: float = 0,
        xcenter: float = 0.5
    ) -> Dict[Any, Tuple[float, float]]:
    """From Joel's answer at https://stackoverflow.com/a/29597209/2966723.

    Licensed under Creative Commons Attribution-Share Alike.

    If the graph is a tree this will return the players to plot this in a
    hierarchical layout.

    Parameters
    ----------
    G : Any
        The graph (must be a tree). In practive, must be an instance of one of
        the classes provided by `networkx`.
    root : Any, optional
        The root node of current branch. The default is None.
        * If the tree is directed and this is not given, the root will be found
        and used.
        * If the tree is directed and this is given, then  the players will be
        just for the descendants of this node.
        * If the tree is undirected and not given, then a random choice will be
        used.
    width : float, optional
        Horizontal space allocated for this branch - avoids overlap with other
        branches. The default is 1..
    vert_gap : float, optional
        Gap between levels of hierarchy. The default is 0.2.
    vert_loc : float, optional
        Vertical location of root. The default is 0.
    xcenter : float, optional
        Horizontal location of root. The default is 0.5.

    Raises
    ------
    TypeError
        If the graph is not a tree.

    Returns
    -------
    Dict[Any, Tuple[float, float]]
        Mapping from every node in the tree to its layout player.

    See Also
    --------
    networkx.is_tree

    """
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a \
                      tree')
    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(
            G: Any,
            root: Any = None,
            width: float = 1.,
            vert_gap: float = 0.2,
            vert_loc: float = 0,
            xcenter: float = 0.5,
            pos: Dict[Any, Tuple[float, float]] = None,
            parent: Any = None):
        """See hierarchy_pos for most arguments.

        Parameters
        ----------
        pos : Dict[Any, Tuple[float, float]]
            A dictionary saying where all nodes go if they have been assigned.
            Default is None.
        parent : Any
            Parent of this branch - only affects it if non-directed.
            Default is None.

        """
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width/len(children)
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc-vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


def plot_game(
        game: ExtensiveFormGame,
        player_colors: Dict[Any, str],
        utility_label_shift: float = 0.03,
        fig_kwargs: Dict[str, Any] = None,
        node_kwargs: Dict[str, Any] = None,
        edge_kwargs: Dict[str, Any] = None,
        edge_labels_kwargs: Dict[str, Any] = None,
        patch_kwargs: Dict[str, Any] = None,
        legend_kwargs: Dict[str, Any] = None,
        draw_utility: bool = True,
        decimals: int = 1,
        utility_label_kwargs: Dict[str, Any] = None,
        info_sets_kwargs: Dict[str, Any] = None
    ) -> plt.Figure:
    """Make a figure of the game tree.

    Encoded information:
        * Node colors encode the turn function at every node.
        * Dashed archs between nodes indicate information sets.
        * Numbers in parenthesis below terminal nodes indicate utilities
          (optional).
    
    Parameters
    ----------
    game : ExtensiveFormGame
        A game in extensive form to be plotted.
    player_colors : Dict[Any, str]
        Dictionary mapping every player in the game to the color to use for the
        nodes where it is the player's turn. Color white is not recommended, as
        it is reserved for chance nodes.
    utility_label_shift : float, optional
        To adjust the utility labels under the terminal nodes.
        The default is 0.03.
    fig_kwargs : Dict[str, Any], optional
        Additional keywork arguments related to the rendering of the figure -
        they are passed to `matplotlib.pyplot.subplots`.
        The default is None.
    node_kwargs : Dict[str, Any], optional
        Additional keyword arguments related to the rendering of the game tree
        nodes - they are passed to `nx.draw_network`.
        The default is None.
    edge_kwargs : Dict[str, Any], optional
        Additional keyword arguments related to the rendering of the game tree
        edges - they are passed to `nx.draw_network`.
        The default is None.
    edge_labels_kwargs : Dict[str, Any], optional
        Additional keyword arguments related to the rendering of the edge
        labels - they are passed to `nx.draw_network_edge_labels`.
        The default is None.
    patch_kwargs : Dict[str, Any], optional
        Additional keyword arguments related to the rendering of the legend
        patches - they are passed to `matplotlib.patches.Patch`.
        The default is None.
    legend_kwargs : Dict[str, Any], optional
        Additional keyword arguments related to the rendering of the legend -
        they are passed to `matplotlib.axes.Axes.legend`.
        The default is None.
    draw_utility : bool, optional
        Whether labels should be drawn below the terminal nodes displaying the
        utilities for all players.
        The default is True.
    decimals : int, optional
        The number of decimals places for the utility labels.
        The default is 1.
    utility_label_kwargs : Dict[str, Any], optional
        Additional keyword arguments related to the rendering of the utility
        labels at the terminal nodes - they are passed to
        `matplotlib.pyplot.text`.
        The default is None.
    info_sets_kwargs : Dict[str, Any], optional
        Additional keyword arguments related to the rendering of the archs
        connecting the information sets - they are passed to
        `matplotlib.patches.Arch`.
        The default is None.

    Returns
    -------
    fig : matplotlib.figure.Figure

    """
    pos = hierarchy_pos(game.game_tree, game.game_tree.root)
    fig, ax = plt.subplots(**fig_kwargs)
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.set_facecolor("white")

    # if there is chance in the game and it does not have a color, set it to
    # white
    if game.get_theta_partition()['chance'] != set():
        if 'chance' not in player_colors.keys():
            player_colors['chance'] = 'white'

    # draw the game tree
    node_col = []
    for n in game.game_tree.nodes:
        if n in game.game_tree.terminal_nodes:
            col = 'silver'
        else:
            player = game.turn_function[n]
            col = player_colors[player]
        node_col.append(col)
    nx.draw_networkx(game.game_tree, pos=pos, ax=ax, with_labels=True,
                     node_color=node_col, **node_kwargs, **edge_kwargs)

    # prepare edge labels
    edge_labels = {}
    for e in game.game_tree.edges:
        label = game.game_tree.get_edge_data(*e)['action']
        parent_node = e[0]
        parent_player = game.turn_function[parent_node]
        # if edge is action from chance, add probability
        if parent_player == 'chance':
            prob = game.probability[parent_node][e]
            label += ' ({:.2f})'.format(prob)
        edge_labels[e] = label
    # draw edge labels
    nx.draw_networkx_edge_labels(game.game_tree, pos=pos, ax=ax,
                                 edge_labels=edge_labels, **edge_labels_kwargs)

    # draw legend
    handles = []
    for player, col in player_colors.items():
        patch = mpatches.Patch(color=col, label=player, **patch_kwargs)
        patch.set_edgecolor('black')
        handles.append(patch)
    ax.legend(handles=handles, **legend_kwargs)

    # draw utility on terminal nodes
    if draw_utility:
        terminal_nodes = game.game_tree.terminal_nodes
        for n in terminal_nodes:
            utility_label_player = (pos[n][0], pos[n][1]-utility_label_shift)
            utilities_node = ["{:.{prec}f}".
                              format(game.utility[n][p],
                                     prec=decimals) for p in game.players
                              if p != 'chance']
            utility_label = '{}'.format('\n'.join(utilities_node))
            plt.text(*utility_label_player, utility_label, ha='center',
                     va='bottom', **utility_label_kwargs)

    # draw archs between nodes in the same information set
    for player in game.players:
        if player == 'chance':
            continue
        for info_set in game.information_partition[player]:
            if len(info_set) == 1:
                continue
            for u, v in combinations(info_set, r=2):
                x = (pos[u][0] + pos[v][0])/2
                y = (pos[u][1] + pos[v][1])/2
                width = abs(pos[u][0] - pos[v][0])
                height = 0.1
                arch = mpatches.Arc((x, y), width, height, theta1=0,
                                    theta2=180,
                                    edgecolor=player_colors[player],
                                    fill=False, **info_sets_kwargs)
                ax.add_patch(arch)

    plt.show()
    plt.close(fig)
    return fig


def backward_induction(
        game: ExtensiveFormGame,
        h: Any,
        u_dict: Dict[Any, Dict[Any, float]] = {}
    ) -> Dict[Any, Dict[Any, float]]:
    """Compute the value of node `h` in a subgame by backward induction.

    It computes the values of all the nodes in the subgame having `h` as its
    root node. Only for games with perfect information.

    Parameters
    ----------
    game : ExtensiveFormGame
        A game in extensive forms. Must be a perfect information game without
        any stochastic effects (no `chance` nodes).
    h : Any
        The root of the subgame where to start computing.
    u_dict : Dict[Any, Dict[Any, float]], optional
        A dictionary of the values for every player at the nodes that have
        already been revisited. The default is {}, and it should not be
        modified. It is necessary to perform the recursion.

    Returns
    -------
    Dict[Any, Dict[Any, float]]
        A dictionary mapping, for each visited node (all the descendants of
        `h`), the value assigned to it by every player in the game.

    """
    if h in game.game_tree.terminal_nodes:
        u_dict[h] = game.utility[h]
        return u_dict
    player = game.turn_function[h]
    if player == 'chance':
        u = {p: 0. for p in game.players}
    else:
        u = {p: -float('inf') for p in game.players}
    u_dict[h] = u
    for e in game.game_tree.out_edges(h):
        child = e[1]
        u_child = backward_induction(game, child, u_dict)[child]
        if player == 'chance':
            prob_edge = game.probability[h][e]
            for pos in game.players:
                u[pos] += prob_edge*u_child[pos]
        else:
            if u_child[player] > u[player]:
                u = u_child
    u_dict[h] = u
    return u_dict


def subgame_perfect_equilibrium_pure(game: ExtensiveFormGame) -> Dict[Any, Any]:
    """Find a subgame perfect equilibrium in pure strategies.

    Parameters
    ----------
    game : ExtensiveFormGame
        The game in extensive form.

    Returns
    -------
    SPE : Dict[Any, Any]
        A subgame perfect equilibrium in pure strategies, mapping each nodes to
        the action to be taken.

    """
    values_dict = backward_induction(game, game.game_tree.root)
    SPE = {}
    for n in game.game_tree.nodes:
        if n in game.game_tree.terminal_nodes:
            continue
        player = game.turn_function[n]
        if player == 'chance':
            continue
        next_value = -float('inf')
        action = None
        for e in game.game_tree.out_edges(n):
            child = e[1]
            if values_dict[child][player] > next_value:
                next_value = values_dict[child][player]
                action = (e, game.game_tree.get_edge_data(*e)['action'])
        SPE[n] = action
    return SPE


def DFS_equilibria_paths(
        game: ExtensiveFormGame,
        h: Any,
        pure_strategy: Dict[Any, Any],
        path: List[Any],
        probability: float,
        path_store: List[Tuple[List[Any], float]]
    ) -> None:
    """Find all the equilibrium paths.

    This function finds all of the paths given the deterministic strategy and
    considering the chance nodes, and stores (path, probability) tuples in a
    `store`.

    Parameters
    ----------
    game : ExtensiveFormGame
        The game being played.
    h : Any
        The node where play starts.
    pure_strategy : Dict[Any, Any]
        A dictionary mapping every decision node to the (edge, action) pair to
        be followed.
    path : List[Any]
        The path played before reaching the current node.
    probability : float
        The probability of playing the path played before reaching the current
        node.
    path_store : List[Tuple[List[Any], float]]
        A store where the computed paths are stores alongside with their
        probabilities of being played.

    Examples
    --------
    The intended way to call this function is:
    >>> path_store = []
    >>> DFS_equilibria_paths(game, game.game_tree.root, pure_strat, [], 1, path_store)
    >>> print(path_store)

    """
    path.append(h)
    # if the current node is a decision node
    if h in pure_strategy.keys():
        next_node = pure_strategy[h][0][1]
        action = pure_strategy[h][1]
        path.append(action)
        DFS_equilibria_paths(game, next_node, pure_strategy, path, probability,
                             path_store)
    # if the current node is a chance node
    elif h in game.turn_function.keys() and game.turn_function[h] == 'chance':
        prob_until_chance = probability
        for e in game.game_tree.out_edges(h):
            path_until_chance = deepcopy(path)
            next_node = e[1]
            action = game.game_tree.get_edge_data(*e)['action']
            path_until_chance.append(action)
            prob = prob_until_chance*game.probability[h][e]
            DFS_equilibria_paths(game, next_node, pure_strategy,
                                 path_until_chance, prob, path_store)
    # if current node is terminal, append path to the store
    else:
        path_store.append((path, probability))


def build_subgame(extensive_game: ExtensiveFormGame, root: int) -> NormalFormGame:
    """Build a normal game that emanates from a node in an extensive game.

    Assumes that the root from which the normal form game is built corresponds
    to the root of the last round of the extensive game.

    Parameters
    ----------
    extensive_game : ExtensiveFormGame
    root : int
        The root from which a last rounds of the extensive game starts.

    Raises
    ------
    AssertionError
        If a descendant of a chance node is not terminal.
    ValueError
        If a path of play does not end at a chance or at a terminal node.

    Returns
    -------
    normal_form_game : NormalFormGame
        The game in normal form corresponding that starts at the input root
        node.

    """
    # get the players and their possible actions
    player_actions = {}
    n = root
    while True:
        try:
            active_player = extensive_game.turn_function[n]
            if active_player == 'chance':
                break
        # KeyError happens if terminal node is reached, not in the turn
        # function
        except KeyError:
            break

        out_edges = list(extensive_game.game_tree.out_edges(n, data='action'))
        actions = tuple(o[2] for o in out_edges)
        player_actions[active_player] = actions
        n = out_edges[0][1]

    players = extensive_game.players
    actions = []
    for p in players:
        try:
            actions.append(player_actions[p])
        except KeyError:
            actions.append(('no-op',))

    # build the payoff function
    payoff_function = {}
    non_empty_actions = [a for a in actions if a]
    possible_play_paths = product(*non_empty_actions)

    # scan through the possible paths of play
    for p in possible_play_paths:
        n = root
        for action in p:
            if action == 'no-op':
                continue
            out_edges = list(extensive_game.game_tree.out_edges(n,
                                                                data='action'))
            next_node = [o[1] for o in out_edges if o[2] == action][0]
            n = next_node

        # last node of play path is a terminal node
        if n in extensive_game.game_tree.terminal_nodes:
            utility = tuple(extensive_game.utility[n][p] for p in players)

        # last node of play path is a chance node: weight average over
        # descendant terminal nodes
        elif extensive_game.turn_function[n] == 'chance':
            utility_dict = {pl: 0 for pl in players}
            for (_, desc), prob in extensive_game.probability[n].items():
                assert desc in extensive_game.game_tree.terminal_nodes,\
                    "node {} should be a terminal node".format(desc)
                for pl in players:
                    utility_dict[pl] += prob*extensive_game.utility[desc][pl]
            utility = tuple(utility_dict[pl] for pl in players)

        else:
            raise ValueError("node at end of path play {} from root node {} \
                        is not a terminal nor a chance node".format(p, root))

        payoff_function[p] = utility

    normal_form_game = NormalFormGame(
        players=players,
        actions=actions,
        payoff_function=payoff_function
    )

    return normal_form_game


def scalar_function(x: List[float]) -> float:
    """Function to be minimized: total deviation incentives for all players.

    Written in a format such that the only input is a mixed strategy encoded
    as a numpy.array.

    Parameters
    ----------
    x : List[float]
        Array encoding a mixed strategy. The game to which it is to be applied
        is set as an attribute of the function externally

    Raises
    ------
    AttributeError
        If, at the time of being called, no normal-form game has been set as an
        attribute, to which the mixed strategy array encoded in the array is
        passed to compute the incentives to deviate.

    Returns
    -------
    f : float
        The function to be minimixed, i.e. the total incentive to deviate from
        the mixed strategy:

        .. math::

            f(s) = \sum\limits_{i \in G} \sum\limits_{j \in A_j} (d_i^j(s))^2

    References
    ----------
    Shohan, Y., & Leyton-Browm, K. (2009). Computing Solution Concepts of
    Normal-Form Games. In Multiagent Systems: Algorithmic, Game-Theoretic,
    and Logical Foundations (pp. 87–112). Cambridge University Press.

    """
    if not scalar_function.game:
        raise AttributeError("scalar_function() called without game attribute")
    mixed_strat = scalar_function.game.strategies_vec2dic(x)
    f = scalar_function.game.incentive_target_function(mixed_strat)
    return f


def minimize_incentives(
        normal_game: NormalFormGame
    ) -> Tuple[Dict[Any, Dict[Any, float]], float]:
    """Compute the mixed strategy that minimizes the incentive to deviate.

    Given an arbitrary normal-form game, compute the (in general, mixed)
    strategy profile that minimizes the incentives to deviate from all players.
    The target function being minimized is:

    .. math::

        f(s) = \sum\limits_{i \in G} \sum\limits_{j \in A_j} (d_i^j(s))^2 \\
        c_{i}^{j}(s) = u_i(a_{j}^{i}, s_{-j}) - u_i(s) \\
        d_{i}^{j}(s) = max(c_{i}^{j}(s), 0)

    It uses the scipy.optimize library to solve the optimization problem. In
    particular, their implementation of the Trust-Region Constrained algorithm.

    Parameters
    ----------
    normal_game : NormalFormGame

    Raises
    ------
    ValueError
        If the optimization (i.e. the call to ``scipy.optimize.minimize``) is
        not successfull.

    Returns
    -------
    Dict[Any, Dict[Any, float]]
        The mixed strategy that minimizes the total incentives to deviate, as a
        dictionary mapping every player in the game to a mixed strategy.
    float
        The target function at the solution.

    """

    # set attribute of the function to minimize, since it can only take a
    # vector array as argument
    setattr(scalar_function, 'game', normal_game)

    x0 = normal_game.completely_random_strat_vector()
    linear_constraints = normal_game.make_linear_constraints()
    bounds = normal_game.make_strat_bounds()

    opt = minimize(scalar_function,
                   x0,
                   method='SLSQP',
                   constraints=[linear_constraints],
                   options={'ftol': 1.E-8},
                   bounds=bounds)

    delattr(scalar_function, 'game')

    # check that the minimization has been successful
    if not opt.success:
        raise ValueError(opt.message)

    # from vector to mixed strategy dictionary
    mixed_strat_solution = normal_game.strategies_vec2dic(opt.x)

    # return the mixed strategy and the value of the target function
    return mixed_strat_solution, opt.fun


def subgame_perfect_equilibrium(
        extensive_form_game: ExtensiveFormGame,
        equilibrium_function: Callable
    ) -> Tuple[Dict[Any, Any], Dict[Any, Any], Dict[Any, Any]]:
    """Compute the sequential equilibriums in an Extensive Form Game.

    This function works on an Extensive Form Game built as a sequence of,
    possibly different, Normal Form Games. This function identifies the
    subgames starting from those closer to the end of the game (i.e. to the
    root nodes), and passes them to ``build_subgame`` to build that part of
    the game tree as a normal form game. Then, it calls the provided
    equilibrium function to find the mixed strategy incentivized in that
    subgame, and backtracks the resulting utility up the game tree.

    Parameters
    ----------
    extensive_form_game : ExtensiveFormGame
    equilibrium_function : Callable
        The function that computes a solution concept on a (single-rounds)
        normal form game. It should return the result as a dictionary with
        the game players as keys, and a dictionary mapping their available
        actions to the probabilities as values.

    Returns
    -------
    subgame_mixed_strategies : Dict[Any, Any]
        The mapping from the nodes that are the roots of the subgames to the
        mixed equilibrium strategies computed for their subgame.
    backtrack_utilities : Dict[Any, Any]
        The mapping from the nodes that are the roots of the subgames to the
        utilities resulting from the computed equilibrium strategies.
    target_function : Dict[Any, Any]
        Mapping from the nodes that are roots of the sequential normal-form
        games to the optimized deviation incentive function, which should
        ideally be ~0 for all nodes.

    """
    extensive_game = deepcopy(extensive_form_game)
    max_rounds = max(extensive_game.node_rounds.values())
    subgame_mixed_strategies = {}
    backtrack_utilities = {}
    target_function = {}
    subgame_rounds = max_rounds-1

    while subgame_rounds >= 0:
        subgame_root_nodes = [
            n for n in extensive_game.node_rounds.keys()
            if extensive_game.node_rounds[n] == subgame_rounds
            and n not in extensive_game.game_tree.terminal_nodes
        ]

        # compute equilibrium at the subgames closest to the terminal nodes
        for s in subgame_root_nodes:
            # build the last subgame as an extensive form game
            normal_game = build_subgame(extensive_game, s)

            # function to compute the mixed strategy equilibrium here
            mixed_equilibrium_strategy, f = equilibrium_function(normal_game)

            subgame_mixed_strategies[s] = mixed_equilibrium_strategy
            target_function[s] = f

            # store utility at the root node of the subgame
            mes_list = [mixed_equilibrium_strategy[p] for p in
                        normal_game.players]
            rewards = normal_game.mixed_strategies_rewards(*mes_list)
            backtrack_utilities[s] = {p: r for p, r in
                                      zip(normal_game.players, rewards)}

        for s in subgame_root_nodes:
            # delete all descendants from subgame root nodes
            desc = descendants(extensive_game.game_tree, s)
            extensive_game.game_tree.remove_nodes_from(desc)

            # remove previous terminal nodes from terminal list
            terminal_previous = [d for d in desc
                                 if d in
                                 extensive_game.game_tree.terminal_nodes]
            for t in terminal_previous:
                extensive_game.game_tree.terminal_nodes.remove(t)
            extensive_game.game_tree.terminal_nodes.append(s)

            # remove previous non-terminal nodes from turn function
            for d in desc:
                if d in extensive_game.turn_function.keys():
                    extensive_game.turn_function.pop(d)

            # remove subgame root node from turn function because now it is
            # terminal
            extensive_game.turn_function.pop(s)

            # backtrack utility
            extensive_game.set_utility(s, backtrack_utilities[s])

        subgame_rounds -= 1

    return subgame_mixed_strategies, backtrack_utilities, target_function


def outcome_probability(
        extensive_game: ExtensiveFormGame,
        rounds_strat: Dict[Any, Any],
        outcome_node: Any
    ) -> float:
    """Compute the probability of reaching a terminal node.

    Compute the probability that a terminal node is reached given the
    strategies of players at the consecutive game rounds.

    Parameters
    ----------
    extensive_game : ExtensiveFormGame
        The game in extensive form where the path and probability of play is
        to be computed.
    rounds_strat : Dict[Any, Any]
        The mixed strategies at every round of the game, equivalent to a
        normal form game.
    outcome_node : Any
        The terminal node towards which the path of play is to be computed.

    Returns
    -------
    float

    """
    assert outcome_node in extensive_game.game_tree.terminal_nodes, \
        "node {} is not a terminal node".format(outcome_node)
    path_from_root = shortest_path(extensive_game.game_tree,
                                   extensive_game.game_tree.root, outcome_node)
    probability = 1
    for i in range(len(path_from_root)-1):
        n = path_from_root[i]
        # retrieve the strategy that applies to that part of the game
        if n in rounds_strat.keys():
            local_strategy = rounds_strat[n]

        player = extensive_game.turn_function[n]
        next_node = path_from_root[i+1]

        if player == 'chance':
            action_prob = extensive_game.probability[n][(n, next_node)]
            pass
        else:
            a = extensive_game.game_tree.get_edge_data(n, next_node, 'action')
            action = a['action']
            action_prob = local_strategy[player][action]
        probability *= action_prob
        if probability == 0:
            return 0
    return probability


if __name__ == '__main__':
    print(prisoners_dilemma)
    print(rock_paper_scissors)
    pass
