import sys

def get_args_args():
    if len(sys.argv) < 2:
        return None,[]
    
    all_args = sys.argv[1:]

    cmd = all_args[0].lower()
    p = all_args[1:]

    return cmd,p