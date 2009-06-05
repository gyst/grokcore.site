##############################################################################
#
# Copyright (c) 2006-2009 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

from grokcore.component.interfaces import IContext

from persistent import Persistent

from zope.interface import implements

from zope.app.component.site import SiteManagerContainer

from zope.app.container.contained import Contained


class Site(SiteManagerContainer):
    """Mixin for creating sites in Grok applications.

    When an application `grok.Model` or `grok.Container` also inherits
    from `grok.Site`, then it can additionally support the registration
    of local Component Architecture entities like `grok.LocalUtility`
    and `grok.Indexes` objects; see those classes for more information.

    """


class LocalUtility(Contained, Persistent):
    """The base class for local utilities in Grok applications.

    Although application developers can create local utilies without
    actually subclassing `grok.LocalUtility`, they gain three benefits
    from doing so.  First, their code is more readable because their
    classes "look like" local utilities to casual readers.  Second,
    their utility will know how to persist itself to the Zope database,
    which means that they can set its object attributes and know that
    the values are getting automatically saved.  Third, they can omit
    the `grok.provides()` directive naming the interface that the
    utility provides, if their class only `grok.implements()` a single
    interface (unless the interface is one that the `grok.LocalUtility`
    already implements, in which case Grok cannot tell them apart, and
    `grok.provides()` must be used explicitly anyway).

    """
    implements(IContext)
