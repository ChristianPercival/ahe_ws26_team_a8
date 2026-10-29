# 2026-10-29T16:11:24.579353100
import vitis

client = vitis.create_client()
client.set_workspace(path="lab_02")

platform = client.get_component(name="microblaze")
status = platform.build()

comp = client.get_component(name="hello_world")
comp.build()

status = platform.build()

status = platform.build()

comp.build()

status = platform.update_hw(hw_design = "$COMPONENT_LOCATION/../lab_02/microblaze_wrapper.xsa")

status = platform.build()

status = platform.build()

comp.build()

vitis.dispose()

