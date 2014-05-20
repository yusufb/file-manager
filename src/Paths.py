BOOKMARKS = "../resources/data/bookmarks.json"
FILE_TYPES = "../resources/data/file_types.json"

if __name__=='__main__':
    print BOOKMARKS
    from os.path import isfile 
    if isfile(BOOKMARKS):
        print "test"