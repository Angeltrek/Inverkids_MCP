import re
from typing import Any, List, Optional
from src.utils.exceptions import ValidationError


class Validator:
    """Comprehensive input validation utilities"""
    
    # Patterns
    ENROLLMENT_PATTERN = r"^[A-Z]{3}\d{3,}$"
    
    @staticmethod
    def validate_required(value: Any, field_name: str) -> Any:
        """Validate that a value is provided"""
        if value is None or (isinstance(value, str) and not value.strip()):
            raise ValidationError(f"{field_name} is required", field=field_name)
        return value
    
    @staticmethod
    def validate_enrollment_id(enrollment_id: str) -> str:
        """
        Validate and normalize enrollment ID.
        
        Expected format: STU001, TCH042, ADM100, etc.
        - 3 letters (role prefix)
        - 3+ digits (unique identifier)
        
        Args:
            enrollment_id: Raw enrollment ID
            
        Returns:
            Normalized (uppercase) enrollment ID
            
        Raises:
            ValidationError: If format is invalid
        """
        Validator.validate_required(enrollment_id, "enrollment_id")
        
        if not isinstance(enrollment_id, str):
            raise ValidationError(
                "Enrollment ID must be a string",
                field="enrollment_id"
            )
        
        enrollment_id = enrollment_id.strip().upper()
        
        if len(enrollment_id) < 6:
            raise ValidationError(
                "Enrollment ID too short (minimum 6 characters)",
                field="enrollment_id"
            )
        
        if len(enrollment_id) > 20:
            raise ValidationError(
                "Enrollment ID too long (maximum 20 characters)",
                field="enrollment_id"
            )
        
        if not re.match(Validator.ENROLLMENT_PATTERN, enrollment_id):
            raise ValidationError(
                "Invalid enrollment ID format. Expected: ABC123 "
                "(3 letters followed by 3+ digits)",
                field="enrollment_id"
            )
        
        return enrollment_id
    
    @staticmethod
    def validate_password(password: str) -> None:
        """
        Validate password requirements.
        
        Args:
            password: User password
            
        Raises:
            ValidationError: If password doesn't meet requirements
        """
        Validator.validate_required(password, "password")
        
        if not isinstance(password, str):
            raise ValidationError(
                "Password must be a string",
                field="password"
            )
        
        if len(password) < 6:
            raise ValidationError(
                "Password must be at least 6 characters long",
                field="password"
            )
        
        if len(password) > 128:
            raise ValidationError(
                "Password too long (maximum 128 characters)",
                field="password"
            )
    
    @staticmethod
    def validate_token(token: str) -> str:
        """
        Validate authentication token format.
        
        Args:
            token: JWT or session token
            
        Returns:
            Trimmed token
            
        Raises:
            ValidationError: If token is invalid
        """
        Validator.validate_required(token, "token")
        
        if not isinstance(token, str):
            raise ValidationError(
                "Token must be a string",
                field="token"
            )
        
        token = token.strip()
        
        if len(token) < 10:
            raise ValidationError(
                "Invalid token format (too short)",
                field="token"
            )
        
        return token
    
    @staticmethod
    def validate_level(level: Any) -> str:
        """
        Validate and normalize academic level.
        
        Accepts:
        - Integers: 1, 2, 3
        - Strings: "1", "Level 3", "3ro", "nivel-5"
        
        Args:
            level: Academic level in various formats
            
        Returns:
            Normalized level as string (e.g., "3")
            
        Raises:
            ValidationError: If level is invalid
        """
        Validator.validate_required(level, "level")
        
        # Convert to string
        level_str = str(level).strip().lower()
        
        # Extract numeric part
        match = re.search(r"\d+", level_str)
        if not match:
            raise ValidationError(
                f"Invalid level format: '{level}'. Must contain a number.",
                field="level"
            )
        
        level_num = int(match.group())
        
        # Validate range (assuming K-12 system)
        if level_num < 1 or level_num > 12:
            raise ValidationError(
                f"Level must be between 1 and 12, got: {level_num}",
                field="level"
            )
        
        return str(level_num)
    
    @staticmethod
    def validate_language(lang: str) -> str:
        """
        Validate language code.
        
        Args:
            lang: Language code (ISO 639-1)
            
        Returns:
            Lowercase language code
            
        Raises:
            ValidationError: If language code is invalid
        """
        Validator.validate_required(lang, "language")
        
        lang = lang.strip().lower()
        
        if not re.match(r"^[a-z]{2}$", lang):
            raise ValidationError(
                "Invalid language code. Expected 2-letter ISO code (e.g., 'es', 'en')",
                field="language"
            )
        
        return lang
    
    @staticmethod
    def validate_group_ids(group_ids: List[str]) -> List[str]:
        """
        Validate list of group IDs.
        
        Args:
            group_ids: List of group identifiers
            
        Returns:
            List of validated group IDs
            
        Raises:
            ValidationError: If any ID is invalid
        """
        if not group_ids:
            raise ValidationError(
                "At least one group ID is required",
                field="group_ids"
            )
        
        if not isinstance(group_ids, (list, tuple)):
            raise ValidationError(
                "Group IDs must be a list",
                field="group_ids"
            )
        
        if len(group_ids) > 100:
            raise ValidationError(
                "Too many group IDs (maximum 100)",
                field="group_ids"
            )
        
        validated = []
        for idx, gid in enumerate(group_ids):
            if not gid or not isinstance(gid, str):
                raise ValidationError(
                    f"Invalid group ID at index {idx}: '{gid}'",
                    field="group_ids"
                )
            validated.append(gid.strip())
        
        return validated
    
    @staticmethod
    def validate_user_type(user_type: str) -> str:
        """
        Validate user type.
        
        Args:
            user_type: Type of user
            
        Returns:
            Normalized user type
            
        Raises:
            ValidationError: If user type is invalid
        """
        Validator.validate_required(user_type, "user_type")
        
        user_type = user_type.strip().lower()
        
        valid_types = ["student", "teacher", "admin", "parent"]
        if user_type not in valid_types:
            raise ValidationError(
                f"Invalid user type: '{user_type}'. "
                f"Must be one of: {', '.join(valid_types)}",
                field="user_type"
            )
        
        return user_type