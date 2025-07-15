
class Field:
    def __init__(self, width, height):
        """Initialize the Field with Width and Height coordinates."""
        if not isinstance(width, int) or not isinstance(height, int) or width < 0 or height < 0:
            raise ValueError("Width and height must be positive integers.")
        
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Field(width={self.width}, height={self.height})"
        
    