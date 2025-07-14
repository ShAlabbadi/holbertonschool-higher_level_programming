import logging

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and attendee data.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    
    Returns:
        None: Creates output files or logs errors
    """
    
    # Validate input types
    if not isinstance(template, str):
        logging.error(f"Invalid template type. Expected string, got {type(template).__name__}")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        logging.error(f"Invalid attendees type. Expected list of dictionaries, got {type(attendees).__name__}")
        return
    
    # Check for empty template
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    
    # Check for empty attendees list
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Get a copy of the template for each attendee
        invitation = template
        
        # Replace each placeholder with the attendee's data or "N/A" if missing
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")
        
        # Handle None values explicitly
        if event_date is None:
            event_date = "N/A"
        
        # Perform the replacements
        invitation = invitation.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace("{event_location}", str(event_location))
        
        # Write to output file
        filename = f"output_{i}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(invitation)
        except IOError as e:
            logging.error(f"Failed to write file {filename}: {str(e)}")
