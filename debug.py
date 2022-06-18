INPUT = """\
test
"""
#region ########################################
import io, sys
sys.stdin = io.StringIO(INPUT)
#endregion #####################################

s = input()

print(s)

