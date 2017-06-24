import sys
import getopt


def usage():
    """
    prints usage
    """
    print("#########################\n\n-h display helptext\n-t + option dislays something")

def test(a):
    """
    something
    """
     print("Arguments ar:" +str(a))

    try:
        opts, args = getopt.getopt(sys.argv[1:], 't:h', ['test=','help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(2)
        elif opt in ("-t","--test"):
            test(arg)
        else:
            usage()
            sys.exit(2)
