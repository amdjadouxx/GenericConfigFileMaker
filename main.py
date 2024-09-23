from GenericConfigFileMaker import GenericConfigFileMaker

# Create an instance of the GenericConfigFileMaker class
config_maker = GenericConfigFileMaker()

# Add a section named "settings"
config_maker.add_section("settings")

# Add fields to the "settings" section
config_maker.add_field_to_section("settings", "resolution_width", 1920)
config_maker.add_field_to_section("settings", "resolution_height", 1080)
config_maker.add_field_to_section("settings", "fullscreen", True)
config_maker.add_field_to_section("settings", "vsync", False)
config_maker.add_field_to_section("settings", "audio_volume", 75)

# Add another section named "network"
config_maker.add_section("network")

# Add fields to the "network" section
config_maker.add_field_to_section("network", "hostname", "localhost")
config_maker.add_field_to_section("network", "port", 8080)

# Add a section named "user"
config_maker.add_section("user")

# Add fields to the "user" section
config_maker.add_field_to_section("user", "username", "admin")
config_maker.add_field_to_section("user", "password", "admin")

# Add a nested section named "advanced" under the "settings" section
config_maker.add_section("advanced", "settings")

# Add fields to the nested "advanced" section
config_maker.add_field_to_section("advanced", "anti_aliasing", True, "settings")
config_maker.add_field_to_section("advanced", "texture_quality", "high", "settings")

# Generate the configuration file named 'generic_config.cfg'
config_maker.generate_file('generic_config.cfg')