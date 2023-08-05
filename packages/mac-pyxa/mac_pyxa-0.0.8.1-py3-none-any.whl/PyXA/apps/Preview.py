""".. versionadded:: 0.0.1

Control the macOS Preview application using JXA-like syntax.
"""

from enum import Enum
from typing import List, Tuple, Union
from AppKit import NSURL

from PyXA import XABase
from PyXA import XABaseScriptable
from ..XAProtocols import XACanOpenPath, XAClipboardCodable, XACloseable, XAPrintable

class XAPreviewApplication(XABaseScriptable.XASBApplication, XACanOpenPath):
    """A class for managing and interacting with Preview.app.

    .. seealso:: :class:`XAPreviewWindow`, :class:`XAPreviewDocument`

    .. versionadded:: 0.0.1
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.xa_wcls = XAPreviewWindow

        self.frontmost: bool #: Whether Preview is the active application
        self.name: str #: The name of the application
        self.version: str #: The version of Preview.app

    @property
    def frontmost(self) -> bool:
        return self.xa_scel.frontmost()

    @property
    def name(self) -> str:
        return self.xa_scel.name()

    @property
    def version(self) -> str:
        return self.xa_scel.version()

    def print(self, path: Union[str, NSURL], show_prompt: bool = True):
        """Opens the print dialog for the file at the given path, if the file can be opened in Preview.

        :param path: The path of the file to print.
        :type path: Union[str, NSURL]
        :param show_prompt: Whether to show the print dialog or skip directly printing, defaults to True
        :type show_prompt: bool, optional

        .. versionadded:: 0.0.1
        """
        if isinstance(path, str):
            path = NSURL.alloc().initFileURLWithPath_(path)
        self.xa_scel.print_printDialog_withProperties_(path, show_prompt, None)

    # Documents
    def documents(self, filter: dict = None) -> 'XAPreviewDocumentList':
        """Returns a list of documents matching the filter.

        :Example 1: List all documents

        >>> import PyXA
        >>> app = PyXA.application("Preview")
        >>> print(app.documents())
        <<class 'PyXA.apps.Preview.XAPreviewDocumentList'>['Example1.pdf', 'Example2.pdf']>

        .. versionchanged:: 0.0.4

           Now returns an object of :class:`XAPreviewDocumentList` instead of a default list.

        .. versionadded:: 0.0.1
        """
        return self._new_element(self.xa_scel.documents(), XAPreviewDocumentList, filter)


class XAPreviewWindow(XABaseScriptable.XASBPrintable):
    """A class for managing and interacting with Preview windows.

    .. seealso:: :class:`XAPreviewApplication`

    .. versionadded:: 0.0.1
    """
    def __init__(self, properties):
        super().__init__(properties)

        self.properties: dict #: All properties of the window
        self.bounds: Tuple[Tuple[int, int], Tuple[int, int]] #: The bounding rectangle of the window
        self.closeable: bool #: Whether the window has a close button
        self.document: XAPreviewDocument #: The document currently displayed in the window
        self.floating: bool #: WHether the window floats
        self.id: int #: The unique identifier for the window
        self.index: int #: The index of the window in the front-to-back ordering
        self.miniaturizable: bool #: Whether the window can be minimized
        self.miniaturized: bool #: Whether the window is currently minimized
        self.modal: bool #: Whether the window is a modal view
        self.name: str #: The title of the window
        self.resizable: bool #: Whether the window can be resized
        self.titled: bool #: Whether the window has a title bar
        self.visible: bool #: Whether the window is currently visible
        self.zoomable: bool #: Whether the window can be zoomed
        self.zoomed: bool #: Whether the window is currently zoomed

    @property
    def properties(self) -> dict:
        return self.xa_elem.properties()

    @property
    def bounds(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        return self.xa_elem.bounds()

    @property
    def closeable(self) -> bool:
        return self.xa_elem.closeable()

    @property
    def document(self) -> 'XAPreviewDocument':
        return self._new_element(self.xa_elem.document(), XAPreviewDocument)

    @property
    def floating(self) -> bool:
        return self.xa_elem.floating()

    @property
    def id(self) -> int:
        return self.xa_elem.id()

    @property
    def index(self) -> int:
        return self.xa_elem.index()

    @property
    def miniaturizable(self) -> bool:
        return self.xa_elem.miniaturizable()

    @property
    def miniaturized(self) -> bool:
        return self.xa_elem.miniaturized()

    @property
    def modal(self) -> bool:
        return self.xa_elem.modal()

    @property
    def name(self) -> str:
        return self.xa_elem.name()

    @property
    def resizable(self) -> bool:
        return self.xa_elem.resizable()

    @property
    def titled(self) -> bool:
        return self.xa_elem.titled()

    @property
    def visible(self) -> bool:
        return self.xa_elem.visible()

    @property
    def zoomable(self) -> bool:
        return self.xa_elem.zoomable()

    @property
    def zoomed(self) -> bool:
        return self.xa_elem.zoomable()


class XAPreviewDocumentList(XABase.XAList, XAClipboardCodable):
    """A wrapper around lists of documents that employs fast enumeration techniques.

    All properties of documents can be called as methods on the wrapped list, returning a list containing each documents's value for the property.

    .. versionadded:: 0.0.4
    """
    def __init__(self, properties: dict, filter: Union[dict, None] = None):
        super().__init__(properties, XAPreviewDocument, filter)

    def properties(self) -> List[dict]:
        return list(self.xa_elem.arrayByApplyingSelector_("properties"))

    def name(self) -> List[str]:
        return list(self.xa_elem.arrayByApplyingSelector_("name"))

    def path(self) -> List[XABase.XAPath]:
        ls = self.xa_elem.arrayByApplyingSelector_("path")
        return [XABase.XAPath(x) for x in ls]

    def modified(self) -> List[str]:
        return list(self.xa_elem.arrayByApplyingSelector_("modified"))

    def by_properties(self, properties: dict) -> 'XAPreviewDocument':
        return self.by_property("properties", properties)

    def by_name(self, name: str) -> 'XAPreviewDocument':
        return self.by_property("name", name)

    def by_path(self, path: XABase.XAPath) -> 'XAPreviewDocument':
        return self.by_property("path", str(path.xa_elem))

    def by_modified(self, modified: bool) -> 'XAPreviewDocument':
        return self.by_property("modified", modified)

    def get_clipboard_representation(self) -> List[NSURL]:
        """Gets a clipboard-codable representation of each document in the list.

        When the clipboard content is set to a document, each documents's file URL is added to the clipboard.

        :return: The document's file URL
        :rtype: List[NSURL]

        .. versionadded:: 0.0.8
        """
        paths = self.path()
        return [x.xa_elem for x in paths]

    def __repr__(self):
        return "<" + str(type(self)) + str(self.name()) + ">"
    
class XAPreviewDocument(XABase.XATextDocument, XAPrintable, XACloseable, XAClipboardCodable):
    """A class for managing and interacting with documents in Preview.

    .. seealso:: :class:`XAPreviewApplication`

    .. versionadded:: 0.0.1
    """
    def __init__(self, properties):
        super().__init__(properties)
        self.properties: dict #: All properties of the document
        self.name: str #: The name of the document
        self.path: str #: The document's file path
        self.modified: bool #: Whether the document has been modified since the last save

    @property
    def properties(self) -> dict:
        return self.xa_elem.properties()

    @property
    def name(self) -> str:
        return self.xa_elem.name()

    @property
    def path(self) -> XABase.XAPath:
        return XABase.XAPath(self.xa_elem.path())

    @property
    def modified(self) -> bool:
        return self.xa_elem.modified()

    def print(self, print_properties: Union[dict, None] = None, show_dialog: bool = True) -> 'XAPreviewDocument':
        """Prints the document.

        :param print_properties: Properties to set for printing, defaults to None
        :type print_properties: Union[dict, None], optional
        :param show_dialog: Whether to show the print dialog, defaults to True
        :type show_dialog: bool, optional
        :return: The document object
        :rtype: XAPreviewDocument

        .. versionadded:: 0.0.4
        """
        if print_properties is None:
            print_properties = {}
        self.xa_elem.print_printDialog_withProperties_(self.xa_elem, show_dialog, print_properties)
        return self

    def save(self, file_path: str = None):
        """Saves the document.
        
        If a file path is provided, Preview will attempt to save the file with the specified file extension at that path. If automatic conversion fails, the document will be saved in its original file format. If no path is provided, the document is saved at the current path for the document.

        :Example 1: Save a PDF (or any compatible document) as a PNG

        >>> import PyXA
        >>> app = PyXA.application("Preview")
        >>> doc = app.documents()[0] # A PDF
        >>> # Save to Downloads to avoid permission errors
        >>> doc.save("/Users/steven/Downloads/Example.png")
        
        .. versionadded:: 0.0.4
        """
        self.xa_elem.saveAs_in_(None, file_path)

    def get_clipboard_representation(self) -> NSURL:
        """Gets a clipboard-codable representation of the document.

        When the clipboard content is set to a document, the documents's file URL is added to the clipboard.

        :return: The document's file URL
        :rtype: NSURL

        .. versionadded:: 0.0.8
        """
        return self.path.xa_elem

    def __repr__(self):
        return self.name