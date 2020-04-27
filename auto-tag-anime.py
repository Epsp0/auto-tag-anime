import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import model
import tag

class addAnimeTags():
    def __init__(self):
        self.model = model.deepdanbooruModel()

    def navigateDir(self, path):
        if os.path.isdir(path): 
            for root, dirs, files in os.walk(path):
                for filename in files:
                    print(self.addTagsToImage(root + '/' + filename))
        else:
            print(self.addTagsToImage(path))

    def addTagsToImage(self, path):
        
        if sys.platform == 'win32':   
            file_ext = path[len(path)-3:len(path)]
            if file_ext != 'jpg' and file_ext != 'jpeg':
                return path + " is not a JPEG, no exif data"
        
        status, tags = self.model.classify_image(path)
        if status == 'success':
            self.add_tags(path, tags)
            return 'added ' + str(len(tags)) + ' tags to ' + path
        else:
            return 'failed to add tags for ' + path
            
    def add_tags(self, file, tags):
        if sys.platform == "linux" or sys.platform == "darwin":
            tag.osx_writexattrs(file, tags)
        elif sys.platform == 'win32':
            tag.win_addInfo(file, tags)
    
def parseArgs():
    if len(sys.argv) < 2:
        print("no path")
        sys.exit()

    if not os.path.exists(sys.argv[1]):
        print('path does not exist')
        sys.exit()

if __name__ == "__main__":
    parseArgs()
    addAnimeTags = addAnimeTags()
    addAnimeTags.navigateDir(sys.argv[1])