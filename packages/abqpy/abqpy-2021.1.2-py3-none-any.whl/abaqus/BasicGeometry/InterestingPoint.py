from .Edge import Edge
from ..UtilityAndView.abaqusConstants import *


class InterestingPoint:
    """Interesting points can be located at the following:
    - The middle of an edge.
    - The middle of an arc.
    - The center of an arc.
    An :py:class:`~abaqus.BasicGeometry.InterestingPoint.InterestingPoint` object is a temporary object and cannot be accessed from the Mdb
    object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import part
            import assembly
    """

    def __init__(self, edge: Edge, rule: SymbolicConstant):
        """This method creates an interesting point along an edge. An InterestingPoint is a
        temporary object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].parts[name].InterestingPoint
                mdb.models[name].rootAssembly.instances[name].InterestingPoint

        Parameters
        ----------
        edge
            An :py:class:`~abaqus.BasicGeometry.Edge.Edge` object specifying the edge on which the interesting point is positioned.
        rule
            A SymbolicConstant specifying the position of the interesting point. Possible values are
            MIDDLE or CENTER.

        Returns
        -------
        InterestingPoint
            An :py:class:`~abaqus.BasicGeometry.InterestingPoint.InterestingPoint` object.

        """
        ...
