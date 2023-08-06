def extract_errormsg(code_as_string):
    # Run code_as_string, and return the error message as string if any
    try:
        exec(code_as_string)
        result = None
    except Exception as e:
        result = str(e)
    
    return result