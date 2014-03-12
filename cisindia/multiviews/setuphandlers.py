from collective.grok import gs
from cisindia.multiviews import MessageFactory as _

@gs.importstep(
    name=u'cisindia.multiviews', 
    title=_('cisindia.multiviews import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('cisindia.multiviews.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
