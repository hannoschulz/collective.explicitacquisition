from zExceptions import NotFound
from ZPublisher.interfaces import IPubAfterTraversal

from zope.component import adapter
from Products.CMFCore.interfaces import IContentish

from Products.CMFPlone.interfaces import IPublishableThroughAcquisition



@adapter(IPubAfterTraversal)
def avoid_acquired_content(event):
    request = event.request
    parents = request['PARENTS']
    context = parents[0]
    if IPublishableThroughAcquisition.providedBy(context):
        return
    if IContentish.providedBy(context):
        parent_ids = [item.getId() for item in parents]
        parent_ids.reverse()
        acquired = parent_ids != list(context.getPhysicalPath())
        if acquired:
            raise NotFound(request.URL)
