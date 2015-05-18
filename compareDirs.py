from filecmp import dircmp

def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print("Diffs: {} found in folders {} and {}".format(name, dcmp.left,
                                                    dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

dcmp = dircmp('a','b')
print_diff_files(dcmp)
