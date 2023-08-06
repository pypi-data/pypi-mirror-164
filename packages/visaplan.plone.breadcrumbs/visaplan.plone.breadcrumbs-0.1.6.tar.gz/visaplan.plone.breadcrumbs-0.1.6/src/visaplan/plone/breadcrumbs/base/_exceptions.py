# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
"""\
visaplan.plone.breadcrumbs: .base._exceptions
"""
# ---------------- [ Brotkrümel-Registry: Exception-Klassen ... [
class BreadcrumbsException(Exception):
    pass


class NoCrumbsException(BreadcrumbsException):
    """
    Keine Breadcrumbs für diesen Request
    """
    def __init__(self, cls, id):
        self.cls = cls
        self._id = id

    def __str__(self):
        return '%s(%s, %r)' % (
                self.__class__.__name__,
                self.cls,
                self._id,
                )


class SkipCrumbException(BreadcrumbsException):
    """
    Diesen Krümel nicht erzeugen
    (noch nicht verwendet)

    Die Krümelklasse --> SkipCrumb verwenden, um für bekannte Requests keinen
    Krümel für die Aufrufmethode zu erzeugen (wohl aber ggf. für den Kontext)
    """
# ---------------- ] ... Brotkrümel-Registry: Exception-Klassen ]
