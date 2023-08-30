from NetscapeBookmarksFileParser import NetscapeBookmarksFile, BookmarkFolder, BookmarkItem, parser
import os, shutil
import json

data_stash = {}

def interpret_folder(folder: BookmarkFolder, fn: str = "-"):
    cur_out = data_stash[fn] = []
    for item in folder.items:
        if isinstance(item, BookmarkFolder):
            interpret_folder(item, fn+item.name+"-")
        elif isinstance(item, BookmarkItem):
            cur_out.append(item.href)

with open("bookmarks.html", "r", encoding="utf-8") as bmf:
    bm = NetscapeBookmarksFile(bmf)
    bm.parse()
    interpret_folder(bm.bookmarks)

if os.path.exists("dump"):
    shutil.rmtree("dump")
os.mkdir("dump")

for fn, data in data_stash.items():
    if len(data) <= 0: continue
    fp = f"dump/%s.json" % fn
    with open(fp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)