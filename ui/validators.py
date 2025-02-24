from prompt_toolkit.validation import Validator, ValidationError
from typing import Optional, Union
import logging
from utils.logger import get_logger

logger = get_logger()

class NumberValidator(Validator):
    """Validates numeric input with optional range constraints"""
    
    def __init__(self, 
                 min_val: Optional[Union[int, float]] = None,
                 max_val: Optional[Union[int, float]] = None,
                 allow_float: bool = True,
                 param_name: str = "Value"):
        self.min_val = min_val
        self.max_val = max_val
        self.allow_float = allow_float
        self.param_name = param_name

    def validate(self, document):
        """
        Validates that the input is a number within the specified constraints
        
        Args:
            document: The document to validate

        Raises:
            ValidationError: If the input is invalid
        """
        try:
            text = document.text.strip()
            if not text:
                raise ValidationError(message=f'{self.param_name} cannot be empty')
                
            # Try to convert to number
            try:
                value = float(text) if self.allow_float else int(text)
            except ValueError:
                if self.allow_float:
                    raise ValidationError(message=f'{self.param_name} must be a valid number')
                else:
                    raise ValidationError(message=f'{self.param_name} must be a valid integer')

            # Check range constraints
            if self.min_val is not None and value < self.min_val:
                raise ValidationError(message=f'{self.param_name} must be >= {self.min_val}')
            if self.max_val is not None and value > self.max_val:
                raise ValidationError(message=f'{self.param_name} must be <= {self.max_val}')

            # Log validation success
            logger.debug(f"Validated {self.param_name}: {value}")
            
        except ValidationError as e:
            logger.warning(f"Validation failed for {self.param_name}: {str(e)}")
            raise

class PathValidator(Validator):
    """Validates file paths"""
    
    def __init__(self, must_exist: bool = False, file_type: str = None):
        self.must_exist = must_exist
        self.file_type = file_type

    def validate(self, document):
        """
        Validates that the input is a valid file path
        
        Args:
            document: The document to validate

        Raises:
            ValidationError: If the path is invalid
        """
        try:
            path = document.text.strip()
            if not path:
                raise ValidationError(message='Path cannot be empty')

            # Create Path object
            from pathlib import Path
            path_obj = Path(path)

            # Check if path should exist
            if self.must_exist and not path_obj.exists():
                raise ValidationError(message=f'File {path} does not exist')

            # Check file type if specified
            if self.file_type and not path.endswith(self.file_type):
                raise ValidationError(message=f'File must be a {self.file_type} file')

            logger.debug(f"Validated path: {path}")

        except ValidationError as e:
            logger.warning(f"Path validation failed: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in path validation: {str(e)}")
            raise ValidationError(message=f'Invalid path: {str(e)}')

class ParameterValidator:
    """Factory class for creating appropriate validators based on parameter type"""
    
    @staticmethod
    def create_validator(param_name: str, param_type: type, **constraints):
        """
        Creates an appropriate validator based on parameter type and constraints
        
        Args:
            param_name: Name of the parameter
            param_type: Type of the parameter
            **constraints: Additional constraints (min_val, max_val, etc.)

        Returns:
            Validator: Appropriate validator for the parameter
        """
        if param_type in (int, float):
            return NumberValidator(
                allow_float=param_type is float,
                param_name=param_name,
                **constraints
            )
        elif param_type is str and constraints.get('is_path', False):
            return PathValidator(
                must_exist=constraints.get('must_exist', False),
                file_type=constraints.get('file_type')
            )
        else:
            # For types without specific validation
            return None
