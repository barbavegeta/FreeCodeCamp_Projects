def add_time(start, duration, day_of_week=None):
    # Days of the week in order, for reference
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Parse start time and duration
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    dur_hour, dur_minute = map(int, duration.split(":"))
    
    # Convert start time to 24-hour format
    if period == "PM":
        start_hour += 12 if start_hour < 12 else 0
    elif start_hour == 12:
        start_hour = 0

    # Calculate total minutes
    total_minutes = start_minute + dur_minute
    total_hours = start_hour + dur_hour + (total_minutes // 60)
    total_minutes %= 60
    days_later = total_hours // 24
    final_hour = total_hours % 24
    
    # Determine AM/PM and convert final_hour to 12-hour format
    final_period = "AM" if final_hour < 12 else "PM"
    final_hour = final_hour % 12 if final_hour % 12 != 0 else 12
    
    # Prepare final time string
    new_time = f"{final_hour}:{total_minutes:02d} {final_period}"

    # Calculate new day of the week, if given
    if day_of_week:
        day_index = days_of_week.index(day_of_week.capitalize())
        new_day = days_of_week[(day_index + days_later) % 7]
        new_time += f", {new_day}"

    # Add day information
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time
