import pytest
from src.app.validators import Validator
from src.utils.exceptions import ValidationError


class TestValidator:
    """Tests for input validation utilities"""
    
    # -------------------------------------------------------------------------
    # Enrollment ID Validation
    # -------------------------------------------------------------------------
    
    def test_validate_enrollment_id_valid(self):
        """Test valid enrollment IDs"""
        # Standard format
        assert Validator.validate_enrollment_id("STU001") == "STU001"
        
        # Lowercase should be normalized to uppercase
        assert Validator.validate_enrollment_id("stu001") == "STU001"
        
        # Different roles
        assert Validator.validate_enrollment_id("TCH042") == "TCH042"
        assert Validator.validate_enrollment_id("ADM100") == "ADM100"
        
        # More digits
        assert Validator.validate_enrollment_id("STU12345") == "STU12345"
    
    def test_validate_enrollment_id_empty(self):
        """Test empty enrollment ID"""
        with pytest.raises(ValidationError) as exc_info:
            Validator.validate_enrollment_id("")
        
        assert "required" in str(exc_info.value).lower()
        assert exc_info.value.details.get("field") == "enrollment_id"
    
    def test_validate_enrollment_id_too_short(self):
        """Test too short enrollment ID"""
        with pytest.raises(ValidationError) as exc_info:
            Validator.validate_enrollment_id("AB1")
        
        assert "short" in str(exc_info.value).lower()
    
    def test_validate_enrollment_id_invalid_format(self):
        """Test invalid formats"""
        # No letters
        with pytest.raises(ValidationError):
            Validator.validate_enrollment_id("123456")
        
        # No digits
        with pytest.raises(ValidationError):
            Validator.validate_enrollment_id("ABCDEF")
        
        # Special characters
        with pytest.raises(ValidationError):
            Validator.validate_enrollment_id("STU-001")
    
    def test_validate_enrollment_id_whitespace(self):
        """Test that whitespace is handled"""
        assert Validator.validate_enrollment_id("  STU001  ") == "STU001"
    
    # -------------------------------------------------------------------------
    # Password Validation
    # -------------------------------------------------------------------------
    
    def test_validate_password_valid(self):
        """Test valid passwords"""
        Validator.validate_password("password123")
        Validator.validate_password("mySecureP@ss!")
        Validator.validate_password("123456")  # Minimum length
    
    def test_validate_password_empty(self):
        """Test empty password"""
        with pytest.raises(ValidationError) as exc_info:
            Validator.validate_password("")
        
        assert "required" in str(exc_info.value).lower()
    
    def test_validate_password_too_short(self):
        """Test password too short"""
        with pytest.raises(ValidationError) as exc_info:
            Validator.validate_password("12345")
        
        assert "6 characters" in str(exc_info.value).lower()
    
    def test_validate_password_too_long(self):
        """Test password too long"""
        long_password = "a" * 129
        with pytest.raises(ValidationError):
            Validator.validate_password(long_password)
    
    # -------------------------------------------------------------------------
    # Token Validation
    # -------------------------------------------------------------------------
    
    def test_validate_token_valid(self):
        """Test valid tokens"""
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.test"
        assert Validator.validate_token(token) == token
        
        # With whitespace
        assert Validator.validate_token(f"  {token}  ") == token
    
    def test_validate_token_empty(self):
        """Test empty token"""
        with pytest.raises(ValidationError):
            Validator.validate_token("")
    
    def test_validate_token_too_short(self):
        """Test token too short"""
        with pytest.raises(ValidationError):
            Validator.validate_token("short")
    
    # -------------------------------------------------------------------------
    # Level Validation
    # -------------------------------------------------------------------------
    
    def test_validate_level_integer(self):
        """Test integer levels"""
        assert Validator.validate_level(1) == "1"
        assert Validator.validate_level(5) == "5"
        assert Validator.validate_level(12) == "12"
    
    def test_validate_level_string_numeric(self):
        """Test numeric string levels"""
        assert Validator.validate_level("3") == "3"
        assert Validator.validate_level("10") == "10"
    
    def test_validate_level_string_with_text(self):
        """Test levels with descriptive text"""
        assert Validator.validate_level("Level 3") == "3"
        assert Validator.validate_level("3ro grado") == "3"
        assert Validator.validate_level("nivel-5") == "5"
    
    def test_validate_level_out_of_range(self):
        """Test levels outside valid range"""
        with pytest.raises(ValidationError) as exc_info:
            Validator.validate_level(0)
        assert "between 1 and 12" in str(exc_info.value)
        
        with pytest.raises(ValidationError):
            Validator.validate_level(13)
    
    def test_validate_level_invalid_format(self):
        """Test invalid level formats"""
        with pytest.raises(ValidationError):
            Validator.validate_level("invalid")
        
        with pytest.raises(ValidationError):
            Validator.validate_level("abc")
    
    # -------------------------------------------------------------------------
    # Language Validation
    # -------------------------------------------------------------------------
    
    def test_validate_language_valid(self):
        """Test valid language codes"""
        assert Validator.validate_language("es") == "es"
        assert Validator.validate_language("en") == "en"
        assert Validator.validate_language("fr") == "fr"
        
        # Uppercase should be normalized
        assert Validator.validate_language("ES") == "es"
    
    def test_validate_language_invalid(self):
        """Test invalid language codes"""
        # Too long
        with pytest.raises(ValidationError):
            Validator.validate_language("esp")
        
        # Too short
        with pytest.raises(ValidationError):
            Validator.validate_language("e")
        
        # With numbers
        with pytest.raises(ValidationError):
            Validator.validate_language("e1")
    
    # -------------------------------------------------------------------------
    # Group IDs Validation
    # -------------------------------------------------------------------------
    
    def test_validate_group_ids_valid(self):
        """Test valid group IDs"""
        ids = ["group_1", "group_2", "group_3"]
        assert Validator.validate_group_ids(ids) == ids
    
    def test_validate_group_ids_empty_list(self):
        """Test empty list"""
        with pytest.raises(ValidationError) as exc_info:
            Validator.validate_group_ids([])
        
        assert "at least one" in str(exc_info.value).lower()
    
    def test_validate_group_ids_not_list(self):
        """Test non-list input"""
        with pytest.raises(ValidationError):
            Validator.validate_group_ids("group_1")
    
    def test_validate_group_ids_too_many(self):
        """Test too many group IDs"""
        ids = [f"group_{i}" for i in range(101)]
        with pytest.raises(ValidationError) as exc_info:
            Validator.validate_group_ids(ids)
        
        assert "100" in str(exc_info.value)
    
    def test_validate_group_ids_invalid_id(self):
        """Test invalid ID in list"""
        with pytest.raises(ValidationError):
            Validator.validate_group_ids(["group_1", "", "group_3"])
        
        with pytest.raises(ValidationError):
            Validator.validate_group_ids(["group_1", None, "group_3"])