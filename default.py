# -*- coding: utf-8 -*-

from __future__ import division

import os
import sys
import urllib

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

__plugin_handle__ = int(sys.argv[1])
ADDON = xbmcaddon.Addon(id='plugin.video.iplayerwww')
sys.path.insert(0, os.path.join(xbmcaddon.Addon("plugin.video.iplayerwww").getAddonInfo("path"),
                                'resources', 'lib'))


try:
    import ipwww_common as Common
    import ipwww_video as Video
    import ipwww_radio as Radio
    Video.ADDON = ADDON
    Radio.ADDON = ADDON
except ImportError, error:
    print error
    print sys.path
    d = xbmcgui.Dialog()
    d.ok(str(error), 'Please check you installed this plugin correctly.')
    raise


def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params) - 1] == '/'):
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param


params = get_params()
content_type = None
url = None
name = None
mode = None
iconimage = None
description = None
subtitles_url = None
logged_in = False
keyword = None


def CATEGORIES():
    if content_type == "video":
        Common.AddMenuEntry(Common.translation(31000), 'iplayer', 106, '', '', '')
        Common.AddMenuEntry(Common.translation(31017), 'url', 109, '', '', '')
        Common.AddMenuEntry(Common.translation(31001), 'url', 105, '', '', '')
        Common.AddMenuEntry(Common.translation(31002), 'url', 102, '', '', '')
        Common.AddMenuEntry(Common.translation(31003), 'url', 103, '', '', '')
        Common.AddMenuEntry(Common.translation(31004), 'url', 104, '', '', '')
        Common.AddMenuEntry(Common.translation(31005), 'url', 101, '', '', '')
        Common.AddMenuEntry(Common.translation(31006), 'url', 107, '', '', '')
        Common.AddMenuEntry(Common.translation(31007), 'url', 108, '', '', '')
    elif content_type == "audio":
        Common.AddMenuEntry("Live National Radio HQ", 'url', 118, '', '', '')
        Common.AddMenuEntry("Live Radio", 'url', 113, '', '', '')
        Common.AddMenuEntry("Radio A-Z", 'url', 112, '', '', '')
        Common.AddMenuEntry("Radio Genres", 'url', 114, '', '', '')
        Common.AddMenuEntry("Radio Search", 'url', 115, '', '', '')
        Common.AddMenuEntry("Radio Most Popular", 'url', 116, '', '', '')
        Common.AddMenuEntry("Radio Favourites", 'url', 117, '', '', '')


try:
    content_type = Common.utf8_unquote_plus(params["content_type"])
except:
    pass
try:
    url = Common.utf8_unquote_plus(params["url"])
except:
    pass
try:
    name = Common.utf8_unquote_plus(params["name"])
except:
    pass
try:
    iconimage = Common.utf8_unquote_plus(params["iconimage"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass
try:
    description = Common.utf8_unquote_plus(params["description"])
except:
    pass
try:
    subtitles_url = Common.utf8_unquote_plus(params["subtitles_url"])
except:
    pass
try:
    logged_in = params['logged_in'] == 'True'
except:
    pass
try:
    keyword = Common.utf8_unquote_plus(params["keyword"])
except:
    pass



# These are the modes which tell the plugin where to go.
if mode is None or url is None or len(url) < 1:
    CATEGORIES()

# Modes 101-119 will create a main directory menu entry
elif mode == 101:
    Video.ListLive()

elif mode == 102:
    Video.ListAtoZ()

elif mode == 103:
    Video.ListCategories()

elif mode == 104:
    Video.Search(keyword)

elif mode == 105:
    Video.ListMostPopular()

elif mode == 106:
    Video.ListHighlights(url)

elif mode == 107:
    Video.ListWatching(logged_in)

elif mode == 108:
    Video.ListFavourites(logged_in)

elif mode == 109:
    Video.ListChannelHighlights()

elif mode == 112:
    Radio.ListAtoZ()

elif mode == 113:
    Radio.ListLive()

elif mode == 114:
    Radio.ListGenres()

elif mode == 115:
    Radio.Search(keyword)

elif mode == 116:
    Radio.ListMostPopular()

elif mode == 117:
    Radio.ListFavourites(logged_in)

elif mode == 118:
    Radio.ListLiveHQ()

    # Modes 121-199 will create a sub directory menu entry
elif mode == 121:
    Video.GetEpisodes(url)

elif mode == 122:
    Video.GetAvailableStreams(name, url, iconimage, description)

elif mode == 123:
    Video.AddAvailableLiveStreamsDirectory(name, url, iconimage)

elif mode == 124:
    Video.GetAtoZPage(url)

elif mode == 125:
    Video.ListCategoryFilters(url)

elif mode == 126:
    Video.GetFilteredCategory(url)

elif mode == 127:
    Video.GetGroup(url)

elif mode == 128:
    Video.ScrapeEpisodes(url)

elif mode == 131:
    Radio.GetEpisodes(url)

elif mode == 132:
    Radio.GetAvailableStreams(name, url, iconimage, description)

elif mode == 133:
    Radio.AddAvailableLiveStreamsDirectory(name, url, iconimage)

elif mode == 134:
    Radio.GetAtoZPage(url)

elif mode == 135:
    Radio.GetGenrePage(url)

# Modes 201-299 will create a playable menu entry, not a directory
elif mode == 201:
    Video.PlayStream(name, url, iconimage, description, subtitles_url)

elif mode == 202:
    Video.AddAvailableStreamItem(name, url, iconimage, description)

elif mode == 203:
    Video.AddAvailableLiveStreamItem(name, url, iconimage)

elif mode == 211:
    Radio.PlayStream(name, url, iconimage, description, subtitles_url)

elif mode == 212:
    Radio.AddAvailableStreamItem(name, url, iconimage, description)

elif mode == 213:
    Radio.AddAvailableLiveStreamItem(name, url, iconimage)

elif mode == 214:
    Radio.AddAvailableLiveStreamItemHQ(name, url, iconimage)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
