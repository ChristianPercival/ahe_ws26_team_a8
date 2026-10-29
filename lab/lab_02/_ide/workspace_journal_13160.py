# 2026-10-29T15:09:00.694929500
import vitis

client = vitis.create_client()
client.set_workspace(path="lab_02")

advanced_options = client.create_advanced_options_dict(dt_overlay="0")

platform = client.create_platform_component(name = "microblaze",hw_design = "$COMPONENT_LOCATION/../lab_02/microblaze_wrapper.xsa",os = "standalone",cpu = "microblaze_0",domain_name = "standalone_microblaze_0",generate_dtb = False,advanced_options = advanced_options,compiler = "gcc")

platform = client.get_component(name="microblaze")
status = platform.build()

comp = client.create_app_component(name="hello_world",platform = "$COMPONENT_LOCATION/../microblaze/export/microblaze/microblaze.xpfm",domain = "standalone_microblaze_0")

status = platform.build()

status = platform.build()

comp = client.get_component(name="hello_world")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

vitis.dispose()

