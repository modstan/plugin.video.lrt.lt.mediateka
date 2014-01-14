import urlparse

import xbmcgui
import xbmcplugin

import libmediateka as lm

#item = xbmcgui.ListItem('Naujausi video')
#xbmcplugin.addDirectoryItem(HANDLE, PATH + '?latest=1', item, True)

def draw_meniu(xxx, playeble=False):
    for menu_item in xxx:
        item = xbmcgui.ListItem(menu_item[1])
        if playeble:
            videolink = lm.get_data(menu_item[0], lm.regexp['videolink'])
            if len(videolink):
                xbmcplugin.addDirectoryItem(HANDLE, videolink[0], item)
        else:
            xbmcplugin.addDirectoryItem(HANDLE, PATH+'?meniu=%s' % menu_item[0], item, True)
 
if __name__ == '__main__':
    PATH = sys.argv[0]
    HANDLE = int(sys.argv[1])
    PARAMS = urlparse.parse_qs(sys.argv[2][1:])

    if "meniu" in PARAMS:
        meniu = PARAMS["meniu"][0].split('/')

        if meniu[0] == "laidos":
            if len(meniu) == 1:
                match = [('laidos/abc', 'laidos pagal abecele'), ('laidos/visos', 'visos laidos')]
                draw_meniu(match)
            elif len(meniu) == 2:
                if meniu[1] == 'abc':
                    match = lm.get_data("laidos", lm.regexp['abecele'])
                    draw_meniu(match)
                else:
                    match = lm.get_data(PARAMS["meniu"][0], lm.regexp['laidos'])
                    draw_meniu(match)
            else:
                match = lm.get_data(PARAMS["meniu"][0], lm.regexp['laidu-list'])
                draw_meniu(match, playeble=True)
        elif meniu[0] == "tiesiogiai":
            match = lm.get_data(PARAMS["meniu"][0], lm.regexp['tiesiogiai'])
            draw_meniu(match, playeble=True)
        elif meniu[0] == "temos":
            if len(meniu) == 1:
                match = lm.get_data(PARAMS["meniu"][0], lm.regexp['temos'])
                draw_meniu(match)
        """
        elif meniu[0] == "irasas":
            print("------ rodysiu ------")
            match = lm.get_data(PARAMS["meniu"][0], lm.regexp['videolink'])
            print(match[0])
            item = xbmcgui.ListItem(path=match[0])
            xbmcplugin.setResolvedUrl(HANDLE, True, item)
            print("-------end-----------")
        """
    else:
        match = lm.get_data( '', lm.regexp['pagrindinis'])
        draw_meniu(match)

    xbmcplugin.endOfDirectory(HANDLE)
