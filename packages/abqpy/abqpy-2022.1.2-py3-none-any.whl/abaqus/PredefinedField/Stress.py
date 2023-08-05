from .PredefinedField import PredefinedField
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


class Stress(PredefinedField):
    """The Stress object stores the data for an initial stress predefined field.
    The Stress object is derived from the PredefinedField object.

    .. note::
        This object can be accessed by:

        .. code-block:: python

            import load
            mdb.models[name].predefinedFields[name]

        The corresponding analysis keywords are:

        - INITIAL CONDITIONS

    """

    def __init__(
        self,
        name: str,
        region: Region,
        distributionType: SymbolicConstant = UNIFORM,
        sigma11: float = None,
        sigma22: float = None,
        sigma33: float = None,
        sigma12: float = None,
        sigma13: float = None,
        sigma23: float = None,
    ):
        """This method creates a Stress predefined field object.

        .. note::
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].Stress

        Parameters
        ----------
        name
            A String specifying the repository key.
        region
            A Region object specifying the region to which the predefined field is applied. Region
            is ignored if the predefined field has *distributionType*=FROM_FILE.
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM
            and FROM_FILE. The default value is UNIFORM.
        sigma11
            A Float specifying the first principal component of the stress.
        sigma22
            A Float specifying the second principal component of the stress.
        sigma33
            A Float specifying the third principal component of the stress.
        sigma12
            A Float specifying the first shear component of the stress.
        sigma13
            A Float specifying the second shear component of the stress.
        sigma23
            A Float specifying the third shear component of the stress.

        Returns
        -------
            A Stress object.
        """
        super().__init__()

    def setValues(
        self,
        distributionType: SymbolicConstant = UNIFORM,
        sigma11: float = None,
        sigma22: float = None,
        sigma33: float = None,
        sigma12: float = None,
        sigma13: float = None,
        sigma23: float = None,
    ):
        """This method modifies the Stress object.

        Parameters
        ----------
        distributionType
            A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM
            and FROM_FILE. The default value is UNIFORM.
        sigma11
            A Float specifying the first principal component of the stress.
        sigma22
            A Float specifying the second principal component of the stress.
        sigma33
            A Float specifying the third principal component of the stress.
        sigma12
            A Float specifying the first shear component of the stress.
        sigma13
            A Float specifying the second shear component of the stress.
        sigma23
            A Float specifying the third shear component of the stress.
        """
        ...
