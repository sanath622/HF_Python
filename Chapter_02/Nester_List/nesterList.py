import sys
"""This is the 01_HF_ListsWithinLists_Function module and it provides one function called print_lol(), which prints lists that may or may not include nested lists"""
def print_lol_1(the_list, indent = False, level=0, fh=sys.stdout):
    """ This function takes a posotional arguement called "the_list", which is any python list(of, possibly nested lists)
    Each data item in the list is recursively printed and printed on to the screen on its own line"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)