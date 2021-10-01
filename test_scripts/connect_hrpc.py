import hrpyc

connection, hou = hrpyc.import_remote_module()
color = hou.node("/obj/geo1/color1")
print(hou.node("/obj/geo1/color1"))
color.parm("colorr").set(1)
color.parm("colorg").set(0)
color.parm("colorb").set(1)
