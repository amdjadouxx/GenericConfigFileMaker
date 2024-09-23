class GenericConfigFileMaker:
    """
    Class to generate configuration files in a generic way.

    Attributes:
    -----------
    sections : dict
        Dictionary containing sections and their fields.

    Methods:
    --------
    add_section(section_name, parent_section=None):
        Adds a section to the configuration file.
    
    add_field_to_section(section_name, field_name, field_value, parent_section=None):
        Adds a field to a specific section.
    
    generate_file(filename):
        Generates the configuration file with the added sections and fields.
    """

    def __init__(self):
        self.sections = {}

    def add_section(self, section_name, parent_section=None):
        """
        Adds a section to the configuration file.

        Parameters:
        -----------
        section_name : str
            The name of the section to add.
        
        parent_section : str, optional
            The name of the parent section if the section is nested.
        """
        if parent_section:
            if parent_section not in self.sections:
                self.sections[parent_section] = {}
            if section_name not in self.sections[parent_section]:
                self.sections[parent_section][section_name] = {}
        else:
            if section_name not in self.sections:
                self.sections[section_name] = {}

    def add_field_to_section(self, section_name, field_name, field_value, parent_section=None):
        """
        Adds a field to a specific section.

        Parameters:
        -----------
        section_name : str
            The name of the section to add the field to.
        
        field_name : str
            The name of the field to add.
        
        field_value : any
            The value of the field to add.
        
        parent_section : str, optional
            The name of the parent section if the section is nested.
        """
        if parent_section:
            if parent_section not in self.sections:
                self.add_section(parent_section)
            if section_name not in self.sections[parent_section]:
                self.add_section(section_name, parent_section)
            self.sections[parent_section][section_name][field_name] = field_value
        else:
            if section_name not in self.sections:
                self.add_section(section_name)
            self.sections[section_name][field_name] = field_value

    def generate_file(self, filename):
        """
        Generates the configuration file with the added sections and fields.

        Parameters:
        -----------
        filename : str
            The name of the configuration file to generate.
        """
        def write_section(f, section_name, fields, indent=0):
            indent_str = ' ' * indent
            f.write(f"{indent_str}{section_name} = {{\n")
            for key, value in fields.items():
                if isinstance(value, dict):
                    write_section(f, key, value, indent + 4)
                else:
                    f.write(f"{indent_str}    {key} = {value};\n")
            f.write(f"{indent_str}}};\n")

        with open(filename, 'w') as f:
            for section_name, fields in self.sections.items():
                write_section(f, section_name, fields)