# 8-14 Cars
# Write a func that stores cars in a dictionary. 
# It should always receive manufacturer and model name. 
# Make it also accept arbitrary number of kwargs. 
# Print it at the end to make sure all is good. 
def make_car(manufacturer, model, **kwargs):
    """Create a dictionary with car information."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model

    return kwargs

nissan_car = make_car('nissan', 'fairlady z', color = 'green', \
    tow_package = True)\

print(nissan_car)