from ..UtilityAndView.abaqusConstants import *


class Regularization:
    """The Regularization object defines the tolerance to be used for regularizing material
    data.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].regularization
            import odbMaterial
            session.odbs[name].materials[name].regularization

        The corresponding analysis keywords are:

        - DASHPOT
    """

    #: A Float specifying the tolerance to be used for regularizing material data. The default
    #: value is 0.03.
    rtol: float = 0

    #: A SymbolicConstant specifying the form of regularization of strain-rate-dependent
    #: material data. Possible values are LOGARITHMIC and LINEAR. The default value is
    #: LOGARITHMIC.
    strainRateRegularization: SymbolicConstant = LOGARITHMIC

    def __init__(
        self, rtol: float = 0, strainRateRegularization: SymbolicConstant = LOGARITHMIC
    ):
        """This method creates a Regularization object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].Regularization
                session.odbs[name].materials[name].Regularization

        Parameters
        ----------
        rtol
            A Float specifying the tolerance to be used for regularizing material data. The default
            value is 0.03.
        strainRateRegularization
            A SymbolicConstant specifying the form of regularization of strain-rate-dependent
            material data. Possible values are LOGARITHMIC and LINEAR. The default value is
            LOGARITHMIC.

        Returns
        -------
        Regularization
            A :py:class:`~abaqus.Material.Regularization.Regularization` object.

        Raises
        ------
        RangeError
        """
        ...

    def setValues(self, *args, **kwargs):
        """This method modifies the Regularization object.

        Raises
        ------
        RangeError
        """
        ...
