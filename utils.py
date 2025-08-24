def normalize_and_count(s: str, token: str) -> tuple[str, int]: 
    # trim string
    s_trimmed = s.strip()
    
    # convert to lowercase
    s_lower = s_trimmed.lower()
    
    # collapse spaces, joining is easier than manually checking
    s_collapsed = " ".join(s_lower.split())
    
    # count tokens
    token_lower = token.lower() # just in case
    token_count = s_collapsed.count(token_lower)
    
    return s_collapsed, token_count
    