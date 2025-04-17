def sanitize_filename(name):
    """
    Sanitizes a string to be used as a filename by replacing problematic characters.
    
    Args:
        name (str): The original filename that may contain invalid characters
        
    Returns:
        str: A sanitized filename with invalid characters replaced
    """
    # Replace forward slashes with hyphens to avoid directory path issues
    # Replace spaces with underscores for better compatibility across systems
    # Additional characters could be handled here if needed (e.g., ?, *, :, etc.)
    return name.replace("/", "-").replace(" ", "_")