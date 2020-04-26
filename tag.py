import sys
if sys.platform == 'win32':
    import os
    import iptcinfo3
else:
    import xattr

def osx_writexattrs(F,TagList):

    """ writexattrs(F,TagList):
    writes the list of tags to three xattr field:
    'kMDItemFinderComment','_kMDItemUserTags','kMDItemOMUserTags'
       This version uses the xattr library """

    plistFront = '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><array>'
    plistEnd = '</array></plist>'
    plistTagString = ''
    for Tag in TagList:
        plistTagString = plistTagString + '<string>{}</string>'.format(Tag)
    TagText = plistFront + plistTagString + plistEnd

    OptionalTag = "com.apple.metadata:"
    XattrList = ["kMDItemFinderComment","_kMDItemUserTags","kMDItemOMUserTags"]
    for Field in XattrList:
        xattr.setxattr (F,OptionalTag+Field,TagText.encode('utf8'))
            # Equivalent shell command is xattr -w com.apple.metadata:kMDItemFinderComment [PLIST value] [File name]

def win_addInfo(F,TagList):
    try:
        info = iptcinfo3.IPTCInfo(F)
        info['keywords'] = TagList
        info.save()
        os.remove(F + '~')
    except:
        print("failed to edit exif data")