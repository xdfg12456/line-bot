import os
import json
from linebot import LineBotApi, WebhookHandler
import os
import json
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    TextSendMessage, StickerSendMessage, ImageSendMessage, VideoSendMessage,
    AudioSendMessage, LocationSendMessage, TemplateSendMessage, CarouselTemplate,
    CarouselColumn, ButtonsTemplate, PostbackAction, URIAction, MessageAction,
    ImageCarouselTemplate, ImageCarouselColumn, QuickReply, QuickReplyButton,
    ConfirmTemplate, CameraAction, CameraRollAction, LocationAction,
    DatetimePickerAction, FlexSendMessage, BubbleContainer, BoxComponent,
    TextComponent, ImageComponent, ImagemapSendMessage, BaseSize,
    URIImagemapAction, MessageImagemapAction, ImagemapArea
) # 看需要用到甚麼再import甚麼

token = 'haqKuA8wK6tb6ufQT7RoL+lpp//xk9w/kCtmgZ3sgng+WHJa67GtnPa/s5TOzcPQETmcMQWKR92/59e9mtVbtbGVO+VGML8nPkERjRxw5gSo+feO2xSB+GOsrXg7Tp8Ypnghkn+5AF51mFUHwYoetQdB04t89/1O/w1cDnyilFU='
secret = '2e8243533a67cd9fca5a885d1091b244'
