from collective.portlet.collectionmultiview import BaseRenderer
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.interface import Interface
from zope import schema
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget

class FeaturedRenderer(BaseRenderer):

    title = 'Featured Renderer'
    template = ViewPageTemplateFile('/templates/featured.pt')

class ImageListingRenderer(BaseRenderer):

    title = 'Image Listing Renderer'
    template = ViewPageTemplateFile('/templates/image_listing.pt')


class ILeadSummaryRendererSchema(Interface):
    more_text = schema.TextLine(
        title=u'Title for "More" link',
        default=u"More",
        required=False
    )
    more_url = schema.TextLine(
        title=u'URL for "More" link',
        default=None,
        required=False
    )

class LeadSummaryRenderer(BaseRenderer):

    title = 'Lead Summary Renderer'
    schema = ILeadSummaryRendererSchema
    template = ViewPageTemplateFile('/templates/lead_summary.pt')

class EventsRenderer(BaseRenderer):

    title = 'Events Renderer'
    template = ViewPageTemplateFile('/templates/events.pt')

class RichTextRenderer(BaseRenderer):

    title = 'RichTextRenderer'
    template = ViewPageTemplateFile('/templates/richtext.pt')


class IStaticRichTextSchema(Interface):

    text = schema.Text(
        title=u'Text'
    )

    more_text = schema.TextLine(
        title=u'Title for "More" link',
        default=u"More",
        required=False
    )
    more_url = schema.TextLine(
        title=u'URL for "More" link',
        default=None,
        required=False
    )


class StaticRichTextRenderer(BaseRenderer):
    custom_widgets = {
        'text': WYSIWYGWidget
    }
    schema = IStaticRichTextSchema
    title = 'StaticRichTextRenderer'
    template = ViewPageTemplateFile('/templates/static_richtext.pt')
