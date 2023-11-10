from ever_playground import *
gen_dict = assemble("""
  NEWC PUSHINT 0 STUR 8 ENDC
  PUSHINT 1
  SETLIBCODE
  PUSHCTR c5
""")
res = runvm(Slice(gen_dict), [], capabilities = 0x800)
print(res.state.cc.stack[0])
