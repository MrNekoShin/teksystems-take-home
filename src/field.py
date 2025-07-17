

class Field:
    def __init__(self, width: int, height: int) -> None:
        """Initialize the Field with Width and Height coordinates."""
        if not isinstance(width, int) or not isinstance(height, int) or width < 0 or height < 0:
            raise ValueError("Width and height must be positive integers.")
        
        self.width: int = width
        self.height: int = height

    def __repr__(self) -> str:
        return f"Field(width={self.width}, height={self.height})"
        
    