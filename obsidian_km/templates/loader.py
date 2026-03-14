"""Template loader and variable replacement."""

import re
from pathlib import Path
from typing import Dict, Optional


class TemplateLoader:
    """Loads templates and replaces variables."""
    
    def __init__(self, templates_path: str):
        """
        Initialize template loader.
        
        Args:
            templates_path: Path to templates directory
        """
        self.templates_path = Path(templates_path)
        
    def load_template(self, template_name: str) -> str:
        """
        Load a template file.
        
        Args:
            template_name: Name of the template (e.g., 'daily-note', 'project')
                          Can be with or without .md extension
        
        Returns:
            Template content as string
            
        Raises:
            FileNotFoundError: If template file doesn't exist
        """
        # Add .md extension if not present
        if not template_name.endswith('.md'):
            template_name = f"{template_name}.md"
            
        template_file = self.templates_path / template_name
        
        if not template_file.exists():
            raise FileNotFoundError(f"Template not found: {template_file}")
            
        return template_file.read_text(encoding='utf-8')
    
    def replace_variables(self, template: str, variables: Dict[str, str]) -> str:
        """
        Replace template variables with actual values.
        
        Variables are in the format {{variable_name}}.
        
        Args:
            template: Template content with variables
            variables: Dictionary mapping variable names to values
        
        Returns:
            Template with variables replaced
        """
        result = template
        
        # Replace each variable
        for var_name, var_value in variables.items():
            # Match {{variable_name}} pattern
            pattern = r'\{\{' + re.escape(var_name) + r'\}\}'
            # Escape backslashes in the replacement value to avoid regex interpretation
            escaped_value = str(var_value).replace('\\', '\\\\')
            result = re.sub(pattern, escaped_value, result)
        
        return result
    
    def apply_template(
        self, 
        template_name: str, 
        variables: Dict[str, str],
        keep_unfilled: bool = False
    ) -> str:
        """
        Load a template and replace variables.
        
        Args:
            template_name: Name of the template
            variables: Dictionary mapping variable names to values
            keep_unfilled: If True, keep unfilled variables as {{var}}.
                          If False, replace with empty string.
        
        Returns:
            Template with variables replaced
            
        Raises:
            FileNotFoundError: If template file doesn't exist
        """
        template = self.load_template(template_name)
        result = self.replace_variables(template, variables)
        
        if not keep_unfilled:
            # Remove any remaining unfilled variables
            result = re.sub(r'\{\{[^}]+\}\}', '', result)
        
        return result
    
    def get_template_variables(self, template_name: str) -> list[str]:
        """
        Extract all variable names from a template.
        
        Args:
            template_name: Name of the template
        
        Returns:
            List of variable names found in the template
            
        Raises:
            FileNotFoundError: If template file doesn't exist
        """
        template = self.load_template(template_name)
        
        # Find all {{variable_name}} patterns
        pattern = r'\{\{([^}]+)\}\}'
        matches = re.findall(pattern, template)
        
        # Return unique variable names
        return list(set(matches))
    
    def list_templates(self) -> list[str]:
        """
        List all available templates.
        
        Returns:
            List of template names (without .md extension)
        """
        if not self.templates_path.exists():
            return []
        
        templates = []
        for file in self.templates_path.glob('*.md'):
            templates.append(file.stem)
        
        return sorted(templates)
