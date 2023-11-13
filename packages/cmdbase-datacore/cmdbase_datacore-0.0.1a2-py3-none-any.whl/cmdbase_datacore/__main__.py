from cmdbase_utils import main_base
from .commons import Context
from .commands import add_arguments, all_handle

def main():
    main_base(Context, add_arguments=add_arguments, default_handle=all_handle)

if __name__ == '__main__':
    main()
