from mesa import Model
from valalgn.sampling import create_app

from typing import Any


class YourModel(Model):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """An ABM whose evolution is determined by a set of norms."""
        super().__init__(*args, **kwargs)

    def step(
        self,
        norms: dict[str, dict[str, Any]]
    ) -> None:
        """The model evolves according to the set of norms in place.

        By having the norms as an input to the model's ``step()`` method, it is
        possible to model changes in the implemented normative system while the
        model is still running.

        Parameters
        ----------
        norms : Dict[Any, Dict[Any, Any]]
            A map of the norms governing the evolution of the model at that
            step. This map is provided as a dictionary from norm identifiers
            (keys) to a dictionary mapping each of the norms' parameters to
            their values.

        Raises
        ------
        NotImplementedError
        """
        raise NotImplementedError
    

def your_value_semantics_funcion(mdl: YourModel) -> float:
    """Value semantics function.

    Parameters
    ----------
    mdl : YourModel

    Returns
    -------
    float
        The degree of respect for the value at the current state of the model.

    Raises
    ------
    NotImplementedError
    """
    raise NotImplementedError


if __name__ == '__main__':
    app = create_app(
        'shapley',
        YourModel,
        your_value_semantics_funcion,
        model_args=[...],
        model_kwargs={...}
    )
    app.run()
